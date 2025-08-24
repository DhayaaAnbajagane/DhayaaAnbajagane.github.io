---
layout: page
title: Research
description:
no_groups: true
---

0. 
{:toc}

**The question that motivates me most is "what happened at the first moments in our Universe?".** I work on understanding fundamental physics from the earliest epochs of our Universe using observations of structure (weak lensing, galaxy clusters, tSZ etc.). This naturally requires working on better understanding how we go from pixels to objects, and also on the astrophysical processes occuring within these structures. As a result I work on a broader range of topics, spanning the measurement, modelling, and inference for all these probes.

The data products and software packages from my research projects can be found at my [data products page](/data.md) and [code page](/code.md).


## Inflation and Cosmological Colliders
Inflation is our leading theory for the physics governing the earliest epochs in our Universe, and for what generated fluctuations in the initial density field. This process is mediated by a particle dubbed the "inflaton". However, we still have fundamental questions about this epoch. How many particles participated in inflation? What are their masses, spins, symmetries, etc.? What kinds of interactions do they have with each other? Changes to this physics alters the initial density field, and therefore the late-time structure we see. Searching for these signatures is akin to particle colliders on the Earth, like the LHC, but now using correlations on the sky. So this research program is also commonly referred to as "Cosmological Colliders"

A core part of my research program is building new tools to extend the modelling of these signatures and thereby use new measurements of structure to answer these questions. These novel methods are publicly available in the [`Aarambam`](https://github.com/DhayaaAnbajagane/Aarambam) package, while all simulations from my program are publicly available in the [`Ulagam` suite](https://ulagam-simulations.readthedocs.io/en/latest/). 


![](/assets/img/research/FeynmanDiagrams.svg){:.lead style="width:100%;height:auto;display:block;margin:0 auto"}

*Feynman diagram sketches of the different kinds of particle interactions during the inflationary epoch. My work focuses on all three, with a particular focus on the "Massive Exchange" interactions, also referred to as the Cosmological Collider.*
{:.figcaption}

## Weak lensing
Weak gravitational lensing is the distortion of light from distant sources due to the matter intervening the source and us, the observer. It is a powerful, mature technique for mapping the distribution of all matter (even those that don't emit light, i.e. dark matter) in the visible Universe. I have worked on everything from the processing of pixel-level data, the measurement of galaxy shapes and redshifts from this data, building models to analyse the measurements, and obtaining cosmology results. We refer to this as the "pixels-to-cosmology" pipeline, and I had led this for the DECADE (Dark Energy Camera All Data Everywhere) Cosmic Shear project. All I have also been actively involved in the pixel-level processing for the Dark Energy Survey, and am now working on the upcoming Rubin Observatory data, which will dramatically improve our ability to measure lensing.

![](/assets/img/research/DECam.jpg){:.lead loading="lazy" style="width:80%;height:auto;display:block;margin:0 auto"}

*The sky coverage of the DECADE survey, alongside DES and upcoming lensing surveys like LSST and Euclid. The DECADE data (blue) triples the existing area coverage from lensing surveys.*
{:.figcaption}

## Baryons, tSZ, and cross-correlations
An active area of research is understanding the main astrophysical processes governing the evolution of the density and pressure (or temperature) of the baryon component of our Universe. I have worked on this actively in simulations, including several projects with fantastic undergrads at UChicago, and in data via measurements of pressure profiles around galaxy clusters. A key challenge that I work on is the efficient and flexible modelling of different baryonic fields (density, pressure, etc.). My software package, [`BaryonForge`](https://github.com/DhayaaAnbajagane/BaryonForge.git), is actively used in the community to model these fields both at the level of summary statistics and at the full field/map. My observable of choice is the thermal Sunyaev Zeldovich effect, which is a tracer of the gas pressure, and be observed in mm-wave (CMB) surveys. I work with data from the South Pole Telescope, the Atacama Cosmology Telescope, and Planck. I currently lead the development of tSZ maps for the South Pole Telescope.

![](/assets/img/research/BaryonForge.jpg){:.lead style="width:100%;height:auto;display:block;margin:0 auto"}

*Gas pressure maps from IllustrisTNG-300 (left) and mock maps made from BaryonForge using just the halo catalog. The three panels vary the radial extent of the gas within a halo (stronger feedback leads to puffier halos). The main utility in BaryonForge is simultaneously/consistently modelling the impact of baryons on both the matter density and the gas thermodynamics fields.*
{:.figcaption}

## Photometric surveys and data calibration
A large part of my research is processing image-level data from photometric surveys. I particularly enjoy using synthetic source injection as a method of calibrating and understanding our pipelines well. This is a technique where you inject synthetic light profiles of any object of interest (galaxies, stars, etc.) into the real images and rerun the entire processing pipeline. The final data products are a set of simulated data that reflect the range of complexities arising from a multi-component pipeline operating on messy, real data. I have led the development of such tools for the DECADE and DES survey, including the extension of these tools for a variety of science cases such as dwarf galaxy searches, stellar stream detection, galaxy cluster selection etc. I am actively involved in using my existing data products to help plan next steps in calibrating the upcoming LSST datasets.

![](/assets/img/research/Y6Balrog.jpg){:.lead style="width:100%;height:auto;display:block;margin:0 auto"}

*Number density distribution of synthetic sources from Balrog (left) and those from DES Y6 data (right). There are clear visual features shared by the two, which is an example of how Balrog can be used to calibrated observational biases in photometric data.*
{:.figcaption}

## Other things!
An assortment of other topics I've worked on are: efficient statistics for non-Gaussian information, localized linear regression techniques, galaxy velocity bias, large-scale structure from gravitational wave experiments etc.