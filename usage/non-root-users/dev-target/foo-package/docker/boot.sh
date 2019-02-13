#!/bin/sh

# Runs as SCU user ---------------------------------------------
echo "Booting in ${MY_BOOT_MODE} mode ..."
echo "Activating python virtual env..."
source $HOME/.venv/bin/activate

echo "  User    :`id $(whoami)`"
echo "  Workdir :`pwd`"

if [[ ${MY_BOOT_MODE} == "development" ]]
then 
    # WARNING: might show secrets in logs
    echo "  Environment :" 
    printenv  | sed 's/=/: /' | sed 's/^/    /' | sort
fi


if [ ${MY_BOOT_MODE} == "development" ]
    
then 
