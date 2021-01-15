import numpy as np
import torch
import torch.fft
import math

class ST_mycode_new(object):
    def __init__(self, filters_set, J, L, device='cpu'):
        self.M, self.N = filters_set['psi'][0][0].shape
        dtype = filters_set['psi'][0][0].dtype
        self.device = device
        self.filters_set = torch.zeros((J,L,self.M,self.N), dtype=dtype)
        if device=='gpu':
            self.filters_set = self.filters_set.cuda()
        for j in range(J):
            for l in range(L):
                self.filters_set[j,l] = filters_set['psi'][j*L+l][0]
    
    def cut_high_k_off(self, data_f, j=2):
            M = data_f.shape[-2]
            N = data_f.shape[-1]
            dx = M//2**j
            dy = N//2**j
            result = torch.cat(
                (torch.cat(
                    ( data_f[...,:dx, :dy] , data_f[...,-dx:, :dy]
                    ), -2),
                 torch.cat(
                    ( data_f[...,:dx, -dy:] , data_f[...,-dx:, -dy:]
                    ), -2)
                ),-1)
            return result

    def forward(self, data, J, L,
                j1j2_criteria='j2>j1', mask=None, pseudo_coef=1,
                algorithm='fast',):
        M, N = self.M, self.N
        data = torch.from_numpy(data)
        data_f = torch.fft.fftn(data, dim=(-2,-1))
        
        S_0 = torch.zeros(1, dtype=data.dtype)  
        S_1 = torch.zeros((J,L), dtype=data.dtype)
        S_2 = torch.zeros((J,L,J,L), dtype=data.dtype)
        S_2_reduced = torch.zeros((J,J,L), dtype=data.dtype)
        if self.device=='gpu':
            S_1 = S_1.cuda()
            S_2 = S_2.cuda()
            S_2_reduced = S_2_reduced.cuda()
        S_0[0] = data.mean()
        
        if algorithm == 'classic':
            filters_set = self.filters_set

            I_1_temp  = torch.fft.ifftn(
                data_f[None,None,:,:] * filters_set,
                dim=(-2,-1),
            ).abs()**pseudo_coef
            S_1 = I_1_temp.mean((-2,-1))

            I_1_temp_f = torch.fft.fftn(I_1_temp, dim=(-2,-1))
            for j1 in np.arange(J):
                for j2 in np.arange(J):
                    if eval(j1j2_criteria):
                        I_2_temp = torch.fft.ifftn(
                            I_1_temp_f[j1,:,None,:,:] * filters_set[j2,None,:,:,:], 
                            dim=(-2,-1),
                        ).abs()**pseudo_coef
                        S_2[j1,:,j2,:] = I_2_temp.mean((-2,-1))
        
        if algorithm == 'fast':
            # only use the low-k Fourier coefs when calculating 
            # large-j scattering coefs.
            for j1 in np.arange(J):
                if j1>=1:
                    data_f_small = self.cut_high_k_off(data_f, j1)
                    wavelet_f = self.cut_high_k_off(self.filters_set[j1], j1)
                else:
                    data_f_small = data_f
                    wavelet_f = self.filters_set[j1]
                _, M1, N1 = wavelet_f.shape
                I_1_temp  = torch.fft.ifftn(
                    data_f_small[None,:,:] * wavelet_f,
                    dim=(-2,-1),
                ).abs()**pseudo_coef
                S_1[j1] = I_1_temp.mean((-2,-1))* M1*N1/M/N
                
                I_1_temp_f = torch.fft.fftn(I_1_temp, dim=(-2,-1))
                for j2 in np.arange(J):
                    if eval(j1j2_criteria):
                        if j1>=1:
                            factor = j2-j1+1
                        else:
                            factor = j2
                        I_1_temp_f_small = self.cut_high_k_off(I_1_temp_f, factor)
                        wavelet_f2 = self.cut_high_k_off(self.filters_set[j2], j2)
                        _, M2, N2 = wavelet_f2.shape
                        I_2_temp = torch.fft.ifftn(
                            I_1_temp_f_small[:,None,:,:] * wavelet_f2[None,:,:,:], 
                            dim=(-2,-1),
                        ).abs()**pseudo_coef
                        S_2[j1,:,j2,:] = I_2_temp.mean((-2,-1)) * M2*N2/M/N                      
        
        for l1 in range(L):
            for l2 in range(L):
                S_2_reduced[:,:,(l2-l1)%L] += S_2[:,l1,:,l2]
        S_2_reduced /= L
        
        S = torch.cat(( S_0, S_1.sum(1), S_2_reduced.flatten()  )).numpy()
        return S, S_0, S_1, S_2



