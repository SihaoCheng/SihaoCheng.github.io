import numpy as np
import torch
import torch.fft
import math

class ST_mycode(object):
    def __init__(self, filters_set):
        self.filters_set = filters_set

    def forward(self, data, J, L, backend='torch', input_dtype='numpy',
                  j1j2_criteria='j2>j1', mask=None, pseudo_coef=1):
        # Number of coefficients per layer
        filters_set = self.filters_set
        self.M = data.shape[-2]
        self.N = data.shape[-1]

        if mask is not None:
            mask /= mask.mean()
        else:
            mask = 1

        if input_dtype=='numpy': 
            S_0 = np.zeros(1, dtype=data.dtype)
            S_1 = np.zeros((J,L), dtype=data.dtype)
            S_2 = np.zeros((J,L,J,L), dtype=data.dtype)
            S_2_reduced = np.zeros((J,J,L), dtype=data.dtype)
        elif input_dtype=='torch':
            S_0 = torch.zeros(1, dtype=data.dtype)
            S_1 = torch.zeros((J,L), dtype=data.dtype)
            S_2 = torch.zeros((J,L,J,L), dtype=data.dtype)
            S_2_reduced = torch.zeros((J,J,L), dtype=data.dtype)
        S_0[0] = data.mean()
        
        if backend=='torch':
            if input_dtype=='numpy':
                data = torch.from_numpy(data)
            data_f = torch.fft.fftn(data, dim=(-2,-1))
            for j1 in np.arange(J):
                for l1 in np.arange(L):
                    I_1_temp  = torch.fft.ifftn(
                        data_f * filters_set['psi'][j1*L+l1][0],
                        dim=(-2,-1),
                    ).abs()**pseudo_coef
                    S_1[j1,l1] = (I_1_temp.numpy() * mask).mean()

                    I_1_temp_f = torch.fft.fftn(I_1_temp, dim=(-2,-1))
                    for j2 in np.arange(J):
                        if eval(j1j2_criteria):
                            for l2 in np.arange(L):
                                I_2_temp = torch.fft.ifftn(
                                    I_1_temp_f * filters_set['psi'][j2*L+l2][0], 
                                    dim=(-2,-1),
                                ).abs()**pseudo_coef
                                S_2[j1,l1,j2,l2] = (I_2_temp.numpy() * mask).mean()
        if backend=='numpy':
            data_f = np.fft.fft2(data)
            for j1 in np.arange(J):
                for l1 in np.arange(L):
                    I_1_temp  = np.abs(np.fft.ifft2(
                         data_f * filters_set['psi'][j1*L+l1][0]
                    ))**pseudo_coef
                    S_1[j1,l1] = (I_1_temp * mask).mean()

                    I_1_temp_f = np.fft.fft2(I_1_temp)
                    for j2 in np.arange(J):
                        if eval(j1j2_criteria):
                            for l2 in np.arange(L):
                                I_2_temp = np.abs(np.fft.ifft2(
                                    I_1_temp_f * filters_set['psi'][j2*L+l2][0]
                                ))**pseudo_coef
                                S_2[j1,l1,j2,l2] = (I_2_temp * mask).mean()
                                # what about masks?
        
        for l1 in range(L):
            for l2 in range(L):
                S_2_reduced[:,:,(l2-l1)%L] += S_2[:,l1,:,l2]
        S_2_reduced /= L
        
        if input_dtype=='numpy':
            S = np.concatenate(( S_0, S_1.sum(1), S_2_reduced.flatten() ))
        if input_dtype=='torch':
            S = torch.cat(( S_0, S_1.sum(1), S_2_reduced.flatten()  )).numpy()
        return S, S_0, S_1, S_2

        
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
        
        if algorithm == 'classic_loop':
            filters_set = self.filters_set
            
            for j1 in np.arange(J):
                for l1 in np.arange(L):
                    I_1_temp  = torch.fft.ifftn(
                        data_f * filters_set[j1, l1],
                        dim=(-2,-1),
                    ).abs()**pseudo_coef
                    S_1[j1, l1] = I_1_temp.mean((-2,-1))

                    I_1_temp_f = torch.fft.fftn(I_1_temp, dim=(-2,-1))
                    for j2 in np.arange(J):
                        if eval(j1j2_criteria):
                            I_2_temp = torch.fft.ifftn(
                                I_1_temp_f[None,:,:] * filters_set[j2,:,:,:], 
                                dim=(-2,-1),
                            ).abs()**pseudo_coef
                            S_2[j1,l1,j2,:] = I_2_temp.mean((-2,-1))
        
        if algorithm == 'classic_2loop':
            filters_set = self.filters_set
            
            for j1 in np.arange(J):
                for l1 in np.arange(L):
                    I_1_temp  = torch.fft.ifftn(
                        data_f * filters_set[j1, l1],
                        dim=(-2,-1),
                    ).abs()**pseudo_coef
                    S_1[j1, l1] = I_1_temp.mean((-2,-1))

                    I_1_temp_f = torch.fft.fftn(I_1_temp, dim=(-2,-1))
                    for j2 in np.arange(J):
                        if eval(j1j2_criteria):
                            for l2 in np.arange(L):
                                I_2_temp = torch.fft.ifftn(
                                    I_1_temp_f * filters_set[j2,l2], 
                                    dim=(-2,-1),
                                ).abs()**pseudo_coef
                                S_2[j1,l1,j2,l2] = I_2_temp.mean((-2,-1))
        
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
        
        if algorithm == 'fast_2loop':
            for j1 in np.arange(J):
                if j1>=1:
                    data_f_small = self.cut_high_k_off(data_f, j1)
                    wavelet_f = self.cut_high_k_off(self.filters_set[j1], j1)
                else:
                    data_f_small = data_f
                    wavelet_f = self.filters_set[j1]
                _, M1, N1 = wavelet_f.shape
                
                for l1 in np.arange(L):
                    I_1_temp  = torch.fft.ifftn(
                        data_f_small * wavelet_f[l1],
                        dim=(-2,-1),
                    ).abs()**pseudo_coef
                    S_1[j1,l1] = I_1_temp.mean((-2,-1))* M1*N1/M/N
                
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
                            
                            for l2 in np.arange(L):
                                I_2_temp = torch.fft.ifftn(
                                    I_1_temp_f_small * wavelet_f2[l2], 
                                    dim=(-2,-1),
                                ).abs()**pseudo_coef
                                S_2[j1,l1,j2,l2] = I_2_temp.mean((-2,-1)) * M2*N2/M/N
        
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

    def get_numerical_factors(self, L):
        ##### Constant used to compute the filter bank
        xi0 = 1.7 * np.pi
        sigma = 0.248 * np.power(2, -0.55) * xi0
        c = 1 / (1.29) * 2 ** (L / 2 - 1) * math.factorial(L / 2 - 1) / np.sqrt(L / 2 * math.factorial(L - 2))

        # In order to recover Sixin's wavelet, I need to divide hat_phi by this discrepency factor
        discrepency_factor = 1.157853617690941

        return xi0, sigma, c, discrepency_factor

    def compute_hat_psi(self, N, L, pulsation_2d, theta, delta_n, delta_theta_n, c, xi0):
        delta_n_x = delta_n * np.cos(theta-delta_theta_n)
        delta_n_y = delta_n * np.sin(theta-delta_theta_n)
        hatpsi = c * np.exp(-np.power(np.abs(pulsation_2d) - xi0, 2) / (xi0**2 - (np.abs(pulsation_2d) - xi0)**2))
        hatpsi = np.nan_to_num(hatpsi)
        hatpsi = hatpsi * (np.absolute(pulsation_2d) <= 2*xi0).astype(int)
        hatpsi = hatpsi * np.power(np.cos(np.angle(pulsation_2d) - theta), L-1)
        hatpsi = hatpsi * (
            (((np.angle(pulsation_2d) - theta) % (2*np.pi)) <= (np.pi / 2.)).astype(int)
            +
            (((np.angle(pulsation_2d) - theta) % (2*np.pi)) >= (3*np.pi / 2.)).astype(int)
        )

        hatpsi = hatpsi*np.exp(- 1j*(np.real(pulsation_2d)*delta_n_x + np.imag(pulsation_2d)*delta_n_y))

        hatpsi[N // 2: N, N // 2: 3 * N // 2] += hatpsi[3 * N // 2:, N // 2: 3 * N // 2]
        hatpsi[N: 3*N//2, N // 2: 3 * N // 2] += hatpsi[:N//2, N // 2: 3 * N // 2]

        hatpsi[N // 2: 3 * N // 2, N // 2: N] += hatpsi[N // 2: 3 * N // 2, 3 * N // 2:]
        hatpsi[N // 2: 3 * N // 2, N: 3 * N // 2] += hatpsi[N // 2: 3 * N // 2, :N // 2]

        hatpsi[N: 3 * N // 2, N:3 * N // 2] += hatpsi[0:N // 2, :N // 2]
        hatpsi[N // 2: N, N // 2:N] += hatpsi[3 * N // 2:, 3 * N // 2:]

        hatpsi[N: 3*N//2, N // 2:N] += hatpsi[:N // 2, 3 * N // 2:]
        hatpsi[N // 2:N, N: 3 * N // 2] += hatpsi[3 * N // 2:, :N // 2]

        return np.fft.ifftshift(hatpsi[N // 2: 3 * N // 2, N // 2: 3 * N // 2])

    def compute_hat_psi_j_theta_delta_n(self, j, l, N, L, delta_n, delta_theta_n, c, xi0):
        frequencies_x = np.arange(-1, 1, 1/(N))
        frequencies_y = np.arange(-1, 1, 1/(N))
        pulsation_2d = (2**j) * 2 * np.pi * np.array([frequencies_x + 1j * frequency_y for frequency_y in frequencies_y])

        return compute_hat_psi(N, L, pulsation_2d, np.pi*l/L, delta_n, delta_theta_n, c, xi0)

    def compute_bank_of_wavelet(self, delta_theta_n, N, L, J, max_delta_n):
        xi0, sigma, c, discrepency_factor = self.get_numerical_factors(L)
        list_hat_psi = []
        for l in range(2*L):
            print("l = {}".format(l))
            list_hat_psi_l = []
            for j in range(1, J+1):
                list_hat_psi_j = []
                for delta_n in range(max_delta_n+1):
                    delta_theta_n_values = [0] if delta_n==0 else delta_theta_n
                    for delta_theta_n_value in delta_theta_n_values:
                        psi_hat = compute_hat_psi_j_theta_delta_n(j, l, N, L, 3*delta_n/2, delta_theta_n_value, c, xi0) / discrepency_factor

                        list_hat_psi_j.append(psi_hat)
                list_hat_psi_l.append(np.array(list_hat_psi_j))
            list_hat_psi.append(np.array(list_hat_psi_l))

        hat_phi = compute_hat_phi_j(J-2, N, sigma)

        result = {
            "filt_fftpsi": np.array(list_hat_psi),
            "filt_fftphi": hat_phi
        }
        filename = 'bump_steerable_wavelet_N_' + str(N) + '_J_' + str(J) + '_L' + str(L) + '_dn' + str(max_delta_n) + '.npy'
        np.save(os.path.join('bump_steerable_wavelet', 'filters', filename), result)


    def create_bank_scaling_functions(N, J, L):
        _, sigma, _, _ = get_numerical_factors(L)
        list_hatphi = []
        for j in range(2, J-1):
            fftphi = compute_hat_phi_j(j, N, sigma)
            list_hatphi.append(fftphi)

        np.save(os.path.join('bump_steerable_wavelet', 'filters', 'bump_scaling_functions_N_{N}_J_{J}.npy'.format(N=N, J=J)), np.array(list_hatphi))


