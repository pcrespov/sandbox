#!/bin/sh

# This entrypoint script:
#
# - Executes with root privileges *inside* of the container upon start
# - Allows starting the container as root to perform some root-level operations at runtime
#  (e.g. on volumes mapped inside)
# - Notice that this way, the container *starts* as root but *runs* as scu (non-root user)
#
# See https://stackoverflow.com/questions/39397548/how-to-give-non-root-user-in-docker-container-access-to-a-volume-mounted-on-the

echo "Entrypoint for stage ${MY_BUILD_TARGET} ..."
echo "  User    :`id $(whoami)`"
echo "  Workdir :`pwd`"


if [[ ${MY_BUILD_TARGET} == "development" ]]
then
    MOUNT=/home/scu/foo-package
    #MOUNT=/wrong

    stat $MOUNT &> /dev/null || \
        (echo "ERROR: You must mount '$MOUNT' to deduce user and group ids" && exit 1) # FIXME: exit does not stop script

    USERID=$(stat -c %u $MOUNT)
    GROUPID=$(stat -c %g $MOUNT)

    addgroup -g $GROUPID hgrp
    addgroup scu hgrp
fi


# Appends docker group if socket is mounted
DOCKER_MOUNT=/var/run/docker.sock
stat $DOCKER_MOUNT &> /dev/null
if [[ $? -eq 0 ]]
then 
    GROUPID=$(stat -c %g $DOCKER_MOUNT)

    addgroup -g $GROUPID docker
    addgroup scu docker
fi

echo "Starting boot ..."
su-exec scu "$@"