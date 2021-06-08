# Advecting  lagrangian particles with eNATL60 hourly currents (u,v at 15-m)

### b. For IMEDEA: 49 particles advected for 7 days (2009-09-01 to 2009-09-07) in a small subregion region

* _Where to download the data:_  https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/catalog/meomopendap/extract/Eurosea/Lagragian_trajectories/catalog.html

* _What trajectories were computed:_
  - 49 particles, evenly spaced, are initiated  in each of the small subregion in MEDWEST and NANFL regions (see Fig.1 below for illustration). 
  - The lagrangian trajectories are computed  for 6 days based on the horizontal currents (u,v) at 15 m depth, starting on the 1st of september 2009, and computed and saved every 15 min.

* _What do the netcdf files  contain:_
  - The files contain variables: time, lat, lon of each trajectory, and also interpolated values of ssh, u_convert, v_convert  at each particle location. 
  - The interpolation in space is done by Ocean Parcels, which carefully takes into account the specificities of the NEMO grid (C-grid) (see: https://nbviewer.jupyter.org/github/OceanParcels/parcels/blob/master/parcels/examples/tutorial_nemo_curvilinear.ipynb).
  - Each variable has  2 dimensions: ‘traj’ (of size 49, for each particle) and ‘obs’ (of size 577, for each 15-min timestep of the 6-day period). 
  - the interpolated u and v at 15m are given in unit: m/s in the variables u_conv and v_conv in the file,   and in unit: deg/s in the variables u_interp, v_interp. 
Note2: 

* _Jupyter notebook available [here](./notebooks/2021-05-01_SLX_JZ_lagrangiantraj_4IMEDA.ipynb)._

![traj1](./figs/figlagrangian1.png)<br>
_Fig.2 Initial location (a) and trajectories (b) of the 49  lagrangian particles  over the 6-day period from 1st of september to 7th of september 200,9 computed with Ocean Parcels from the eNATL60 simulation (no tide) hourly outputs in the MEDWEST predefined region. The SSH field is shown as background : (a) on the 1st of september, and  (b) averaged over the 6-day period._

