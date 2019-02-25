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

USERNAME=myu

if [[ ${MY_BUILD_TARGET} == "development" ]]
then
    # myu takes host's user/group identity except in the case of root,
    # in which it adds only group
    
    # NOTE: image files with old id permissions will remain
    # NOTE: expects docker run ... -v $(pwd):/devel/foo-package
    DEVEL_MOUNT=/devel/foo-package

    stat $DEVEL_MOUNT &> /dev/null || \
        (echo "ERROR: You must mount '$DEVEL_MOUNT' to deduce user and group ids" && exit 1) # FIXME: exit does not stop script

    USERID=$(stat -c %u $DEVEL_MOUNT)
    GROUPID=$(stat -c %g $DEVEL_MOUNT)
    GROUPNAME=$(getent group ${GROUPID} | cut -d: -f1)

    if [[ $USERID -eq 0 ]]
    then
        addgroup $USERNAME root
    else
        # take host's credentials in myu
        if [[ -z "$GROUPNAME" ]]
        then
            GROUPNAME=myu
            addgroup -g $GROUPID $GROUPNAME
        else
            addgroup $USERNAME $GROUPNAME
        fi

        deluser $USERNAME &> /dev/null
        adduser -u $USERID -G $GROUPNAME -D -s /bin/sh $USERNAME
    fi
fi


# Appends docker group if socket is mounted
DOCKER_MOUNT=/var/run/docker.sock
stat $DOCKER_MOUNT &> /dev/null
if [[ $? -eq 0 ]]
then
    GROUPID=$(stat -c %g $DOCKER_MOUNT)
    GROUPNAME=docker

    addgroup -g $GROUPID $GROUPNAME &> /dev/null
    # if GROUPID already in use, then reuse name
    if [[ $? -gt 0 ]]
    then
        GROUPNAME=$(getent group ${GROUPID} | cut -d: -f1)
    fi
    addgroup $USERNAME $GROUPNAME
fi

echo "Starting boot ..."
su-exec $USERNAME "$@"