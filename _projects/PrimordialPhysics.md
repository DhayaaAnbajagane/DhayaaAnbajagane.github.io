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
  - title: Forecast paper
    url: ''
sitemap: false
---

There is much about the primordial Universe that is in active interest within the cosmology community. Many of the questions are traditional particle physics ones --- what particles existed in this epoch, what were their properties, how did they interact with each other, etc. I work on answering these questions with late-time probes like weak lensing, galaxy clusters, tSZ etc. These cosmological probes are already quite mature, so the challenge is primarily a modelling one --- simulations are required to study such primordial physics with these probes. These signatures are broadly referred to as Primordial Non-Gaussianities (PNGs) and their amplitude is generally represented, at leading order, by $$f_{\rm NL}$$.


### Extending $$f_{\rm NL}$$ to weak lensing


In [Anbajagane+ 2024](https://arxiv.org/abs/2310.02349), I performed one of the first detailed analyses on how much information about $$f_{\rm NL}$$ is contained in the weak lensing field. While the canonical view is that the signatures of primordial physics are often washed out on smaller scales as the formation of collapses structures becomes more prominent, it turns out you can use gravity as a "amplifier" to grow the signatures from early times into larger signatures at late time! Lensing is in fact a very complementary approach to existing probes and can increase the model space we can constrain.

![](/assets/img/projects/PNGSingleFieldconstraints.jpg){:.lead style="width:100%;height:auto;display:block;margin:0 auto"}

*[Figure 4 in Anbajagane+ 2024](https://arxiv.org/abs/2310.02349) Potential constraints on inflation from current and upcoming lensing surveys, in comparison to those from galaxy clustering from existing and upcoming spectroscopic surveys. This paper was published in 2023 and so could only use the forecast of D'Amico++ for what DESI would achieve. The actual constraints will likely be a at least a bit better than what was thought previously (DESI data-taking is going amazing!).*
{:.figcaption}


### Bringing the Cosmological Collider into the Nonlinear Universe

There are only a handful of studies about constrainig $$f_{\rm NL}$$ with nonlinear structure. There are even fewer studies that look at the available range of theoretical models that can cause PNGs. Almost all studies of PNGs in simulations are limited to about five models. In [Anbajagane & Lee 2025a]() and [Anbajagane & Lee 2025b]() we resolved this limitation by introducing a novel simulation framework that can accurately simulate signatures of various phenomenon. One particular class of models, called cosmological colliders, can connect the PNG signatures back to the presence of massive particles in the early Universe and to the properties of these particles (masses, spins, etc.). My work in the above papers details, for the first time, the response of nonlinear structure formation to these primordial signatures. 

![](/assets/img/projects/ColliderTemplates.jpg){:.lead style="width:100%;height:auto;display:block;margin:0 auto"}


*[Figure 2 in Anbajagane & Lee 2025](). An example of thirty templates that have been included in N-body simulations for the first time. This required solutions to a few technical challenges that have now been solved, with resolutions implemented and provided in my public `Aarambam` codebase (see [codes](/code.md)).*
{:.figcaption}