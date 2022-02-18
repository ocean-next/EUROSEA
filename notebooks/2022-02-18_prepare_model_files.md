## Prepare model gridded files:

* The interpolation tool ([gonzag](https://github.com/brodeau/gonzag)) will need the model files at a specific format with only the variable (sossheig) and `glamt` and `gphit` the latitude and longitude of the model grid of SSH (i.e. on the T-grid points  in NEMO). So from the native model outputs, a few NCO, CDO and CDFTOOLS operations are needed to prepare the files before the interoperation tools:
		
* Get glamt and gphit from mesh file:
```
ncks -v glamt,gphit -o missvar.nc mesh_hgr_eNATL60MEDWEST_3.6.nc
ncwa  -a t missvar.nc missvar_cleaned.nc
```

* 	 Remove the gulf of Gascogne from the model outputs:
```
cdfbathy -file modelfile.nc  -var sossheig -zoom 1 243 655 803 -set_zone 32767 
```

* Append glam and gphit to the SSH model output file:
```
ncks -A missvar_cleaned.nc modelsshfile.nc
```

* You’ll also need to “cheat” on the time so that the model time correspond to the obs time. You can use `cdo` to switch time. For example:
```
cdo -shifttime,11years modelfilein.nc modelfileout.nc
```

* Remove other variables (nav_lon and nav_lat) otherwise the interpolation tool will go wrong:
```
ncks -4 -L4 -C -O -x  -v nav_lon,nav_lat modelfileout.nc modelsshfile_corrected.nc 
```
