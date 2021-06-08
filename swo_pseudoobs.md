# Extracting  pseudo-SWOT observations  from eNATL60-no-tide in the EUROSEA target regions 

Aurélie Albert

In collaboration with M. Ballarota (CLS), the latest version of the SWOT Simulator (https://github.com/CNES/swot_simulator) was applied on eNATL60-BLB002 outputs (run without tides). 
Two different configurations of SWOT have been applied for the period of eNATL60 01/07/2009-30/06/2010 : the calval phase (fast-sampling) and the science phase (see Fig.1 and 2).

For each region, the files for the  calval phase and the science phase are in distinct directories. Then for each phase, karin and nadir data are in distinct directories. 

For karin data there are two dimensions : num_pixels (cross track) and num_lines (along track). The variables are ssh_karin, err_timing, err_roll, err_baseline_dilatation, err_phase, err_karin, err_wet_troposphere and ssh_karin_true (no errors).
See https://swot-simulator.readthedocs.io/en/latest/errors.html for  a description of the errors.

For nadir data, there is only num_lines dimension (no cross track). The variables are ssh_nadir, err_altimeter, err_wet_troposphere and ssh_nadir_true (no errors).


![subregions](./figs/regions4.png)<br>
_Fig.1 The calval phase (fast-sampling) : repeating trajectories_

![subregions](./figs/regions5.png)<br>
_Fig.2 The science phase : full coverage_
