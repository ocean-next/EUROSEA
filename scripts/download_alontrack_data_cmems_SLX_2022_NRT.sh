#!/bin/bash
# inspired from Laurent Brodeau's script
## DEPENDENCIES: python 2.7, motuclient (python), and NCO to be installed !

# Your CMEMS credentials
# => "https://resources.marine.copernicus.eu/?option=com_csw&task=results?option=com_csw&view=account"
USER_CMEMS='xxxxxxxxxxx'
PASS_CMEMS='xxxxxxxxxxx'

# Where to save on your computer:
DIR_SAVE="xxxxxxxxxxxxxxxxx"
############################ end of "safe" user configuration ###############################


if [ "${5}" = "" ]; then
    echo
    echo "USAGE: `basename ${0}` <satellite_name> <YEAR1> <MMDD1> <YEAR2> <MMDD2>"
    echo
    echo "     * currently supported satellites => 'jason3' only. More soon"
    echo
    exit
fi

sat="${1}"
YEAR1="${2}"
DT1="${3}"
YEAR2="${4}"
DT2="${5}"

cm1=`echo ${DT1} | cut -c1-2`
cm2=`echo ${DT2} | cut -c1-2`
cd1=`echo ${DT1} | cut -c3-4`
cd2=`echo ${DT2} | cut -c3-4`

h1="00:00:00" ; h2="23:59:59" ; # Begining and end of a day...


case ${sat} in
    "jason3") NAME="JASON3"
                SID="SEALEVEL_GLO_PHY_L3_NRT_OBSERVATIONS_008_044-DGF"
                PID="dataset-duacs-nrt-global-j3-phy-l3"
                ;;
    *) echo
       echo " PROBLEM: Satellite ${sat} is unknown!"
       echo; exit
       ;;
esac


VAR2KEEP="time,latitude,longitude,cycle,track,sla_unfiltered,mdt" ; # variables to keep from original downloaded files...

f2d="${NAME}_${YEAR1}${cm1}${d1}-${YEAR2}${cm2}${d2}.zip"

dsave="${DIR_SAVE}/${NAME}" ; mkdir -p ${dsave}

# Final file to create:
FILE_SAT="${dsave}/${NAME}_${YEAR1}${cm1}${d1}-${YEAR2}${cm2}${d2}.nc"


############################################
# Download and generate the satellite data #
###########################################

if [ ! -f ${FILE_SAT} ]; then

    dir_tmp=${dsave}/tmp
    mkdir -p ${dir_tmp}
    cd ${dir_tmp}/

    if [ ! -f ./${f2d} ]; then
        # Need to download and unzip the archive

        python2 -m motuclient --motu http://nrt.cmems-du.eu/motu-web/Motu \
               --service-id ${SID} \
               --product-id ${PID} \
               --date-min "${YEAR1}-${cm1}-${d1} ${h1}" --date-max "${YEAR2}-${cm2}-${d2} ${h2}" \
               --out-dir ${dir_tmp} --out-name ${f2d} \
               --user ${USER_CMEMS} --pwd ${PASS_CMEMS}

        unzip -o ${f2d}

    fi

    # Need treatment:
    list=`\ls *.nc`

    for ff in ${list}; do

        echo

        fu=`echo ${ff} | sed -e s/'.nc'/'_unpacked.tmp'/g` ; # Name of unpacked file!
        fn=`echo ${ff} | sed -e s/'.nc'/'_tr.tmp'/g`       ; # Name of file with an UNLIMITED time record

        echo "${ff} -> ${fu} -> ${fn}"; echo

        # Unpacking first for safety! => otherwize lon and lat are screwed up!
        if [ ! -f ${fu} ]; then
            ncrename -v longitude,vxx -v latitude,vyy ${ff}
            ncpdq -U ${ff} -o ${fu}
            echo ; echo " *** Unpacked ${ff} into ${fu} !!!"; echo
            ncrename -v vxx,longitude -v vyy,latitude ${fu}
            rm -f ${fn}
        fi

        if [ ! -f ${fn} ]; then
            ncecat -O ${fu} ${fn}     # Add degenerate record dimension named "record"
            echo ; echo
            ncpdq -O -a time,record ${fn} ${fn} # Switch "record" and "time"
            echo ; echo
            ncwa -O -a record ${fn} ${fn}       # Remove (degenerate) "record"
            echo ; echo
        fi

        #if [ ! -f ${fn}4 ]; then
        #    ncks -4 -L 5 --cnk_dmn time_counter,2000 ${fn} -o ${fn}4
        #fi

    done


    CMD="ncrcat -O -h -v ${VAR2KEEP} *_tr.tmp -o ${FILE_SAT}"
    echo; echo " *** ${CMD}"; ${CMD};

    cd ${dsave}/

    rm -rf ./tmp/*.nc ./tmp/*.tmp

else
    echo
    echo " File ${FILE_SAT} is already here! (`pwd`)"
    echo
fi
