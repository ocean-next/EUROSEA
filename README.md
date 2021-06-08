# Ocean Next participation in H2020-EUROSEA
![H2020-EURSEA](./figs/logoEUROSEA.png)<br>

### This repo gathers the work that Stephanie Leroux and  Aurélie Albert @ Ocean Next  have done as part of Task 2.3 in the H2020-EUROSEA project.

* _What is H2020-EUROSEA?_<br>
H2020-EUROSEA is a project aiming at improving and integrating the European Ocean Observing and Forecasting System  (see official website: [https://eurosea.eu/](https://eurosea.eu/)). It has received funding from the European Union’s Horizon 2020  research and innovation programme under grant agreement No 862626).

* _Task2.3:_<br>
Task 2.3 of the project is dedicated to the __design of the Observing System Simulation Experiments (OSSEs) with multi-platform in situ data and impact on fine- scale structures__. Contributors to WP2.3 are CISC (Lead), IMT, MOI, CLS, SOCIB, Ocean Next, ENS. The OSSEs planned in Task 2.3 are further detailed in this public report: [ DOI: 10.3289/eurosea_d2.1](https://doi.org/10.3289/eurosea_d2.1)

* _Ocean Next contribution_<br>
Ocean Next has been in charge of preparing and making available some of the datasets (model outputs and pseudo-observations) based on the  existing eNATL60 simulation ([Brodeau et al, 2020](http://doi.org/10.5281/zenodo.4032732.)) in order to be used for the OSSEs. Two regions were selected, centered on two [SWOT crossovers](https://www.clivar.org/news/swot-%E2%80%98adopt-crossover%E2%80%99-consortium-has-been-endorsed-clivar) : West Mediterranean Sea (WESTMED) and North Atlantic (NANF), see Fig.1.  

![subregions](./figs/regions2.png)<br>
_Fig.1 The two subregions MEDWEST and NANF selected for Task 2.3, centered on  SWOT crossover._


### Datasets available(*) :

**Regional extractions of  the eNATL60 simulation (eNATL60-no-tide):**

- 2 subregions of about 15ºx10º  (WESTMED and NANFL) 
- 2D surface fields extracted:  SSH, SST, SSS, U, V, lon, lat
- Currents: U,V at 15 m and at the surface.
- Period: 1 year (between 1-july-2009 and 30-june-2010)
- Fields available at native resolution (1/60º, hourly) 
- Fields also available at downgraded resolution (1/20º, daily) 
- +(NEMO mask,mesh files to describe the model grid)

**Pseudo-obs  generated from the above model outputs and for the 2 subregions:**

- pseudo-SWOT (swath and nadir, both for the sampling and science phase) [More here],
- pseudo alongtrack SENTINEL3,  SARAL, ENVISAT [More here](),
- Lagrangian particles (pseudo-drifters) in the MEDWEST subregion [More here](),
