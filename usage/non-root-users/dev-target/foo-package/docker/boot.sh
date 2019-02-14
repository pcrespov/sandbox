#!/bin/sh

# BOOT ---------------------------------------------
echo "Booting in ${MY_BOOT_MODE} mode ..."
echo "  User    :`id $(whoami)`"
echo "  Workdir :`pwd`"
if [[ ${MY_BOOT_MODE} == "development" ]]
then 
    ls -la | sed 's/^/    /'
    # WARNING: might show secrets in logs
    echo "  Environment :" 
    printenv  | sed 's/=/: /' | sed 's/^/    /' | sort
fi

if [[ ${MY_BOOT_MODE} == "development" ]]
then     
    cd /devel/foo-package
    $MY_PIP install -e .
fi


echo "  Python :" 
python --version | sed 's/^/    /'
which python | sed 's/^/    /'
echo "  PIP :" 
$MY_PIP list | sed 's/^/    /'



# RUNNING application ----------------------------------------
echo "Running application ..."
python -c "import foo; print(foo.__file__)"