---
layout: page
title: My datasets
description:
no_groups: true
---

0. 
{:toc}

My work produces a variety of datasets from telescope images and also from simulations. Here is a list of some of the dataproducts whose development I led or was heavily involved in, and how to get access to them.


## DECADE shear catalogs and datavectors

The [shear catalogs](https://datalab.noirlab.edu/data-explorer?showTable=delve_dr3.decade_shear) are immenent at the DataLab by NOIRLab. The datavector for the NGC and SGC regions is available at the `cosmosis-standard-library` [in this location](https://github.com/joezuntz/cosmosis-standard-library/tree/main/likelihood/decade). The associated decam likelihood can be run [using this ini](https://github.com/joezuntz/cosmosis-standard-library/blob/main/examples/decam-13k.ini). The datavectors and cosmology posteriors derived in [Anbajagane & Chang+ 2025e]() are available [in this public folder](https://drive.google.com/drive/folders/1hg8m-Zyk87wCI-ajMn5XstGZQ4bWDVUc?usp=sharing), with descriptions of filenames [in this table](../data_release/decade).

## Ulagam simulations

The [Ulagam simulation suite](https://ulagam-simulations.readthedocs.io/) is set a full-sky N-body simulations that are focused on resolving signatures from primordial physics in the deeply nonlinear regime. The original sims were introduced in [Anbajagane+ 2024](https://arxiv.org/abs/2310.02349), and additional sims were added in [Anbajagane & Lee 2025a]() and [Anbajagane & Lee 2025b]().


## DELVE DR3 Gold

The DELVE datarelease can be found [at Noirlab here](https://datalab.noirlab.edu/data/delve). The coadd images, produced as part of the DECADE campaign within DELVE, cover an additional $$14,\!000 \,\,{\rm deg}^2$$ of sky outside the DES DR2. The catalogs from this coadd processing can be found at [this NOIRLab table](https://datalab.noirlab.edu/data-explorer?showTable=delve_dr3.coadd_objects). The raw images are being uploaded currently.


## DES Y6 Balrog

The DES Y6 synthetic source injection (SSI) campaign is the largest dataset at this level of fidelity --- every image in the DES Y6 dataset has been reprocessed with synthetic sources injected into the image. The catalogs [can be found here](https://des.ncsa.illinois.edu/releases/y6a2/Y6balrog) and are introduced in [Anbajagane+ 2025](https://arxiv.org/abs/2501.05683).

## IllustrisTNG halo structure

I've generated curated, Rockstar-like catalogs from IllustrisTNG and they are part of [TNG's supplemental data release](https://www.tng-project.org/data/docs/specifications/#sec5q). These were used in the baryon imprints study of [Anbajagane+ 2021](https://arxiv.org/abs/2109.02713).


## Other data products I often use:

* [IllustrisTNG](https://www.tng-project.org/about/)
* [Quijote](https://quijote-simulations.readthedocs.io/)
* [CAMELS](https://camels.readthedocs.io/)
* [DES Y3](https://des.ncsa.illinois.edu/releases/y3a2)
* [Planck @ Lambda](https://lambda.gsfc.nasa.gov/product/planck/)
