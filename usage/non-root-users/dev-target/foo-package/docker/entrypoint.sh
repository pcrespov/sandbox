#!/bin/sh

# This entrypoint script:
#
# - Executes with root privileges *inside* of the container upon start
# - Allows starting the container as root to perform some root-level operations at runtime
#  (e.g. on volumes mapped inside)
# - Notice that this way, the container *starts* as root but *runs* as myu (non-root user)
#
# See https://stackoverflow.com/questions/39397548/how-to-give-non-root-user-in-docker-container-access-to-a-volume-mounted-on-the

echo "Entrypoint for stage ${MY_BUILD_TARGET} ..."
echo "  User    :`id $(whoami)`"
echo "  Workdir :`pwd`"


if [[ ${MY_BUILD_TARGET} == "development" ]]
then
    # Takes user/group ids of host
    #
    # NOTE: image files with old id permissions will remain
    # TODO: rename myu as USER's

    # NOTE: expects docker run ... -v $(pwd):/devel/foo-package
    DEVEL_MOUNT=/devel/foo-package

    stat $DEVEL_MOUNT &> /dev/null || \
        (echo "ERROR: You must mount '$DEVEL_MOUNT' to deduce user and group ids" && exit 1) # FIXME: exit does not stop script

    USERID=$(stat -c %u $DEVEL_MOUNT)
    GROUPID=$(stat -c %g $DEVEL_MOUNT)

    deluser myu &> /dev/null
    addgroup -g $GROUPID myu
    adduser -u $USERID -G myu -D -s /bin/sh myu
fi


# Appends docker group if socket is mounted
DOCKER_MOUNT=/var/run/docker.sock
stat $DOCKER_MOUNT &> /dev/null
if [[ $? -eq 0 ]]
then
    GROUPID=$(stat -c %g $DOCKER_MOUNT)
    GROUPNAME=docker

    addgroup -g $GROUPID $GROUPNAME
    if [[ $? -gt 0 ]]
    then
        # if group already exists in container, then reuse name
        GROUPNAME=$(getent group ${GROUPID} | cut -d: -f1)
    fi
    addgroup myu $GROUPNAME
fi

echo "Starting boot ..."
su-exec myu "$@"