class FiltersSet(object):
    def __init__(self, M, N, J, L):
        self.M = M
        self.N = N
        self.J = J
        self.L = L

    def generate_morlet(self, if_save=False, save_dir=None, precision='double'):
        psi = []
        for j in range(self.J):
            for theta in range(self.L):
                wavelet = self.morlet_2d(
                    M=self.M, 
                    N=self.N, 
                    sigma=0.8 * 2**j, 
                    theta=(int(self.L-self.L/2-1)-theta) * np.pi / self.L, 
                    xi=3.0 / 4.0 * np.pi /2**j, 
                    slant=4.0/self.L,
                )
                wavelet_Fourier = np.fft.fft2(wavelet)
                wavelet_Fourier[0,0] = 0
                if precision=='double':
                    psi.append([torch.from_numpy(wavelet_Fourier.real)])
                if precision=='single':
                    psi.append([torch.from_numpy(wavelet_Fourier.real.astype(np.float32))])

        filters_set_mycode = {'psi':psi}
        if if_save:
            np.save(
                save_dir + 'filters_set_mycode_M' + str(self.M) + 'N' + str(self.N)
                + 'J' + str(self.J) + 'L' + str(self.L) + '_' + precision + '.npy', 
                np.array([{'filters_set': filters_set_mycode}])
            )
        else:
            return filters_set_mycode

    def morlet_2d(self, M, N, sigma, theta, xi, slant=0.5, offset=0, fft_shift=False):
        """
            Computes a 2D Morlet filter.
            A Morlet filter is the sum of a Gabor filter and a low-pass filter
            to ensure that the sum has exactly zero mean in the temporal domain.
            It is defined by the following formula in space:
            psi(u) = g_{sigma}(u) (e^(i xi^T u) - beta)
            where g_{sigma} is a Gaussian envelope, xi is a frequency and beta is
            the cancelling parameter.

            Parameters
            ----------
            M, N : int
                spatial sizes
            sigma : float
                bandwidth parameter
            xi : float
                central frequency (in [0, 1])
            theta : float
                angle in [0, pi]
            slant : float, optional
                parameter which guides the elipsoidal shape of the morlet
            offset : int, optional
                offset by which the signal starts
            fft_shift : boolean
                if true, shift the signal in a numpy style

            Returns
            -------
            morlet_fft : ndarray
                numpy array of size (M, N)
        """
        wv = self.gabor_2d(M, N, sigma, theta, xi, slant, offset, fft_shift)
        wv_modulus = self.gabor_2d(M, N, sigma, theta, 0, slant, offset, fft_shift)
        K = np.sum(wv) / np.sum(wv_modulus)

        mor = wv - K * wv_modulus
        return mor

    def gabor_2d(self, M, N, sigma, theta, xi, slant=1.0, offset=0, fft_shift=False):
        """
            Computes a 2D Gabor filter.
            A Gabor filter is defined by the following formula in space:
            psi(u) = g_{sigma}(u) e^(i xi^T u)
            where g_{sigma} is a Gaussian envelope and xi is a frequency.

            Parameters
            ----------
            M, N : int
                spatial sizes
            sigma : float
                bandwidth parameter
            xi : float
                central frequency (in [0, 1])
            theta : float
                angle in [0, pi]
            slant : float, optional
                parameter which guides the elipsoidal shape of the morlet
            offset : int, optional
                offset by which the signal starts
            fft_shift : boolean
                if true, shift the signal in a numpy style

            Returns
            -------
            morlet_fft : ndarray
                numpy array of size (M, N)
        """
        gab = np.zeros((M, N), np.complex128)
        R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]], np.float64)
        R_inv = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]], np.float64)
        D = np.array([[1, 0], [0, slant * slant]])
        curv = np.dot(R, np.dot(D, R_inv)) / ( 2 * sigma * sigma)

        for ex in [-2, -1, 0, 1, 2]:
            for ey in [-2, -1, 0, 1, 2]:
                [xx, yy] = np.mgrid[offset + ex * M:offset + M + ex * M, offset + ey * N:offset + N + ey * N]
                arg = -(curv[0, 0] * np.multiply(xx, xx) + (curv[0, 1] + curv[1, 0]) * np.multiply(xx, yy) + curv[
                    1, 1] * np.multiply(yy, yy)) + 1.j * (xx * xi * np.cos(theta) + yy * xi * np.sin(theta))
                gab = gab + np.exp(arg)

        norm_factor = (2 * np.pi * sigma * sigma / slant)
        gab = gab / norm_factor

        if (fft_shift):
            gab = np.fft.fftshift(gab, axes=(0, 1))
        return gab
