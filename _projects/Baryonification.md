---
layout: project
title: 'Baryonification'
caption: Phenomenological models of astrophysics set within cosmological contexts
description: 
date: 22 August 2025
image: 
  path: /assets/img/research/BaryonForge.jpg
links:
  - title: BaryonForge
    url: https://github.com/DhayaaAnbajagane/BaryonForge
sitemap: false
---

Having spent most of the 2020s comparing simulations through a variety of their halo properties (see [Baryon Imprints](/_projects/BaryonImprints.md)) I have used my recent time building phenomenological models. When performing cosmological analyses, a standard approach is to marginalize over astrophysical nuisances in the typical sense, 

$$P({\rm cosmo}) \propto \int P({\rm cosmo} \mid {\rm astro pars.})\, P({\rm astro pars.})$$. 

This can be done by varying a set of hyperparameters of the astrophysical model. However, in reality, the required operation is 

$$P({\rm cosmo}) \propto \int P({\rm cosmo} \mid {\rm astro pars.}, {\rm astro models.})\, P({\rm astro pars.} \mid {\rm astro models.}) \, P({\rm astro models.})$$. 

That is, it is not adequate to just marginalize over the astrophysics parameters but we need to marginalize over the space of models as well. The latter is an ill-defined question and cannot be answered in a principled manner. Many different experts have come up with different (equally reasonable) astrophysical models that solve different sets of equations for the macrophysical approximation to astrophysical processes.

Baryonification is an approach that circumvents this issue for the density field, by connecting the baryon signatures in the density field directly to observables --- such as halo profiles and gas/star fractions --- rather than microphysical equations from different astrophysics processes. Thus, observables can be constrained with available datasets and the model can be used to generate predictions for the density field signatures.

### Map-level Baryonification

In [Anbajagane, Pandey & Chang 2024](https://arxiv.org/abs/2409.03822) we introduced a coherent, robust model for implementing Baryonification at the map-level. The original technique is used on particle snapshots from an N-body simulation. Particles are radially offset from their nearest halo in a manner that mimics the impact of baryons. However, this process is expensive in both computing and storage requirements. In `BaryonForge` we introduce a method that works directly at the map-level, incorporating the projection effects and pixel convolutions. This method has since been validated in [Zhou, Gatti, Anbajagane, Dodelson+ 2025](https://arxiv.org/abs/2505.07949) and found to model the lensing field at $$1\%$$ simultaneously for a variety of higher-order statistics and redshift bins.

![](/assets/img/projects/BaryonForgeMassPressure.jpg){:.lead style="width:100%;height:auto;display:block;margin:0 auto"}

*Example of how different baryonification models consistently impact the pressure (top) and density (bottom). We normalize the bottom row by the TNG density field (hence why the left panel is constant). Locations with high pressures are also accompanied by larger distortions in the density field. BaryonForge provides a consistent, connected model of the two.*
{:.figcaption}


### Halo-model predictions from BCemu, Bacco, and HMx

`BaryonForge` is highly modular, and so it is easy to implement additional models. In [R.S, Pandey, Anbajagane, Krause+ 2025](https://arxiv.org/abs/2507.13317) we tested these models against the Magneticum simulations. In particular, we did a deep dive into the flexibility within each model and how easily the models could be fit to a set of observables "X" and predict a different set "Y".

![](/assets/img/projects/BaryonForgeHaloModel.jpg){:.lead style="width:100%;height:auto;display:block;margin:0 auto"}

*[Figure 7 in R.S+ 2025](https://arxiv.org/abs/2507.13317). The halo-model based predictions are fit to a set of three power spectra and can predict the matter fractions and halo profiles in a consistent manner. The Schneider model performs the best, while the other two are still reasonable though not quite as precise.*
{:.figcaption}


### Baryons with Fast Radio Bursts

Fast radio bursts (FRBs) give a completely different window into the baryons. In [Sharma+ 2026 (inc. Anbajagane)](https://arxiv.org/abs/2604.17162) and many associated works, we used FRBs to constrain the suppression of the matter power spectrum on scales $$k \sim 0.1-3\,h/{\rm Mpc}$$ and the gas fractions of groups and clusters. All models for these analyses are done using `BaryonForge`. We have since extended this to cross-correlations of the dispersion measures of 3,455 CHIME/FRB sources with ten different large-scale structure and baryon tracers in [Sharma, Krause, Ravi, Anbajagane+ 2026](https://arxiv.org/abs/2604.22105).

![](/assets/img/projects/FRB_PkSuppression.svg){:.lead style="width:100%;height:auto;display:block;margin:0 auto"}

*[Figure 4 in Sharma+ 2026](https://arxiv.org/abs/2604.17162). The suppression of the matter power spectrum inferred from FRBs compared to constraints from cosmic shear, X-ray, and SZ observations, and to predictions from hydrodynamical simulations. The FRBs prefer moderate feedback.*
{:.figcaption}

{% include abbreviations.md %}
