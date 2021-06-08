## Extracting  alongtrack nadir SSH pseudo-observations in the EUROSEA target regions

* _What?_ 
  - Along-track pseudo-observation (SSH) from the simulation eNATL60-BLB002, extracted on the 2 subregions (MEDWEST and NANFL). 
  - The interpolation is made with the software Sosie (https://brodeau.github.io/sosie/) based on  the Akima interpolation method.

* _Where to download data:
  - https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/catalog/meomopendap/extract/Eurosea/pseudo-ssh-alongtrack/catalog.html

* _Data:_
  - Each file is 6-month long:
  - In each file you’ll find:
sla_unfiltered (the real obs value (SLA)
sossheig (Sea Surface Height interpolated at all alongtrack locations)
sossheig_np (Sea Surface Height at nearest model grid point )

Pseudo-SENTINEL3A
From 2016-07-01 to 2016-12-31.
From 2017-01-01 to 2017-06-30.

Pseudo-SARAL
From 2016-07-01 to 2016-12-31 (
From 2017-01-01 to 2017-06-30.

Pseudo-ENVISAT
From 2010-07-01 to 2010-12-31.
From 2011-01-01 to 2011-06-30.

* _Notes:_ Sossheig  is the Sea Surface Height (SSH) as simulated by the  model. Keep in mind that the ocean model does not conserve mass with time (because of precipitation, etc. . . ). The spatial mean over the globe of the model SSH (or SLA) at any given time has thus no physical meaning, and can be removed before comparison with the real observed SLA (e.g. Greatbatch 1994).
