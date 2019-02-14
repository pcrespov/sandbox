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



if [[ ${MY_BOOT_MODE} == "tooling" ]]
then
    MOUNT=$HOME
    #MOUNT=/wrong

    stat $MOUNT &> /dev/null || \
        (echo "ERROR: You must mount '$MOUNT' to deduce user and group ids" && exit 1) # FIXME: exit does not stop script

    USERID=$(stat -c %u $MOUNT)
    GROUPID=$(stat -c %g $MOUNT)

    # add host group to scu
    #addgroup -g $GROUPID hgrp
    #addgroup scu hgrp

    # scu == host user and group 
    deluser scu &> /dev/null
    addgroup -g $GROUPID scu
    adduser -u $USERID -G scu -D -s /bin/sh scu
    #chown -R scu:scu $HOME # FIXME: THIS TAKES TOO LONG!!
fi


# Appends docker group if socket is mounted
DOCKER_MOUNT=/var/run/docker.sock
stat $DOCKER_MOUNT &> /dev/null
if [[ $? -eq 0 ]]
then 
    GROUPID=$(stat -c %g $DOCKER_MOUNT)
    addgroup -g $GROUPID docker
    addgroup myu docker
fi

echo "Starting boot ..."
su-exec myu "$@"