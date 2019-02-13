#!/bin/sh

# Runs as SCU user ---------------------------------------------
echo "Booting in ${MY_BUILD_TARGET} mode ..."
echo "Activating python virtual env..."
source $HOME/.venv/bin/activate

echo "  User    :`id $(whoami)`"
echo "  Workdir :`pwd`"
printenv  | sed 's/=/: /'
