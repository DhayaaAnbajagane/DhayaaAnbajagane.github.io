---
layout: project
title: 'Baryon Imprints on Dark Matter Halos'
caption: How does astrophysics change halo structure?
date: 20 August 2025
image: 
  path: /assets/img/projects/Feedback_Variation.jpg
links:
  - title: TNG outputs
    url: https://github.com/DhayaaAnbajagane/Baryon_Imprints_TNG
  - title: CAMELS outputs
    url: https://github.com/mufanshao/CAMELSconcentration
sitemap: false
---

A fascinating part of our Universe is the interaction between the astrophysical process from small scales and the cosmological evolution on large scales. As we have come to realize, these two are intertwined in a highly nonlinear manner. Over the past five years, I've worked on various simulation measurements to understand this behavior and to characterise the range of possible behaviors in these simukations.


### From dwarf galaxies to galaxy clusters

In [Anbajagane, Evrard & Farahi 2023a](https://arxiv.org/abs/2109.02713) we performed one of the first, consistent extractions of baryon signatures in scaling relations across a mass range spanning six orders of magnitude. The detailed backreactions of baryons onto the DM evolution has unique phenomology depending on the mass range under consideration.

![](/assets/img/projects/Feedback_Variation.jpg){:.lead style="width:100%;height:auto;display:block;margin:0 auto"}

*[Figure 7 in Anbajagane+ 2023a](https://arxiv.org/abs/2109.02713) The change in the concentration between hydro and dark matter only simulations (left), and estimates of the average total power from a given process. Both quantities have a clear mass-dependence that is strongly connected. The change in concentration is negative (positive) when feedback (cooling) dominates. The right panels show the change in concentration and velocity dispersion in a set of small TNG runs where a single AGN parameter was varied.*
{:.figcaption}


### The concentration-mass relation in Camels

We then extracted the concentration--mass relation from the CAMELS simulations. These are very small boxes, $$V = (25 {\rm Mpc/h})^3$$, but we can get some sense for what happens in massive halos by stacking the 1000 available sim boxes together and training a global linear regression model (using the `kllr`, described in [my code page](/code.md)). Mufan Shao, a former undergrad at UChicago, led this series of works starting with [Shao, Anbajagane, and Chang 2022](https://arxiv.org/abs/2212.05964) and extracted the local linear regression models.

![](/assets/img/projects/Camelscvir.jpg){:.lead style="width:100%;height:auto;display:block;margin:0 auto"}


*[Figure 6 in Shao, Anbajagane, and Chang 2022](https://arxiv.org/abs/2212.05964). Variations in the concentration mass relation as you vary six paramters from the CAMELS suite.*
{:.figcaption}