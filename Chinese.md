---
layout: default
---

<!--
<img src="https://github.com/SihaoCheng/SihaoCheng.github.io/blob/master/portrait.png?raw=true" width="250" />
<!-- <img src="https://github.com/SihaoCheng/SihaoCheng.github.io/blob/master/IMG_0039.jpg?raw=true" width="400" /> -->
<a href="https://www.bilibili.com/video/BV19L4y1z7hn/?vd_source=5d944598d960afc958b9b557fb1b5bb4"><img src="https://github.com/SihaoCheng/SihaoCheng.github.io/blob/master/miaomiao.png?raw=true" width="215" /></a>

我是程思浩，现在在普林斯顿高等研究院([IAS](https://www.ias.edu))做天体物理博士后研究. 之前我在[北京大学](http://astro.pku.edu.cn/)本科毕业，然后在约翰霍普金斯大学([JHU](https://physics-astronomy.jhu.edu))获得博士学位并在巴黎高师([ENS](https://csd.ens.psl.eu/))访问一年。我在成为专业天文学家之前是一名天文爱好者。
<!--我对物理、数学、哲学、古典音乐、剑道、动漫都很感兴趣。-->

<h1 id="Research">研究</h1>

===========================

我用统计方法分析巡天数据，并研究其中的天体物理问题。我的研究兴趣涉及宇宙学、恒星物理、动力学、(系外)行星。

我过去的工作成果包括：

1. 展现了一种受神经网络启发而设计的统计量在宇宙学中的应用前景
2. 发现了一类古怪的恒星，它们内部正在结晶并且依靠引力能发光
3. 得到了最精确的双白矮星合并频率的测量
4. 发现了一颗“木星候选体“，为研究大质量恒星旁的行星开启了新窗口
5. 在太阳系中发现了一个古怪的矮行星候选体，有可能挑战第九行星的假说
<br>

我现在正在进行的工作包括：

6. 用新方法绘制第一幅银河系相空间的清晰且平整的[**地图**](https://sihaocheng.github.io/phase_space.html)
7. 搜索太阳系内可能存在的未知行星（第九行星/行星X）
<br>

<a href="https://sihaocheng.github.io/phase_space.html"><img src="https://github.com/SihaoCheng/SihaoCheng.github.io/blob/master/guiding_center.png?raw=true" width="400" />


## 太阳系最远的矮行星
在寻找[第九行星/行星X](https://en.wikipedia.org/wiki/Planet_Nine)时，我偶然发现了一个[轨道古怪的遥远天体](https://www.ias.edu/news/extreme-cousin-pluto-possible-dwarf-planet-discovered-solar-systems-edge), 小行星中心的临时编号是[2017 OF201](https://en.wikipedia.org/wiki/2017_OF201)。由于足够大，它大概率可以满足[**矮行星**](https://en.wikipedia.org/wiki/Dwarf_planet)的标准，同时他的轨道延伸到**非常远**，很可能来自太阳系中神秘的[奥尔特云](https://en.wikipedia.org/wiki/Hills_cloud)区域。它的轨道参数还对第九行星的假说造成了挑战。这里是[学术文章](https://ui.adsabs.harvard.edu/abs/2025arXiv250515806C/abstract)和一些报道：[高等研究院](https://www.ias.edu/news/extreme-cousin-pluto-possible-dwarf-planet-discovered-solar-systems-edge)，[普林斯顿大学](https://web.astro.princeton.edu/news/princeton-astronomers-discover-extraordinary-distant-object-solar-systems-edge)，[媒体](https://www.ias.edu/news/featured-story/304516).


<img src="https://github.com/SihaoCheng/SihaoCheng.github.io/blob/master/tno2.png?raw=true" width="500" />
<img src="https://github.com/SihaoCheng/SihaoCheng.github.io/blob/master/tno.png?raw=true" width="500" />


## 大质量恒星身旁也有行星吗?
<a href="https://ui.adsabs.harvard.edu/abs/2024arXiv240803985C/abstract"><img src="https://github.com/SihaoCheng/SihaoCheng.github.io/blob/master/WDPL.png?raw=true" width="300" /></a>
<br>

传统方法很难发现大质量恒星旁的行星，因此，尽管人们已经发现了超过5000颗系外行星，却几乎没有一例在大质量恒星系统中。不过，大质量恒星“死去”后会演化成白矮星，在这样的系统中发现行星就容易很多了。我在斯皮策太空望远镜的数据库中找到一颗4倍木星质量的[行星候选体](https://ui.adsabs.harvard.edu/abs/2024arXiv240803985C/abstract), 并成功申请到了詹姆斯韦伯太空望远镜的[观测时间](https://ui.adsabs.harvard.edu/abs/2024jwst.prop.6410C/abstract)来进行光谱观测。这种新方法为研究大质量恒星旁的行星打开了新的窗口。同时，这种系统很有意思的一点是，其中的行星（类似木星大小）比宿主星还要大很多，因为这些宿主是白矮星（约地球大小）!


## 如何统计地描述一个图片/物理场的形态？
<a href="https://sihaocheng.github.io/scattering_transform"><img src="https://github.com/SihaoCheng/scattering_transform/blob/master/figures/image_generation.png?raw=true" width="580" /></a>
<br>

从星云的照片到星系的网状分布，天文学中常常遇到需要对图像/物理场的结构进行统计的描述。，“散射变换”为这类问题提供了一个新方法。这一新统计量借用了卷积神经网络([CNNs](https://en.wikipedia.org/wiki/Convolutional_neural_network))中的运算和概念，但同时拥有传统统计量的优势，无需调试或训练。它对输入图像反复进行“小波卷积+取绝对值”的操作，最后再对变换后的信号“取平均值”作为统计量。我首先将它应用在宇宙学中，分析了由[宇宙物质不均匀分布](https://en.wikipedia.org/wiki/Observable_universe#Large-scale_structure)造成的[弱引力透镜](https://en.wikipedia.org/wiki/Weak_gravitational_lensing)效应。我发现它包含的宇宙学信息远高于传统统计量（如相关函数）而与卷积神经网络相近([[1]](https://ui.adsabs.harvard.edu/abs/2020MNRAS.499.5902C/abstract), [[2]](https://ui.adsabs.harvard.edu/abs/2021MNRAS.507.1012C/abstract), [[3]](https://arxiv.org/abs/2112.01288))。我在文章中还仔细讨论了[**如何直观理解这一新统计量**](https://arxiv.org/abs/2112.01288)。我的文章[获得了国际天文统计奖](http://iaa.mi.oa-brera.inaf.it/IAA/awards.html)。我相信它在天体物理以及其他科学数据的处理中将会有广泛的应用。

为了方便更多人使用，我写了一个python模块[`ST.py`](https://github.com/SihaoCheng/scattering_transform)，可供自由下载使用。
<br>
<a><img src="https://pages.jh.edu/~scheng40/ScatteringTransform/images/STvsPowerSpectrum.png" width="300" /></a>
<a><img src="https://pages.jh.edu/~scheng40/ScatteringTransform/images/CosmologicalConstraint.png" width="285" /></a>
<br>

## Gaia数据中的新发现
去年我主要在研究[白矮星](https://en.wikipedia.org/wiki/White_dwarf)。白矮星是宇宙中大多数恒星的最终归宿。我用“盖亚”（[_Gaia_](https://www.cosmos.esa.int/web/gaia/home)）巡天卫星的数据发现（1）一些白矮星有异常慢的冷却速度；（2）有些大质量白矮星是两颗小白矮星融合的产物（点击下图可以查看文章）。这一工作还被天文博客[astrobites](https://astrobites.org/2019/11/12/the-slowly-cooling-white-dwarfs-who-say-ne/)和[AAS Nova](https://aasnova.org/2019/11/19/the-slowly-cooling-white-dwarfs-who-say-ne/)报道.
<br>
<a href="https://sihaocheng.github.io/Qbranch/"><img src="https://pages.jh.edu/~scheng40/Qbranch/images/WD_HR.png" width="315" /></a>
<a href="https://sihaocheng.github.io/DWDmerger"><img src="https://pages.jh.edu/~scheng40/DWDmerger/images/merger_rate1.png" width="300" /></a>

我还写了一个python小工具[`WD_models`](https://github.com/SihaoCheng/WD_models)，用来转换白矮星的测光数据和物理参数。

## 流星光谱
在高中，我和弟弟程思淼找到了一个用数码相机拍摄[流星](https://en.wikipedia.org/wiki/Meteoroid#Meteors)[光谱](https://en.wikipedia.org/wiki/Spectrum)的方法. 我们设计了一个[棱镜](https://en.wikipedia.org/wiki/Prism)装置接在相机镜头前，联系工厂订做了若干件并卖给了其他天文爱好者。下图是我们2010年冬天拍摄的[双子座流星](https://en.wikipedia.org/wiki/Geminids)的光谱。2021年我们重新优化并做了一批新棱镜，价格在1000元人民币左右。如果您感兴趣请联系我们！
<br>
<a href="https://ui.adsabs.harvard.edu/abs/2011JIMO...39...39C/abstract"><img src="https://sihaocheng.github.io/GEM.jpg" width="400" /></a>


# 学习/工作经历
## [普林斯顿高等研究院](https://www.ias.edu/sns/astrophysics)
自然科学学院
<br>
2022-现在, 博士后研究员
<br>
<img src="https://github.com/SihaoCheng/SihaoCheng.github.io/blob/master/campus1020.jpg?raw=true" width="400" />

## [圆周研究所](https://perimeterinstitute.ca/)
2022-现在, 访问研究员
<br>
<img src="https://github.com/SihaoCheng/SihaoCheng.github.io/blob/master/PI.jpg?raw=true" width="400" />

## [巴黎高师](https://csd.ens.psl.eu)
数据科学中心
<br>
2021-2022, 访问研究员
<br>
导师: Prof. [Brice Ménard](https://physics-astronomy.jhu.edu/directory/brice-menard/), Prof. [Stéphane Mallat](https://www.di.ens.fr/~mallat/mallat.html)
<br>
<a href="https://csd.ens.psl.eu/"><img src="https://sihaocheng.github.io/ens-snow-5a969.jpg" width="400" /></a>


## [约翰霍普金斯大学](https://physics-astronomy.jhu.edu/)
物理与天文学系
<br>
2021-2022, 博士后研究员
<br>
2019-2021, 获博士学位
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

<!-- **Cheng, S.**, [Yavetz, T.](https://www.ias.edu/scholars/tomer-yavetz), __, in prep. -->

**Cheng, S.**, [Jiaxuan Li](https://www.jiaxuanli.me/), & [Eritas Yang](https://web.astro.princeton.edu/people/eritas-yang), _Discovery of a dwarf planet candidate in an extremely wide orbit: 2017 OF201_, 2025, [arxiv:2505.15806](https://arxiv.org/abs/2505.15806)

**Cheng, S.**, [Schlaufman, K. C.](http://www.kevinschlaufman.com), & [Caiazzo, I.](https://ilariacaiazzo.com), _A Candidate Giant Planet Companion to the Massive, Young White Dwarf GALEX J071816.4+373139 Informs the Occurrence of Giant Planets Orbiting B Stars_, 2024, [arxiv:2408.03985](https://ui.adsabs.harvard.edu/abs/2024arXiv240803985C/abstract)

**Cheng, S.**, et al., _Cosmological constraints from weak lensing scattering transform using HSC Y1 data_, 2025, [JCAP, 01, 006](https://ui.adsabs.harvard.edu/abs/2025JCAP...01..006C/abstract)

**Cheng, S.**, [Morel, R.](https://www.di.ens.fr/rudy.morel/), [Allys, E.](http://www.lra.ens.fr/~allys/index.html), [Ménard, B.](https://physics-astronomy.jhu.edu/directory/brice-menard/) & [Mallat, S.](https://www.di.ens.fr/~mallat/), _Scattering Spectra for Physics_, 2024, [PNAS Nexus](https://academic.oup.com/pnasnexus/article/3/4/pgae103/7623818)

**Cheng, S.** & [Ménard, B.](https://physics-astronomy.jhu.edu/directory/brice-menard/), _How to quantify fields and textures? A guide to the scattering transoform_, 2021, [arXiv:2112.01288](https://arxiv.org/abs/2112.01288)

<!-- **Cheng, S.**, _Cosmology and Astrophysics with the Scattering Transform_, 2021, [Ph.D. Thesis at Johns Hopkins University](https://pages.jh.edu/scheng40/Dissertation_SihaoCheng.pdf) -->

**Cheng, S.** & [Ménard, B.](https://physics-astronomy.jhu.edu/directory/brice-menard/), _Weak lensing scattering transform: dark energy and neutrino mass sensitivity_, 2021, [MNRAS, 507, 1012](https://ui.adsabs.harvard.edu/abs/2021MNRAS.507.1012C/abstract)

**Cheng, S.**, [Ting, Y.-S.](https://www.mso.anu.edu.au/~yting/), [Ménard, B.](https://physics-astronomy.jhu.edu/directory/brice-menard/), & [Bruna, J.](https://cims.nyu.edu/~bruna/), _A new approach to observational cosmology using the scattering transform_, 2020, [MNRAS, 499, 5902](https://ui.adsabs.harvard.edu/abs/2020MNRAS.499.5902C/abstract)

**Cheng, S.**, [Cummings, J. D.](https://pages.jh.edu/~jcummi19/), [Ménard, B.](https://physics-astronomy.jhu.edu/directory/brice-menard/), & [Toonen, S.](http://www.sr.bham.ac.uk/~toonen/), _Double White Dwarf Merger Products among High-mass White Dwarfs_, 2020, [ApJ, 891, 160](https://ui.adsabs.harvard.edu/abs/2020ApJ...891..160C/abstract)

**Cheng, S.**, _Two delays in white dwarf evolution revealed by Gaia_, 2019, [Proceedings of IAU, 15(S357), 175](https://ui.adsabs.harvard.edu/abs/2020arXiv200104483C/abstract)

**Cheng, S.**, [Cummings, J. D.](https://pages.jh.edu/~jcummi19/), [Ménard, B.](https://physics-astronomy.jhu.edu/directory/brice-menard/), _A Cooling Anomaly of High-mass White Dwarfs_, 2019, [ApJ, 886, 100](https://ui.adsabs.harvard.edu/abs/2019ApJ...886..100C/abstract)

**Cheng, S.**, [Cheng, S.](https://www.researchgate.net/profile/Simiao-Cheng-2), _Meteor spectral observation with DSLR, normal lens and prism_, 2011, [JIMO, 39, 39](https://ui.adsabs.harvard.edu/abs/2011JIMO...39...39C/abstract)


## 重要:

[Bédard, A.](https://warwick.ac.uk/fac/sci/physics/research/astro/people/antoinebedard/), [Blouin, S.](https://www.sblouin.com/), **Cheng, S.**, _Buoyant crystals halt the cooling of white dwarf stars_, 2024, [Nature](https://www.nature.com/articles/s41586-024-07102-y), [(free access link)](https://www.nature.com/articles/s41586-024-07102-y.epdf?sharing_token=6Fo5MeeV6DtHr_ZPzpQPF9RgN0jAjWel9jnR3ZoTv0MUbqXY_GqhdRlxZyDGYY3HSZnFjlZb7aRNzmzancdDVzw-jIFvz6nvI2ifzDYliW4czTow3X_VpRLXsPep6FI_Ha2iFL7JG6e7Abx9Mag-sS0_HCdjjKprVvb7Dzl3_VY%3D)

[Chandra, V.](https://vedantchandra.com/), [Hwang, H.-C.](http://www.hwang-astro.me), [Zakamska, N. L.](https://zakamska.johnshopkins.edu), **Cheng, S.**, _A Gravitational Redshift Measurement of the White Dwarf Mass–Radius Relation_, 2020, [ApJ, 899, 146](https://ui.adsabs.harvard.edu/abs/2020ApJ...899..146C/abstract)

[Lu, C. X.](http://www.ciceroxlu.org), [Schlaufman, K. C.](http://www.kevinschlaufman.com), **Cheng, S.**, _An Increase in Small-planet Occurrence with Metallicity for Late-type Dwarf Stars in the Kepler Field and Its Implications for Planet Formation_, 2020, [AJ, 160, 253](https://ui.adsabs.harvard.edu/abs/2020AJ....160..253L/abstract)



## 其他: 

Novaes, C., **et al.**, _Cosmology from HSC Y1 Weak Lensing with Combined Higher-Order Statistics and Simulation-based Inference_, 2025, [PRD, 111, 083510](https://ui.adsabs.harvard.edu/abs/2025PhRvD.111h3510N/abstract)

[Grandón, D.](https://www.universiteitleiden.nl/en/staffmembers/daniela-grandon-silva#tab-1) **et al.**, _Impact of baryonic feedback on HSC Y1 weak lensing non-Gaussian statistics_, 2024, [PRD, 110, 103539](https://ui.adsabs.harvard.edu/abs/2024PhRvD.110j3539G/abstract)  

Liu, G., **et al.**, _A new code for low-resolution spectral identification of white dwarf binary candidates_, 2024, [A&A, 690, A29](https://ui.adsabs.harvard.edu/abs/2024A%26A...690A..29L/abstract)

[Hwang, H.-C.](http://www.hwang-astro.me), [Ting, Y.-S.](https://www.mso.anu.edu.au/~yting/), **Cheng, S.**, [Speagle, J](https://joshspeagle.com), _Dynamical masses across the Hertzsprung-Russell diagram_, 2024, [MNRAS, 528, 4272](https://ui.adsabs.harvard.edu/abs/2024MNRAS.528.4272H/abstract)

[Marques, G. A.](https://kavlicosmo.uchicago.edu/people/profile/gabriela-a-marques/) **et al.**, _Cosmology from weak lensing peaks and minima with Subaru Hyper Suprime-Cam survey first-year data_, 2023, [MNRAS, 528, 4513](https://ui.adsabs.harvard.edu/abs/2024MNRAS.528.4513M/abstract)

Ren, L., **et al.**, _A Systematic Search for Short-period Close White Dwarf Binary Candidates Based on Gaia EDR3 Catalog and Zwicky Transient Facility Data_, 2023, [ApJS, 264, 39](https://ui.adsabs.harvard.edu/abs/2023ApJS..264...39R/abstract)

Euclid Collaboration, **et al.**, _Euclid preparation-XXVIII. Forecasts for ten different higher-order weak lensing statistics_, 2023, [A&A, 675, A120](https://ui.adsabs.harvard.edu/abs/2023A%26A...675A.120E/abstract)

Liu, D. Z., **et al.**, _Potential scientific synergies in weak lensing studies between the CSST and Euclid space probes_, 2023, [A&A, 669, A128](https://ui.adsabs.harvard.edu/abs/2023A%26A...669A.128L/abstract)

[Camisassa, M.](http://evolgroup.fcaglp.unlp.edu.ar/camisassa.html), **et al.**, _Forever young white dwarfs: when stellar ageing stops_, 2021, [A&A Letters, 649, 7](https://ui.adsabs.harvard.edu/abs/2021A%26A...649L...7C/abstract)

[Bauer, E. B.](https://scholar.google.com/citations?user=GzWCQFgAAAAJ&hl=en), [Schwab, J.](https://yoshiyahu.org), [Bildsten, L.](https://www.kitp.ucsb.edu/bildsten), and **Cheng, S.**, _Multi-Gigayear White Dwarf Cooling Delays from Clustering-Enhanced Gravitational Sedimentation_, 2020, [ApJ, 902, 93](https://ui.adsabs.harvard.edu/abs/2020ApJ...902...93B/abstract)

[Marigo, P.](http://www.astro.unipd.it/marigo/index.html), [Cummings, J. D.](https://pages.jh.edu/~jcummi19/), **et al.**, _Carbon star formation as seen through the non-monotonic initial–final mass relation_, 2020, [Nature Astronomy](https://doi.org/10.1038/s41550-020-1132-1), [full text here](https://rdcu.be/b5r2A)

<h1 id="Contacts">联系方式</h1>
scheng@ias.edu
<br>
+1 443 207 1532
<br>
Bloomberg Hall 150
<br>
1 Einstein Dr, Institute for Advanced Study
<br>
Princeton, NJ08540, USA


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

-->
