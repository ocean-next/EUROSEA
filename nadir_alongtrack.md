# Extracting alongtrack nadir SSH from eNATL60-no-tide in the EUROSEA target regions
Stephanie Leroux, UPDATED  2022-03-14.

## _What?_ 
  - Along-track sampling of the model SSH and SLA(*) (eNATL60-no-tide) in the MEDWEST subregion. 
  - Sampling along the satellite tracks of Jason3, Altika, Cryosat-2 (c2n), H2B, Sentinel-3A, Sentinel-3B
    - From 2020-07-01 to 2020-12-31.
    - From 2021-01-01 to 2021-06-30.
  - (\*) The model SLA(\*) is computed by removing the time mean over the 1-year period (2020-07-01 to 2021-06-31) __and also then removing the spatial mean over the basin at each hourly model output__ as a proxy for filtering out large scales (as requested by SOCIB/IMEDEA/CLS).
  - The along track interpolation is made with the software gonzag (https://github.com/brodeau/gonzag) from Laurent Brodeau,  based on  the Akima interpolation method.
  - Each file is 6-month long.
  - In each `*SLA*` file you’ll find:
    - sla_unfiltered (the real obs value (SLA)
    - slam (Sea Level Anomaly from model after removing time mean and spatial mean, interpolated at all alongtrack locations)
    - slam_np (Sea Level Anomaly from model after removing time mean and spatial mean, at nearest model grid point )
  - In each `*SSH*` file you’ll find:
    - sla_unfiltered (the real obs value (SLA)
    - sossheig (SSH from model, interpolated at all alongtrack locations)
    - sossheig_np (SSH from model , at nearest model grid point )
  - Important: Note that the the real obs value ('sla_filtered')  is _not_ expected to be consistent with the interpolated model values (slam) since the model was run in 2009-2010 and the real obs are taken in the years where the satellites exist (2020-2021).
  - Important too: If you need to retrieve the time-mean and spatial mean that was substracted from the model SSH, you can substract both interpolated files:  SSH_interpolated - SLA_interpolated. You can also look directly at the time-mean model gridded field (on the opendap).


## _Where to download the data?:_
  - On the opendap: https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/catalog/meomopendap/extract/lerouste/Eurosea2022/pseudo-ssh-alongtrack/catalog.html
  - In `INTERP_RESULTS` you'll find the interpolation results (for SLA and SSH).
  - In `DATA_src` you'll find all the input data used to perform the interpolation: 
    - along track real obs downloaded from CMEMS portal and reformatted (see github notebooks for more details): jason3, sentinel3a, sentinel3b, altika, h2b, cryosat2.
    - model gridded SSH and SLA (SLA: time mean and spatial mean removed): caution: in both files the variable is named sossheig. 
    - model time-mean over the 2020-07-2021-06 period : *_TM.nc  (look for the sossheig_mean variable)
    - model spatial mean in the west med region at each hourly output:  *_spmean.nc



## _How is this done? (step by step documentation)_
  - Step1. [Notebook](https://github.com/ocean-next/EUROSEA/blob/main/notebooks/2022-02-18_download-sat-data.md) explaining how to download and prepare the satellite files before applying the interpolation tool.
  - Step2. [Notebook](https://github.com/ocean-next/EUROSEA/blob/main/notebooks/2022-02-18_prepare_model_files.md) explaining how to prepare the model files before applying the interpolation tool.
  - Step3. [Notebook](https://github.com/ocean-next/EUROSEA/blob/main/notebooks/2022-03-09_interpolation_alongtrack.ipynb) demonstrating the interpolation step.
  - Step4. [Notebook](https://github.com/ocean-next/EUROSEA/tree/main/notebooks/2022-02-18_plot_and_check_alontrack.ipynb) demonstrating how to read and plot the interpolated data and compare to the gridded model fields.

![subregions](./figs/jason3.png)<br>
_Fig.1 Example of interpolated SSH along jason3 tracks (3 day period)_
