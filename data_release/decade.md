---
layout: page
title: DECADE public release
sitemap: False
---

<style>
.page__content strong.bold-red { color: #e53935 !important; }
@media (prefers-color-scheme: dark) {
  .page__content strong.bold-red { color: #ff6659 !important; }
}
</style>

## List of data products
First, we list the different products made available so far. Each is detailed further below in its own subsection. If you do not see a product of interest in this list, please contact me! Our goal is to have made all useful products available right away.

**1. Shear Catalog:**{: .bold-accent} The shear catalog is available at [Noirlab](https://datalab.noirlab.edu/data-explorer?showTable=delve_dr3.decade_shear), and [via Globus](https://app.globus.org/file-manager?origin_id=0b5ae9e1-9026-4b94-bc29-ff5f51f94671). If you want to query small subsets, then the Noirlab portal is the best place to go. If you want to use the full catalog (e.g., for correlation studies) the Globus portal is easier. This portal also contains a single HDF5 file (`shear_catalog_sparse.hdf`) which is a curated subset of all objects relevant for the cosmology analysis alone. This is a significantly smaller subset of the full catalog. The globus portal also contains the redshift distributions for the four bins. The necessary calibrations are found in the Table below, can also be obtained from the [paper release here](/_projects/DECADE.md). You will need to apply the shear response yourself.


**2. Cosmology Likelihood:**{: .bold-accent} The full cosmology likelihood is available in the `cosmosis-standard-library`. The ini file for the decam13k likelihood is [here](https://github.com/joezuntz/cosmosis-standard-library/blob/main/examples/decam-13k.ini) and is the recommended starting point. This file can run a combination of DECADE NGC, DECADE SGC, and DES Y3. All the necessary data for the likelihood runs are already on cosmosis.


**3. Cosmic Shear Datavectors:**{: .bold-accent} The associated cosmic shear datavectors, ensemble redshift distributions, and covariance matrices are available [in this public folder](https://drive.google.com/drive/folders/1hg8m-Zyk87wCI-ajMn5XstGZQ4bWDVUc?usp=sharing), and also already in the `cosmosis-standard-library`. See the ini file mentioned above to see the relative filepath within the CSL library. They are also found in the `datavectors` and `n_of_z` folders within the [Globus](https://app.globus.org/file-manager?origin_id=0b5ae9e1-9026-4b94-bc29-ff5f51f94671) endpoint.


**4. DELVE DR3:**{: .bold-accent} The superset `DELVE DR3` catalog, which contains all detected objects, is available at [Noirlab via a queryable database](https://datalab.noirlab.edu/data-explorer?showTable=delve_dr3.coadd_objects). See also this page for more details on the [DELVE data release](https://datalab.noirlab.edu/data/delve). The raw coadd images, including a cutout service, are made available via Noirlab.


**5. Cosmology Posteriors:**{: .bold-accent} The chains from the various results shown in [Anbajagane, Chang et. al (2025e)](https://arxiv.org/abs/2509.03582) are all available as MCMC chains [provided here](https://drive.google.com/drive/folders/1hg8m-Zyk87wCI-ajMn5XstGZQ4bWDVUc?usp=sharing). See the subsection below for details on what chains are available and what the filenames map to.

## Shear catalog

Both Noirlab and Globus have the entire base shear catalog, i.e. any and all measurements of shape made for the DECADE coadd detections. This is a significantly larger superset of the fiducial cosmology catalog. The latter is also provided as a single HDF5 file for ease of use. The cosmology selections can be applied as

~~~python
with h5py.File('shear_catalog_sparse.hdf5', 'r') as f:
    mask = f['MCAL_SEL_NOSHEAR'] == bin_ind  
~~~

where `bin_ind = (1, 2, 3, 4)`. We denote unselected objects with `bin_ind = 0`. A file in the `scripts` directory of the Globus endpoint lists the shear response calculation required. The quick calibration parameters are found below. If you are not using our fiducial selection, these numbers will be different. If you subselect objects based on area, it is mostly fine to use the numbers below. If you subselect on magnitudes and colors, then that is no longer true. We may be able to provide you with recalibrated numbers for simpler selection choices, please reach out!

| Bin | $$m$$ [$$10^{-2}$$] | $$\sigma(\langle z\rangle)$$ [$$10^{-2}$$] | $$R = (R_{11, \rm tot} + R_{22, \rm tot})/2$$ | 
|-----------------|:-----------|:------------|:------------|
| NGC Bin 1 | $$-0.92 \pm 0.296$$ | $$1.63$$ | $$0.836$$ |
| NGC Bin 2 | $$-1.90 \pm 0.421$$ | $$1.39$$ | $$0.771$$ |
| NGC Bin 3 | $$-4.00 \pm 0.428$$ | $$1.01$$ | $$0.741$$ |
| NGC Bin 4 | $$-3.73 \pm 0.462$$ | $$1.17$$ | $$0.621$$ |
| SGC Bin 1 | $$-1.33 \pm 0.472$$ | $$1.61$$ | $$0.844$$| 
| SGC Bin 2 | $$-2.26 \pm 0.657$$ | $$1.40$$ | $$0.778$$| 
| SGC Bin 3 | $$-3.67 \pm 0.697$$ | $$1.00$$ | $$0.748$$| 
| SGC Bin 4 | $$-5.72 \pm 0.804$$ | $$1.16$$ | $$0.626$$| 


And here is a description of all the columns in the catalog:

| Column | Description |
|---|---|
| COADD\_OBJECT\_ID | Unique identifier for the coadded objects |
| DEC | Declination, in degrees |
| DNF\_D1 | DNF photo-z photometric directional distance to nearest neighbor. |
| DNF\_DE1 | DNF photo-z photometric Euclidean distance to nearest neighbor. |
| DNF\_ID1 | DNF photo-z COADD\_OBJECT\_ID corresponding to the nearest neighbor in the training sample. |
| DNF\_Z | DNF photo-z primary point estimate obtained by fitting to the directional neighborhood.|
| DNF\_ZN | DNF photo-z nearest neighbor spec-z. Useful for estimating N(z) for a given sample. |
| DNF\_ZSIGMA | DNF photo-z uncertainty estimate from photometric uncertainties and residuals from the neighborhood fit |
| DNF\_ZERR\_FIT | DNF photo-z error term derived from the residuals of the regression fit |
| DNF\_ZERR\_PARAM | DNF photo-z error term due to magnitude/flux uncertainties propagation |
| DNF\_NNEIGHBORS | DNF photo-z number of neighbors used for the DNF\_Z estimate |
| FLAGS\_FOOTPRINT | Use FLAGS\_FOOTPRINT == 1 to select objects inside the standard "Gold" footprint.|
| FLAGS\_FOREGROUND | Flag describing whether the object is contained in a region with a foreground astrophysical object; recommend FLAGS\_FOREGROUND = 0 for general extragalactic studies. |
| MCAL\_FLAGS | use MCAL\_FLAGS == 0 for the science sample |
| MCAL\_FLUX\_(RIZ)\_(NOSHEAR, 1P, 1M, 2P, 2M) | Metacal fluxes in r, i, z bands |
| MCAL\_FLUX\_(RIZ)\_(NOSHEAR, 1P, 1M, 2P, 2M)\_DERED\_SFD98 | extinction-corrected (SFD98) version of metacal fluxes |
| MCAL\_FLUX\_(RIZ)\_ERR\_(NOSHEAR, 1P, 1M, 2P, 2M) | The 1sigma error on the metacal fluxes |
| MCAL\_FLUX\_(RIZ)\_ERR\_(NOSHEAR, 1P, 1M, 2P, 2M)\_DERED\_SFD98 | The 1sigma error on the extinction-corrected metacal fluxes |
| MCAL\_G\_1\_(NOSHEAR, 1P, 1M, 2P, 2M) | First component of object ellipticity |
| MCAL\_G\_2\_(NOSHEAR, 1P, 1M, 2P, 2M) | Second component of object ellipticity |
| MCAL\_G\_COV\_0\_0\_(NOSHEAR, 1P, 1M, 2P, 2M) | Covariance of the G\_1 estimate |
| MCAL\_G\_COV\_0\_1\_(NOSHEAR, 1P, 1M, 2P, 2M) | Cross covariance of G\_1 and G2 |
| MCAL\_G\_COV\_1\_0\_(NOSHEAR, 1P, 1M, 2P, 2M) | Cross covariance of G\_2 and G\_1 (same as COV\_0\_1) |
| MCAL\_G\_COV\_1\_1\_(NOSHEAR, 1P, 1M, 2P, 2M) | Covariance of the G\_2 estimate |
| MCAL\_W\_(NOSHEAR, 1P, 1M, 2P, 2M) | Shear weights used in the cosmology analysis |
| MCAL\_PSF\_G\_1\_NOSHEAR | First component of PSF ellipticity |
| MCAL\_PSF\_G\_2\_NOSHEAR | Second component of PSF ellipticity |
| MCAL\_PSF\_T\_NOSHEAR | Size of the PSF |
| MCAL\_S2N\_(NOSHEAR, 1P, 1M, 2P, 2M) | Signal-to-noise of the object |
| MCAL\_SEL\_(NOSHEAR, 1P, 1M, 2P, 2M) | Object selection for the cosmology sample. If "mcal\_sel == 0" the object is not selected. Objects are assigned values of [1, 4] depending on which tomographic redshift bin they are assigned to. |
| MCAL\_T\_(NOSHEAR, 1P, 1M, 2P, 2M) | Size of the object (after PSF deconvolution) |
| MCAL\_T\_RATIO\_(NOSHEAR, 1P, 1M, 2P, 2M) | Ratio of  object and PSF sizes |
| RA | Right ascension |

Note that the catalogs contain redshift point estimates from the "Directional Neighborhood Fitting" (DNF) algorithm. These were not used in our fiducial cosmology analysis, but are provided here as they are useful for cluster lensing and other downstream uses of the public catalog. This redshift was determined using the SOF (single object fitting) fluxes provided in the DELVE DR3 processing. 

The metacal-based quantities have five variants. `Noshear` is the fiducial result, while `1p, 1m, 2p, 2m` are variants where the galaxy image was sheared in a specific direction. The latter are used to estimate the shear response. Metacal was only run on `riz` bands. 


## Cosmology Posteriors
This table describes the chains [provided here](https://drive.google.com/drive/folders/1hg8m-Zyk87wCI-ajMn5XstGZQ4bWDVUc?usp=sharing). In all analyses, we do not consider the shear ratio measurements from DES.

### Table of filenames

| Filename | Description |
|-----------------|:-----------|
| decam13k.txt | The fiducial analysis combining NGC, SGC, and DES Y3. |
| decam10k.txt | Combination of just NGC and DES Y3|
| decade-ngc.txt | DECADE NGC-only results|
| decade-sgc.txt | DECADE SGC-only results|
| des.txt | Results from DES Y3 (note we never use shear ratio in any of our analyses)|
| decam13k-ext.txt | Combination of DECam 13k with DES Y5 SNe and DESI DR2 BAO|
| decam13k-ext-w0wa.txt | Decam13k + Ext constraints on the w0-wa dynamical dark energy model|
| decam13k-ext-wphi.txt | Decam13k + Ext constraints on the wphi model of Shajib & Frieman 2025|
| decam13k-bacco.txt | DECam13k analysis using all scales and modelling baryons with the public Bacco emulator|
| decam13k-bcemu.txt | DECam13k analysis using all scales and modelling baryons with the public Bcemu emulator|
| decam13k-Tagn.txt | DECam13k analysis using all scales and modelling baryons with HMCode 2020|
| decam13k-bfg-bacco.txt | DECam13k analysis using all scales and modelling baryons with BaryonForge-based halo model of Bacco|
| decam13k-bfg-bcemu.txt | DECam13k analysis using all scales and modelling baryons with BaryonForge-based halo model of BCemu|
| decam13k-bfg-bacco-wide.txt | The "BFG-Bacco Wide" constraints from the paper|
| decam13k-Tagn-wide.txt | The "Tagn Wide" constraints from the paper|


### Reading out the chains

Here are some utils for reading the chains into a dataframe.

~~~python
def _get_names(file):

    with open(file, 'r') as f:
        params = f.readline()[1:-1].split('\t')
        p_type = [x.split('--')[0] if '--' in x else 'None' for x in params]
        p_name = [x.split('--')[1] if '--' in x else x for x in params]
        p_name = [n + '_delve' if 'delve' in t.lower() else n for n, t in zip(p_name, p_type)]
        p_name = [n + '_sgc'   if 'sgc'   in t.lower() else n for n, t in zip(p_name, p_type)]
        p_name = [n + '_des'   if 'des'   in t.lower() else n for n, t in zip(p_name, p_type)]
        p_name = [n + '_kids'  if 'kids'  in t.lower() else n for n, t in zip(p_name, p_type)]
        p_name = [n + '_' + t  if 'halo_model_parameters' in t else n for n, t in zip(p_name, p_type)]
        p_type = ['None' if p.upper() == p else p for p in p_type]

    p_name = [n + '_lens' if 'lens' in t else n for t, n in zip(p_type, p_name)]
    
    return p_type, p_name


def load_chain_info(file):

    assert os.path.isfile(file), f"The path {file} does not exist"

    CHAINS = pd.read_csv(file, comment = '#', names = _get_names(file)[1], sep = r'\t', engine = 'python')
    
    if 'log_weight' in CHAINS.keys(): CHAINS['weight'] = np.exp(CHAINS['log_weight'])
    if 'OMEGA_M' in CHAINS.keys(): CHAINS['omega_m'] = CHAINS['OMEGA_M']
        
    CHAINS = CHAINS[np.isfinite(CHAINS['post'])]
        
    CHAINS['S8']   = CHAINS['SIGMA_8'] * (CHAINS['omega_m'] / 0.3)**0.5

    return CHAINS


def setup_MCsamples(C, P):
    """
    C is the list of chains (as dataframes) and P is the list of param names you want.
    If a given param name is not in a given chain, we will drop the param from the call for
    that chain
    """
    F = []
    for c in C: 
        
        P_tmp = [p for p in P if p in c.keys()]
        F.append(MCSamples(samples = c[P_tmp].to_numpy(), weights = c['weight'].values, names = c[P_tmp].keys()))

    for f in F:
        for param in f.paramNames.names:
            if param.name in labels: param.label = labels[param.name]
    
    return F
~~~