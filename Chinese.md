---
layout: default
---

<img src="https://github.com/SihaoCheng/SihaoCheng.github.io/blob/master/IMG_0039.jpg?raw=true" width="400" />

我是程思浩，现在在普林斯顿高等研究院([IAS](https://www.ias.edu))做天体物理博士后研究. 我对物理、数学、哲学、古典音乐、剑道、动漫都很感兴趣。

<h1 id="Research">研究</h1>
我用统计方法分析巡天数据，并研究其中的天体物理问题。我的研究兴趣涉及宇宙学、恒星物理、系外行星。我过去的工作包括发现了一类靠引力发光的特殊星体，以及将一种受神经网络启发而设计的新统计量应用到宇宙学中。 

## 如何统计地描述一个图片/物理场的形态？

从星云的照片到星系的网状分布，天文学中常常遇到需要对图像/物理场的结构进行统计的描述。，“散射变换”为这类问题提供了一个新方法。这一新统计量借用了卷积神经网络中的运算和概念，但同时拥有传统统计量的优势，无需调试或训练。它对输入图像反复进行“小波卷积+取绝对值”的操作，最后再对变换后的信号“取平均值”作为统计量。我首先将它应用在宇宙学中，分析了由[宇宙物质不均匀分布](https://en.wikipedia.org/wiki/Observable_universe#Large-scale_structure)造成的[弱引力透镜](https://en.wikipedia.org/wiki/Weak_gravitational_lensing)效应。我发现它包含的宇宙学信息远高于传统统计量（如相关函数）而与卷积神经网络相近([1], [2], [3])。我在文章中还仔细讨论了如何直观理解这一新统计量。我相信它在天体物理以及其他科学数据的处理中将会有广泛的应用。

为了方便更多人使用，我写了一个python模块ST.py，可供自由下载使用。
To advocate the use of the scattering transform, I also wrote a publicly available module ST.py based on pytorch, which can implement 1D and 2D scattering transform in a fast and transparent way. 

<a href="https://arxiv.org/abs/2006.08561"><img src="https://pages.jh.edu/~scheng40/ScatteringTransform/images/STvsPowerSpectrum.png" width="330" /></a>
<a href="https://arxiv.org/abs/2006.08561"><img src="https://pages.jh.edu/~scheng40/ScatteringTransform/images/CosmologicalConstraint.png" width="285" /></a>





## Gaia数据中的新发现
去年我主要在研究[白矮星](https://en.wikipedia.org/wiki/White_dwarf)。白矮星是宇宙中大多数恒星的最终归宿。我用“盖亚”（[_Gaia_](https://www.cosmos.esa.int/web/gaia/home)）巡天卫星的数据发现（1）一些白矮星有异常慢的冷却速度；（2）有些大质量白矮星是两颗小白矮星融合的产物（点击下图可以查看文章）。这一工作还被天文博客[astrobites](https://astrobites.org/2019/11/12/the-slowly-cooling-white-dwarfs-who-say-ne/)和[AAS Nova](https://aasnova.org/2019/11/19/the-slowly-cooling-white-dwarfs-who-say-ne/)报道.
<br>
<a href="https://sihaocheng.github.io/Qbranch/"><img src="https://pages.jh.edu/~scheng40/Qbranch/images/WD_HR.png" width="315" /></a>
<a href="https://sihaocheng.github.io/DWDmerger"><img src="https://pages.jh.edu/~scheng40/DWDmerger/images/merger_rate1.png" width="300" /></a>

我还写了一个python小工具[`WD_models`](https://github.com/SihaoCheng/WD_models)，用来转换白矮星的测光数据和物理参数。

## 流星光谱
在高中，我和弟弟程思淼找到了一个用数码相机拍摄[流星](https://en.wikipedia.org/wiki/Meteoroid#Meteors)[光谱](https://en.wikipedia.org/wiki/Spectrum)的方法. 我们设计了一个[棱镜](https://en.wikipedia.org/wiki/Prism)装置接在相机镜头前，联系工厂订做了若干件并卖给了其他天文爱好者（主要为了减低单价，最后控制在六七百元左右）。下图是我们2010年冬天拍摄的[双子座流星](https://en.wikipedia.org/wiki/Geminids)的光谱。我们正在准备做一批新棱镜。如果您感兴趣请联系我们！
<br>
<a href="https://ui.adsabs.harvard.edu/abs/2011JIMO...39...39C/abstract"><img src="https://sihaocheng.github.io/GEM.jpg" width="400" /></a>


# 学习经历
## [约翰霍普金斯大学](https://physics-astronomy.jhu.edu/)
物理与天文学系
<br>
2019-现在, 博士候选人
<br>
2017-2019, 获硕士学位
<br>
导师: Prof. [Brice Ménard](https://physics-astronomy.jhu.edu/directory/brice-menard/)
<br>
<a href="https://physics-astronomy.jhu.edu/"><img src="https://pages.jh.edu/~scheng40/images/JHU.jpg" width="400" /></a>

## [北京大学](http://astro.pku.edu.cn/)
天文学系
<br>
2012-2016, 获学士学位
<br>
导师: Prof. [Eric Peng (彭逸西)](http://kiaa.pku.edu.cn/info/1011/2660.htm)
<br>
<a href="http://astro.pku.edu.cn/"><img src="https://pages.jh.edu/~scheng40/images/PKU.png" width="400" /></a>

# 发表文章

## 第一作者文章：

**Cheng, S.**, [Ting, Y.-S.](https://www.sns.ias.edu/~ting/), [Ménard, B.](https://physics-astronomy.jhu.edu/directory/brice-menard/), & [Bruna, J.](https://cims.nyu.edu/~bruna/), _A new approach to observational cosmology using the scattering transform_, 2020, [MNRAS, 499, 5902](https://ui.adsabs.harvard.edu/abs/2020MNRAS.499.5902C/abstract)

**Cheng, S.**, [Cummings, J. D.](https://pages.jh.edu/~jcummi19/), Ménard, B., & [Toonen, S.](http://www.sr.bham.ac.uk/~toonen/), _Double White Dwarf Merger Products among High-mass White Dwarfs_, 2020, [ApJ, 891, 160](https://ui.adsabs.harvard.edu/abs/2020ApJ...891..160C/abstract)

**Cheng, S.**, _Two delays in white dwarf evolution revealed by Gaia_, 2019, [Proceedings of IAU, 15(S357), 175](https://ui.adsabs.harvard.edu/abs/2020IAUS..357..175C/abstract)

**Cheng, S.**, Cummings, J. D., Ménard, B., _A Cooling Anomaly of High-mass White Dwarfs_, 2019, [ApJ, 886, 100](https://ui.adsabs.harvard.edu/abs/2019ApJ...886..100C/abstract)

**Cheng, S.**, Cheng, S., _Meteor spectral observation with DSLR, normal lens and prism_, 2011, [JIMO, 39, 39](https://ui.adsabs.harvard.edu/abs/2011JIMO...39...39C/abstract)

## 其他: 

[Lu, C. X.](http://www.ciceroxlu.org), [Schlaufman, K. C.](http://www.kevinschlaufman.com), **Cheng, S.**, _An Increase in Small-planet Occurrence with Metallicity for Late-type Dwarf Stars in the Kepler Field and Its Implications for Planet Formation_, 2020, [AJ, 160, 253](https://ui.adsabs.harvard.edu/abs/2020AJ....160..253L/abstract)

[Bauer, E. B.](https://scholar.google.com/citations?user=GzWCQFgAAAAJ&hl=en), [Schwab, J.](https://yoshiyahu.org), [Bildsten, L.](https://www.kitp.ucsb.edu/bildsten), and **Cheng, S.**, _Multi-Gigayear White Dwarf Cooling Delays from Clustering-Enhanced Gravitational Sedimentation_, 2020, [ApJ, accepted](https://ui.adsabs.harvard.edu/abs/2020arXiv200904025B/abstract)

[Camisassa, M. E.](http://evolgroup.fcaglp.unlp.edu.ar/camisassa.html), Althaus, L. G., Torres, S., Córsico, A. H., **Cheng, S.**, Rebassa-Mansergas, A., _Forever young white dwarfs: when stellar ageing stops_, 2020, [arXiv:2008.03028](https://ui.adsabs.harvard.edu/abs/2020arXiv200803028C/abstract)

[Chandra, V.](https://vedantchandra.com/), [Hwang, H.-C.](http://www.hwang-astro.me), [Zakamska, N. L.](https://zakamska.johnshopkins.edu), **Cheng, S.**, _A Gravitational Redshift Measurement of the White Dwarf Mass–Radius Relation_, 2020, [ApJ, 899, 146](https://ui.adsabs.harvard.edu/abs/2020ApJ...899..146C/abstract)

[Marigo, P.](http://www.astro.unipd.it/marigo/index.html), Cummings, J. D., **et al.**, _Carbon star formation as seen through the non-monotonic initial–final mass relation_, 2020, [Nature Astronomy](https://doi.org/10.1038/s41550-020-1132-1), [full text here](https://rdcu.be/b5r2A)


<h1 id="Contacts">联系方式</h1>
s.cheng@jhu.edu
<br>
+1 443 207 1532
<br>
Bloomberg 506
<br>
3400 N. Charles St., Johns Hopkins University
<br>
Baltimore, MD21218, USA

