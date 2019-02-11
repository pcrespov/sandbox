#!/bin/sh

# This entrypoint script:
#
# - Executes with root privileges *inside* of the container upon start
# - Allows starting the container as root to perform some root-level operations at runtime
#  (e.g. on volumes mapped inside)
# - Notice that this way, the container *starts* as root but *runs* as scu (non-root user)
#
# See https://stackoverflow.com/questions/39397548/how-to-give-non-root-user-in-docker-container-access-to-a-volume-mounted-on-the


WHO=/tim


stat $WHO > /dev/null || \
    (echo You must mount a file to "$WHO" in order to deduce the user &&\
     exit 1 )


# Idenfifies host's user and group id
USERID=$(stat -c %u $WHO)
GROUPID=$(stat -c %g $WHO)

deluser scu > /dev/null 2>&1
addgroup -g $GROUPID scu
adduser -u $USERID -G scu -D -s /bin/sh scu

# in dev mode we give access to `scu` to host's mapped volumes
#RUN addgroup -g $HOST_GID_ARG hgrp &&\
#    addgroup scu hgrp && \
#    chown -R scu:scu $HOME/.venv


su-exec scu "$@"
