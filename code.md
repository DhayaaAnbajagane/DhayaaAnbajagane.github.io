---
layout: page
title: My code
description:
no_groups: true
---

0. 
{:toc}

My research has a heavy computational component, so I write a lot of code! Here are a list of code-bases that I've released to the community.

## [BaryonForge](https://github.com/DhayaaAnbajagane/BaryonForge)

![](/assets/img/code/BaryonForge.png){:.lead style="width:100%;height:auto"}


[`BaryonForge`](https://github.com/DhayaaAnbajagane/BaryonForge) is a pipeline for *Baryonifying* N-body simulations by adding baryon-induced corrections to the density field and/or adding thermodynamic fields such as the gas pressure, temperature etc. The entire modelling pipeline is built out of the Core Cosmology Library (CCL) so the profile classes can also be used with CCL tools to compute analytic, halo model-based predictions for different power spectra. See [Anbajagane+ 2024](https://arxiv.org/abs/2409.03822) for the introduction of the codebase. The method has been validated for lensing measurements in [Zhou+ 2025](https://arxiv.org/abs/2505.07949), and has been used for halo-model calculations (e.g., in [R. S+ 2025](https://arxiv.org/abs/2507.13317)).


## [Aarambam](https://github.com/DhayaaAnbajagane/Aarambam)

![](/assets/img/code/Aarambam.png){:.lead style="width:100%;height:auto;display:block;margin:0 auto"}


[`Aarambam`](https://github.com/DhayaaAnbajagane/Aarambam) is a pipeline for generating non-Gaussian initial conditions for simulations. It provides an end-to-end pipeline for generating the ICs of a N-body simulation given some analytic bispectrum template. The novelty in the codebase is performing a decomposition of arbitrary bispectra into separable functions, and then subsequently generating non-Gaussian initial conditions corresponding to these functions. The output field will contain a three-point correlation consistent with the input bispectra, while ensuring the original two-point correlations are preserved to better than $$0.01\%$$. The methodology is introduced and extensively validated in [Anbajagane & Lee 2025a]() and [Anbajagane & Lee 2025b]().


## [kllr](https://github.com/afarahi/kllr)

![](/assets/img/code/KLLR.png){:.lead style="width:30%;height:auto;display:block;margin:0 auto"}


[`kllr`](https://github.com/afarahi/kllr) is a tool for performing non-parameteric, local linear regression models. It was designed for characterising halo scaling relations without having to assume a specific functional form. The method is introduced in [Farahi, Anbajagane & Evrard 2022](https://arxiv.org/abs/2202.09903). It can do multivariate linear regression in this non-parameteric manner, as introduced in [Anbajagane, Evrard & Farahi 2021](https://arxiv.org/abs/2109.02713).


## Some of my other codes

And a smattering of other code-bases that are publicly viewable, though they do not have a dedicated code release + documentation.

* [Baryon_Imprints_TNG](https://github.com/DhayaaAnbajagane/Baryon_Imprints_TNG): Interpolator of the halo property scaling relations from [Anbajagane+ 2022](https://arxiv.org/abs/2109.02713)


* [tSZ_profiles](https://github.com/DhayaaAnbajagane/tSZ_Profiles): Data products and theory modelling code for tSZ profiles around clusters, from [Anbajagane+2021](https://arxiv.org/abs/2111.04778)


* [Velocity_Bias](https://github.com/DhayaaAnbajagane/VelocityBias): Interpolator of the galaxy velocity bias from various simulations, as presented in [Anbajagane+ 2021](https://arxiv.org/abs/2110.01683)


* [Jax_cosmo](https://github.com/DhayaaAnbajagane/jax_cosmo): Forked implementation of [jax_cosmo](https://github.com/DifferentiableUniverseInitiative/jax_cosmo) designed for modelling scale-dependent bias, as used in [Gagnon, Anbajagne+ 2024](https://arxiv.org/abs/2312.16289).


* [Balrog_of_the_dwarves](https://github.com/DhayaaAnbajagane/Balrog_of_the_dwarves): One (of many) repos containing my routines for doing synthetic source injection in the DELVE/DECADE data. This repo is for injecting dwarf galaxies into the images.

## Public codes I use often

Some other codes that I use very often:

* [pkdgrav3](https://bitbucket.org/dpotter/pkdgrav3/)
* [2LPTPNG](https://github.com/dsjamieson/2LPTPNG)
* [mpi-rockstar](https://github.com/Tomoaki-Ishiyama/mpi-rockstar) 