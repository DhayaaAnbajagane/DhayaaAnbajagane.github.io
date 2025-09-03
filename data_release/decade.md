---
layout: page
title: DECADE chains
sitemap: False
---

This table describes the chains [provided here](https://drive.google.com/drive/folders/1hg8m-Zyk87wCI-ajMn5XstGZQ4bWDVUc?usp=sharing). In all analyses, we do not consider the shear ratio measurements from DES.

## Table of filenames

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


## Reading out the chains

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