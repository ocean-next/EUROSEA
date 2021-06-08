## Extracting alongtrack nadir SSH from eNATL60-no-tide in the EUROSEA target regions
Stephanie Leroux

* _What?_ 
  - Along-track sampling of the model SSH (eNATL60-no-tide) in the 2 subregions (MEDWEST and NANFL). 
  - The interpolation is made with the software Sosie (https://brodeau.github.io/sosie/) based on  the Akima interpolation method.
  - Each file is 6-month long:
  - In each file you’ll find:
    - sla_unfiltered (the real obs value (SLA)
    - sossheig (Sea Surface Height interpolated at all alongtrack locations)
    - sossheig_np (Sea Surface Height at nearest model grid point )

* _Data:_
Sampling of the model SSH along the satellite tracks of :
  - SENTINEL3A
    - From 2016-07-01 to 2016-12-31.
    - From 2017-01-01 to 2017-06-30.
  - SARAL (!! _Drifting Phase_ !!)
    - From 2016-07-01 to 2016-12-31 
    - From 2017-01-01 to 2017-06-30.
  - ENVISAT
    - From 2010-07-01 to 2010-12-31.
    - From 2011-01-01 to 2011-06-30.

* _Where to download the data:
  - https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/catalog/meomopendap/extract/Eurosea/pseudo-ssh-alongtrack/catalog.html

* _Note:_ `sossheig`  is the Sea Surface Height (SSH) as simulated by the  model. Keep in mind that the ocean model does not conserve mass with time (because of precipitation, etc. . . ). The spatial mean over the globe of the model SSH (or SLA) at any given time has thus no physical meaning, and can be removed before comparison with the real observed SLA (e.g. Greatbatch 1994).
