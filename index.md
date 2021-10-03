---
layout: default
---

<img src="https://github.com/SihaoCheng/SihaoCheng.github.io/blob/master/IMG_0039.jpg?raw=true" width="400" />

I am a postdoc researcher at the Johns Hopkins Univerisity ([JHU](https://physics-astronomy.jhu.edu)) and now visiting the École Normale Supérieure in Paris ([ENS Paris(https://www.ens.psl.eu/en)]). I just got me Ph.D. in astrophysics this summer at JHU. I love physics, math, philosophy, [classical music](https://sihaocheng.github.io/music), kendo, and anime.
<!-- Recently, I am reading an astonishing book: [*A Logical Journey: From Gödel to Philosophy*](https://mitpress.mit.edu/books/logical-journey). -->

<h1 id="Research">Research</h1>
I am interested in using statistical analysis to understand our Universe. My interests range from observational cosmology to stellar physics and planets. My work led to the discovery of special stars that shine out of gravitational sedimentation and the cosmological applications of a new statistic that borrows ideas from convolutional neural networks.
<br>

## New statistics for cosmology and astrophysics
<!-- <a href="s22.html"><img src="https://github.com/SihaoCheng/SihaoCheng.github.io/blob/master/s22.png?raw=true" width="450" /></a> -->
<a href="https://ui.adsabs.harvard.edu/abs/2021MNRAS.507.1012C/abstract"><img src="https://github.com/SihaoCheng/scattering_transform/blob/master/image_generation.png?raw=true" width="580" /></a>
<br>

Textures and patterns are ubiquitous in astronomical data but challenging to quantify. The [scattering transform](https://arxiv.org/abs/1101.2286) provides a new powerful statistic for these features. It borrows ideas from convolutional neural nets ([CNNs](https://en.wikipedia.org/wiki/Convolutional_neural_network)), but shares advantages of traditional statistics.
In two recent papers ([[1]](https://ui.adsabs.harvard.edu/abs/2020MNRAS.499.5902C/abstract), [[2]](https://ui.adsabs.harvard.edu/abs/2021MNRAS.507.1012C/abstract)), I discussed in depth **how to intuitively understand this new statistic** which is still unfamiliar to most physicists, and I showed that on [weak lensing](https://en.wikipedia.org/wiki/Weak_gravitational_lensing) [mass maps](https://en.wikipedia.org/wiki/Observable_universe#Large-scale_structure) it outperforms classic statistics and is **on a par with CNNs**. The first paper [won an award of astrostatistics](http://iaa.mi.oa-brera.inaf.it/IAA/awards.html) and was reported by [this astrobites blog](https://astrobites.org/2020/07/30/scattering-stat/).

To advocate the use of the scattering transform, I also wrote a publicly available module [`ST.py`](https://github.com/SihaoCheng/scattering_transform) based on pytorch, which can implement 1D and 2D scattering transform in a fast and transparent way.
<br>
<a><img src="https://pages.jh.edu/~scheng40/ScatteringTransform/images/STvsPowerSpectrum.png" width="300" /></a>
<a><img src="https://pages.jh.edu/~scheng40/ScatteringTransform/images/CosmologicalConstraint.png" width="285" /></a>
<br>


## Discoveries about white dwarfs from _Gaia_ satellite
I also work on [white dwarfs](https://en.wikipedia.org/wiki/White_dwarf), the destiny of most stars in the universe. Using data from the [_Gaia_](https://www.cosmos.esa.int/web/gaia/home) space mission, I discovered a new population of white dwarfs that **cool extremely slowly** and some others that are **merger products**. My work has led to two papers (click the figures below), one of which was highlighted by [astrobites](https://astrobites.org/2019/11/12/the-slowly-cooling-white-dwarfs-who-say-ne/) and [AAS Nova](https://aasnova.org/2019/11/19/the-slowly-cooling-white-dwarfs-who-say-ne/) and considered a major discovery in Gaia data.

To make white dwarf research easier, I also built a publically available package [`WD_models`](https://github.com/SihaoCheng/WD_models) in python for transformation between white dwarf photometry and physical properties.
<br>
<a href="https://sihaocheng.github.io/Qbranch/"><img src="https://pages.jh.edu/~scheng40/Qbranch/images/WD_HR.png" width="315" /></a>
<a href="https://sihaocheng.github.io/DWDmerger/"><img src="https://pages.jh.edu/~scheng40/DWDmerger/images/merger_rate1.png" width="300" /></a>
<br>


## Spectra of meteors
In high school, my twin brother (who is studying philosophy now) and I found an efficient way to take [spectra](https://en.wikipedia.org/wiki/Spectrum) of [meteors](https://en.wikipedia.org/wiki/Meteoroid#Meteors) with digital camera. We designed a [prism](https://en.wikipedia.org/wiki/Prism) device that can screw in front of a lens. We ordered several from a factory, and sold them to other amateurs of astronomy. Shown below is one spectrum of the [Geminid meteor shower](https://en.wikipedia.org/wiki/Geminids), taken in 2010. We have made a new batch of such prism devices with a cost of less than 200 dollars each. If you are interested, please contact us or buy it [here](https://www.ebay.com/itm/144142982226)!
<br>
<a href="https://ui.adsabs.harvard.edu/abs/2011JIMO...39...39C/abstract"><img src="https://sihaocheng.github.io/GEM.jpg" width="400" /></a>


# Education
## [Johns Hopkins University](https://physics-astronomy.jhu.edu/)
Department of Physics and Astronomy
<br>
2017-2021(expected), M.A., Ph.D.
<br>
Advisor: Prof. [Brice Ménard](https://physics-astronomy.jhu.edu/directory/brice-menard/)
<br>
<a href="https://physics-astronomy.jhu.edu/"><img src="https://pages.jh.edu/~scheng40/images/JHU.jpg" width="400" /></a>

## [Peking University](http://astro.pku.edu.cn/) ([北京大学](http://astro.pku.edu.cn/))
Department of Astronomy
<br>
2012-2016, B.S.
<br>
Advisor: Prof. [Eric Peng (彭逸西)](http://kiaa.pku.edu.cn/info/1011/2660.htm)
<br>
<a href="http://astro.pku.edu.cn/"><img src="https://pages.jh.edu/~scheng40/images/PKU.png" width="400" /></a>

# Publications

## First author:

**Cheng, S.** & [Ménard, B.](https://physics-astronomy.jhu.edu/directory/brice-menard/), _Weak lensing scattering transform: dark energy and neutrino mass sensitivity_, 2021, [MNRAS, 507, 1012](https://ui.adsabs.harvard.edu/abs/2021MNRAS.507.1012C/abstract)

**Cheng, S.**, [Ting, Y.-S.](https://www.sns.ias.edu/~ting/), [Ménard, B.](https://physics-astronomy.jhu.edu/directory/brice-menard/), & [Bruna, J.](https://cims.nyu.edu/~bruna/), _A new approach to observational cosmology using the scattering transform_, 2020, [MNRAS, 499, 5902](https://ui.adsabs.harvard.edu/abs/2020MNRAS.499.5902C/abstract)

**Cheng, S.**, [Cummings, J. D.](https://pages.jh.edu/~jcummi19/), [Ménard, B.](https://physics-astronomy.jhu.edu/directory/brice-menard/), & [Toonen, S.](http://www.sr.bham.ac.uk/~toonen/), _Double White Dwarf Merger Products among High-mass White Dwarfs_, 2020, [ApJ, 891, 160](https://ui.adsabs.harvard.edu/abs/2020ApJ...891..160C/abstract)

**Cheng, S.**, _Two delays in white dwarf evolution revealed by Gaia_, 2019, [Proceedings of IAU, 15(S357), 175](https://ui.adsabs.harvard.edu/abs/2020arXiv200104483C/abstract)

**Cheng, S.**, [Cummings, J. D.](https://pages.jh.edu/~jcummi19/), [Ménard, B.](https://physics-astronomy.jhu.edu/directory/brice-menard/), _A Cooling Anomaly of High-mass White Dwarfs_, 2019, [ApJ, 886, 100](https://ui.adsabs.harvard.edu/abs/2019ApJ...886..100C/abstract)

**Cheng, S.**, Cheng, S., _Meteor spectral observation with DSLR, normal lens and prism_, 2011, [JIMO, 39, 39](https://ui.adsabs.harvard.edu/abs/2011JIMO...39...39C/abstract)

## Others: 

[Camisassa, M.](http://evolgroup.fcaglp.unlp.edu.ar/camisassa.html), **et al.**, _Forever young white dwarfs: when stellar ageing stops_, 2021, [A&A Letters, 649, 7](https://ui.adsabs.harvard.edu/abs/2021A%26A...649L...7C/abstract)

[Lu, C. X.](http://www.ciceroxlu.org), [Schlaufman, K. C.](http://www.kevinschlaufman.com), **Cheng, S.**, _An Increase in Small-planet Occurrence with Metallicity for Late-type Dwarf Stars in the Kepler Field and Its Implications for Planet Formation_, 2020, [AJ, 160, 253](https://ui.adsabs.harvard.edu/abs/2020AJ....160..253L/abstract)

[Bauer, E. B.](https://scholar.google.com/citations?user=GzWCQFgAAAAJ&hl=en), [Schwab, J.](https://yoshiyahu.org), [Bildsten, L.](https://www.kitp.ucsb.edu/bildsten), and **Cheng, S.**, _Multi-Gigayear White Dwarf Cooling Delays from Clustering-Enhanced Gravitational Sedimentation_, 2020, [ApJ, 902, 93](https://ui.adsabs.harvard.edu/abs/2020ApJ...902...93B/abstract)

[Chandra, V.](https://vedantchandra.com/), [Hwang, H.-C.](http://www.hwang-astro.me), [Zakamska, N. L.](https://zakamska.johnshopkins.edu), **Cheng, S.**, _A Gravitational Redshift Measurement of the White Dwarf Mass–Radius Relation_, 2020, [ApJ, 899, 146](https://ui.adsabs.harvard.edu/abs/2020ApJ...899..146C/abstract)

[Marigo, P.](http://www.astro.unipd.it/marigo/index.html), [Cummings, J. D.](https://pages.jh.edu/~jcummi19/), **et al.**, _Carbon star formation as seen through the non-monotonic initial–final mass relation_, 2020, [Nature Astronomy](https://doi.org/10.1038/s41550-020-1132-1), [full text here](https://rdcu.be/b5r2A)

<h1 id="Contacts">Contacts</h1>
s.cheng@jhu.edu
<br>
+1 443 207 1532
<br>
Bloomberg 506
<br>
3400 N. Charles St., Johns Hopkins University
<br>
Baltimore, MD21218, USA


<h1 id="skymap">Sky Altas (Aladin)</h1>
<!-- you can find more information about this cool embedded sky altas on http://aladin.u-strasbg.fr/AladinLite/doc/#embedding -->
<!-- include Aladin Lite CSS file in the head section of your page -->
<link rel="stylesheet" href="https://aladin.u-strasbg.fr/AladinLite/api/v2/latest/aladin.min.css" />
 
<!-- you can skip the following line if your page already integrates the jQuery library -->
<script type="text/javascript" src="https://code.jquery.com/jquery-1.12.1.min.js" charset="utf-8"></script>
 
<!-- insert this snippet where you want Aladin Lite viewer to appear and after the loading of jQuery -->
<div id="aladin-lite-div" style="width:600px;height:400px;"></div>
<script type="text/javascript" src="https://aladin.u-strasbg.fr/AladinLite/api/v2/latest/aladin.min.js" charset="utf-8"></script>
<script type="text/javascript">
    var aladin = A.aladin('#aladin-lite-div', {survey: "P/DSS2/color", fov:1, target: "20 45 38.000 +30 42 30.00"});
</script>
