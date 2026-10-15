---
layout: page
title: DECADE redMaPPer public release
sitemap: true
---

0. 
{:toc}

We have generated cluster catalogs for the DECADE and DES footprints, at richness thresholds λ > 20 (main sample) and λ > 5. This was produced using redMaPPer v0.8.7. For each footprint we provide clusters with halo mass estimates, member galaxies, randoms and per-cluster weak-lensing profiles.

All cluster products can be found at the same [Globus endpoint](https://app.globus.org/file-manager?origin_id=0b5ae9e1-9026-4b94-bc29-ff5f51f94671) used for the shear data. Please look in the `cluster catalog` folder.

<!-- TODO: add paper link / arXiv number and a citation request -->

## Cluster Catalog

The catalog is provided under `RedmapperCatalog.hdf5`. It contains the clusters, their member galaxies, and the randoms catalog. Datasets are stored under the hdf5 groups `<SURVEY>/<PRODUCT>/lambda<CUT>/<column>`, with `SURVEY` = `DECADE`, `DES`; `PRODUCT` = `catalog` (clusters), `catalog_members`, `randoms`; `CUT` = `20`, `5`. Each column is its own dataset. Here are simple statistics for the number of objects per category:

| Survey | Sample | Clusters | Members | Randoms |
|--------|--------|---------:|--------:|--------:|
| DECADE | λ > 20 | 26,992 | 1,492,942 | 3,424,509 |
| DECADE | λ > 5 | 357,530 | 8,121,761 | 45,421,661 |
| DES | λ > 20 | 17,970 | 924,437 | 3,243,928 |
| DES | λ > 5 | 258,880 | 5,469,887 | 46,937,408 |

If you are interested in cosmology analyses, and require weak-lensing information, then keep only objects with `FOREGROUND_FLAG == 0`. Some clusters are available in regions without any WL, if the user requires them. In that case drop the flag. You must also apply your own redshift cut (the catalogs have none; randoms cover 0.10 < z < 0.95). We generally limit ourselves to 0.2 < z < 0.65. Here is an example script for reading the data:

```python
import h5py

with h5py.File('RedmapperCatalog.hdf5', 'r') as f:
    g    = f['DECADE/catalog/lambda20']
    z    = g['z_lambda'][:]
    lam  = g['lambda'][:]
    mask = (g['FOREGROUND_FLAG'][:] == 0) & (z > 0.2) & (z < 0.65)
```

The λ > 20 catalog is what should be used for any precision applications, for either cosmology or astrophysics. Lower richness objects are available if the user desires them. The catalogs also contain a `lambda_cyln` variable, whose definition can be found in the catalog paper.

**Masses.** Each cluster has an M200c posterior [Msun/h]: `log10M200c` is its median, and `log10M200c_err_lo` / `log10M200c_err_hi` are the distances to the 16th / 84th percentiles. `log10M200c_flag` denotes the method used to obtain the mass and takes one of the values:

| Flag | Method | DECADE λ > 20 | DES λ > 20 |
|-----:|--------|--------------:|-----------:|
| 1 | Posterior given (λ, z), from the richness–mass relation calibrated on DES×SPT | 25,410 | 16,564 |
| 2 | Individual posterior, joint fit to ACT-matched clusters | 1,531 | 1,143 |
| 3 | Individual posterior, joint fit to SPT-matched clusters (preferred over 2) | 51 | 263 |

It is best to use Flag = 3 objects when available, then 2 and finally 1.

The following describes the most-used columns in the redMaPPer catalogs (all standard redMaPPer columns are included; see Rykoff et al. 2014):

| Column | Description |
|--------|-------------|
| `mem_match_id` | Cluster ID, shared with the member catalog |
| `ra`, `dec` | Position of the most likely central galaxy [deg] |
| `z_lambda`, `z_lambda_e` | Photometric redshift and uncertainty |
| `lambda`, `lambda_e` | Richness and uncertainty |
| `r_lambda` | Richness radius, (λ/100)^0.2 Mpc/h |
| `maskfrac` | Masked fraction of the cluster area |
| `p_cen`; `ra_cent`, `dec_cent`, `id_cent` | Centering probabilities, positions and IDs of the five candidate centrals |
| `mag`, `mag_err`; `refmag`, `refmag_err` | Central galaxy magnitudes (4 bands) and reference-band magnitude |
| `zred`, `zred_e`, `zred_chisq` | Red-sequence photo-z of the central galaxy |
| `cg_spec_z` | Central galaxy spectroscopic redshift, −1 if none |
| `ebv_mean` | Mean E(B−V) over the cluster |
| `lambda_cyln` | Cylinder richness (λ > 20 only), −99 if not computed |
| `log10M200c`, `_err_lo`, `_err_hi`, `_flag` | Mass estimate [log10(Msun/h)], see above |
| `FOREGROUND_FLAG` | Area mask, see above |

## Members

Members carry their host's `mem_match_id`. The membership weight `p * pfree * theta_i * theta_r` summed over a cluster recovers its richness:

```python
import numpy as np, h5py

with h5py.File('RedmapperCatalog.hdf5', 'r') as f:
    c   = f['DES/catalog/lambda20']
    m   = f['DES/catalog_members/lambda20']
    cid = c['mem_match_id'][np.argmax(c['lambda'][:])]
    sel = m['mem_match_id'][:] == cid
    wt  = (m['p'][:][sel] * m['pfree'][:][sel] * 
           m['theta_i'][:][sel] * m['theta_r'][:][sel])
```

| Column | Description |
|--------|-------------|
| `mem_match_id`, `id` | Host cluster ID; galaxy ID in the input photometry |
| `ra`, `dec` | Position [deg] |
| `z` | Cluster redshift used for membership (close to, not equal to, the host's `z_lambda`) |
| `r` | Projected distance from the center [Mpc/h] |
| `p`, `pfree`, `pcol` | Membership probability; probability of not belonging to a higher-ranked cluster; color-only probability |
| `theta_i`, `theta_r` | Luminosity and radial weights |
| `mag`, `mag_err`; `refmag`, `refmag_err` | Magnitudes (4 bands) and reference-band magnitude |
| `zred`, `zred_e`, `zred_chisq`; `chisq` | Red-sequence photo-z; red-sequence χ² at the cluster redshift |
| `zspec` | Spectroscopic redshift, −1 if none |
| `ebv` | E(B−V) |

## Randoms

Match randoms to a cluster sample by applying the redshift cut to `ztrue` and the richness cut to `avg_lambdaout`, using the randoms of the same sample (`lambda20` or `lambda5`). The columns are:

| Column | Description |
|--------|-------------|
| `ra`, `dec` | Position [deg] |
| `ztrue` | Redshift |
| `lambda_in` | Assigned richness |
| `avg_lambdaout` | Recovered richness |
| `weight` | redMaPPer random weight, to ensure the distribution of λ and z matches the data |
| `FOREGROUND_FLAG` | Area mask, see above |

## Lensing

We provide lensing measurements for all clusters with λ > 20. These are in the `RedmapperShear.hdf5` file, which has groups `<SURVEY>/{catalog,randoms}/lambda20` (no λ > 5). Row *i* of each group is row *i* of the same group in `RedmapperCatalog.hdf5`; take positions, redshifts, richnesses and `FOREGROUND_FLAG` from there. Rows with `has_shear = False` have no measurement and zero sums. Only ~5% of randoms have a measurement, so always select on `has_shear`.

| Survey | Clusters with shear | Randoms with shear |
|--------|--------------------:|-------------------:|
| DECADE | 26,665 of 26,992 | 176,716 of 3,424,509 |
| DES | 17,884 of 17,970 | 178,356 of 3,243,928 |

The columns are [`dsigma`](https://github.com/johannesulf/dsigma) pair sums over 29 log-spaced radial bins from 0.01 to 10 comoving Mpc, plus a few per-row quantities:

| Column | Shape | Description |
|--------|-------|-------------|
| `sum 1` | (N, 29) | Number of lens–source pairs |
| `sum w_ls` | (N, 29) | Sum of w_ls |
| `sum w_ls e_t` | (N, 29) | Weighted tangential ellipticity |
| `sum w_ls e_t sigma_crit` | (N, 29) | Weighted tangential ellipticity × Σ_crit |
| `sum w_ls sigma_crit` | (N, 29) | Weighted Σ_crit |
| `sum w_ls R_T` | (N, 29) | Weighted tangential shear response |
| `sum w_ls z_s` | (N, 29) | Weighted source redshift |
| `sum w_ls z_l` | (N, 29) | Weighted lens redshift |
| `sum_pzbf` | (N, 29, 899) | Weighted sum of source-redshift PDFs on the `zbins_pdf` grid, for boost factors (see below) |
| `w_sys` | | Lens weight, 1 for every row |
| `has_shear` | | Whether the row has a measurement |
| `lensing source` | | `decade_N`, `decade_S` or `des` |
| `weight` | | Random weight (randoms only) |

Here w_ls = w_s Σ_crit⁻², e_t is the tangential ellipticity, R_T the tangential shear response and Σ_crit is in Msun/pc². Each group's attributes hold:

| Attribute | Description |
|-----------|-------------|
| `bins` | Radial bin edges |
| `H0`, `Om0` | Cosmology (flat ΛCDM, `H0` = 67.74, `Om0` = 0.3075) |
| `zbins_pdf` | Source-redshift grid for `sum_pzbf` |

The **`compute_deltasigma.py`** file computes ΔΣ for one richness–redshift bin, with the response correction, random subtraction, boost factors and jackknife errors. Installation and usage are at the top of the script:

```
python compute_deltasigma.py --survey DES --z 0.2 0.35 --lam 20 30 --out ds.txt
```

It applies the area mask unless `--no-mask` is given. The core ΔΣ needs only numpy:

```python
import numpy as np, h5py

def stack(g, sel):
    w   = g['w_sys'][:][sel][:, None]
    if 'weight' in g: w = w * g['weight'][:][sel][:, None]  # randoms only
    num = np.sum(w * g['sum w_ls e_t sigma_crit'][:][sel], 0)
    den = np.sum(w * g['sum w_ls'][:][sel], 0)
    R   = np.sum(w * g['sum w_ls R_T'][:][sel], 0) / den
    return num / den / R

with h5py.File('RedmapperCatalog.hdf5', 'r') as cat, h5py.File('RedmapperShear.hdf5', 'r') as sh:

    c, r   = cat['DES/catalog/lambda20'], cat['DES/randoms/lambda20']
    gc, gr = sh['DES/catalog/lambda20'],  sh['DES/randoms/lambda20']

    zc, lc = c['z_lambda'][:], c['lambda'][:]
    zr, lr = r['ztrue'][:],    r['avg_lambdaout'][:]

    sel_c  = gc['has_shear'][:] & (c['FOREGROUND_FLAG'][:] == 0) & (zc > 0.2) & (zc < 0.35) & (lc > 20) & (lc < 30)
    sel_r  = gr['has_shear'][:] & (r['FOREGROUND_FLAG'][:] == 0) & (zr > 0.2) & (zr < 0.35) & (lr > 20) & (lr < 30)

    ds     = stack(gc, sel_c) - stack(gr, sel_r)
```

**Boost factors** use `sum_pzbf`, the weighted sum of source redshift PDFs per radial bin, with shape (N, 29, 899) on the `zbins_pdf` grid. Read it by row (`g['sum_pzbf'][rows]`, with `rows` increasing).

{% include abbreviations.md %}
