## Download the along-track observation files from CMEMS website:

* Info: https://resources.marine.copernicus.eu/product-detail/SEALEVEL_GLO_PHY_L3_NRT_OBSERVATIONS_008_044/INFORMATION

* Data downloaded using the script [`download_alontrack_data_cmems_SLX_2022_NRT.sh`](https://github.com/ocean-next/EUROSEA/blob/main/scripts/download_alontrack_data_cmems_SLX_2022_NRT.sh). The same script also unzips and concatenates the data, and make the time dimension a record dimension (DEPENDENCIES: python 2.7, motuclient (python), and NCO to be installed). You need to put your own CMEMS id and login in the script of course. 
* Usage:  
```./download_alontrack_data_cmems_SLX_2022_NRT.sh <satellite> <year1> <MM1DD1> <year2> <MM2DD2>
```
* I downloaded only 6 months at a time otherwise the files are too big to process. Usage: 
```
./download_alontrack_data_cmems.sh jason3 2016 0701 2017 0101
./download_alontrack_data_cmems.sh jason3 2017 0101 2017 0701
```

* Note:  the script is ready to download `jason3` data for now. Other satelites will be added soon from the available list here: https://resources.marine.copernicus.eu/product-detail/SEALEVEL_GLO_PHY_L3_NRT_OBSERVATIONS_008_044/INFORMATION
