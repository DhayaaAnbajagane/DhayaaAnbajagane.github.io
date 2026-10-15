---
layout: project
title: 'Primordial Physics in the Nonlinear Universe'
caption: 'What happened in the first moments after the Big Bang?'
description: ''
date: 23 August 2025
image: 
  path: /assets/img/projects/ColliderTemplates.jpg
links:
  - title: Aarambam
    url: https://github.com/DhayaaAnbajagane/Aarambam
  - title: Ulagam simulations
    url: https://ulagam-simulations.readthedocs.io/
  - title: Forecast paper
    url: https://arxiv.org/abs/2607.06692
  - title: Halo bias paper
    url: https://arxiv.org/abs/2607.24939
sitemap: true
---

There is much about the primordial Universe that is of active interest within the cosmology community. Many of the questions are traditional particle physics ones --- what particles existed in this epoch, what were their properties, how did they interact with each other, etc. I work on answering these questions with late-time probes like weak lensing, galaxy clusters, tSZ etc. These cosmological probes are already quite mature, so the challenge is primarily a modelling one --- simulations are required to study such primordial physics with these probes. These signatures are broadly referred to as Primordial Non-Gaussianities (PNGs) and their amplitude is generally represented, at leading order, by $$f_{\rm NL}$$.


## Extending $$f_{\rm NL}$$ to weak lensing
{:.h3}


In [Anbajagane+ 2024](https://arxiv.org/abs/2310.02349), I performed one of the first detailed analyses on how much information about $$f_{\rm NL}$$ is contained in the weak lensing field. While the canonical view is that the signatures of primordial physics are often washed out on smaller scales as the formation of collapsed structures becomes more prominent, it turns out you can use gravity as an "amplifier" to grow the signatures from early times into larger signatures at late time! Lensing is in fact a very complementary approach to existing probes and can increase the model space we can constrain.

![Forecast constraints on inflation from lensing surveys compared with galaxy clustering surveys](/assets/img/projects/PNGSingleFieldconstraints.jpg){:.lead loading="lazy" decoding="async"}

*[Figure 4 in Anbajagane+ 2024](https://arxiv.org/abs/2310.02349). Potential constraints on inflation from current and upcoming lensing surveys, in comparison to those from galaxy clustering from existing and upcoming spectroscopic surveys. This paper was published in 2023 and so could only use the forecast of D'Amico+ for what DESI would achieve. The actual constraints will likely be at least a bit better than what was thought previously (DESI data-taking is going amazingly!).*
{:.figcaption}


## Bringing the Cosmological Collider into the Nonlinear Universe
{:.h3}

There are only a handful of studies about constraining $$f_{\rm NL}$$ with nonlinear structure. There are even fewer studies that look at the available range of theoretical models that can cause PNGs. Almost all studies of PNGs in simulations are limited to about five models. In [Anbajagane & Lee 2025a](https://arxiv.org/abs/2509.02693) and [Anbajagane & Lee 2025b](https://arxiv.org/abs/2509.02695) we resolved this limitation by introducing a novel simulation framework that can accurately simulate signatures of various phenomena. One particular class of models, called cosmological colliders, can connect the PNG signatures back to the presence of massive particles in the early Universe and to the properties of these particles (masses, spins, etc.). My work in the above papers details, for the first time, the response of nonlinear structure formation to these primordial signatures. In [Anbajagane 2026](https://arxiv.org/abs/2607.06692), I then forecast how well the combination of weak lensing, thermal SZ, and X-ray fields can constrain these primordial signatures, finding a factor of two improvement over using lensing alone.

![Examples of cosmological collider templates included in N-body simulations](/assets/img/projects/ColliderTemplates.jpg){:.lead loading="lazy" decoding="async"}


*[Figure 2 in Anbajagane & Lee 2025a](https://arxiv.org/abs/2509.02693). Examples of the templates that have been included in N-body simulations for the first time. This required solutions to a few technical challenges that have now been solved, with resolutions implemented and provided in my public `Aarambam` codebase (see [codes](/code.md)).*
{:.figcaption}


## Oscillating halo bias from the Cosmological Collider
{:.h3}

Massive particles during inflation leave an oscillatory imprint in the primordial bispectrum, and this imprint carries over to how halos trace the matter field on large scales. In [Anbajagane & Dalal 2026](https://arxiv.org/abs/2607.24939), we made the first simulation measurements of this oscillating, scale-dependent halo bias. The amplitude and phase of the oscillations depend on halo mass (and the phase is even sensitive to assembly bias!), and higher-frequency signals get washed out as they average down within the size of a halo. A simple peak-background-split model captures all of this.

![Oscillating scale-dependent halo bias from simulations and theory for three collider frequencies in two halo mass bins](/assets/img/projects/HaloBiasOscillations.svg){:.lead loading="lazy" decoding="async"}

*[Figure 4 in Anbajagane & Dalal 2026](https://arxiv.org/abs/2607.24939). The scale-dependent halo bias from simulations (points) and theory (dashed lines) for cosmological collider models at three different frequencies, shown for two halo mass bins. The oscillations are measured and predicted accurately in all cases, and their amplitude drops as the frequency increases since the signal averages down within the halo.*
{:.figcaption}

{% include abbreviations.md %}
