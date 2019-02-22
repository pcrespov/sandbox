#!/bin/sh 

echo "Entrypoint for stage ${MY_BUILD_TARGET} ..."
echo "  User    :`id $(whoami)`"
echo "  Workdir :`pwd`"

# already exists
USER=myu
DEVEL_MOUNT=/devel/foo-package

# group and user ids
USERID=$(stat -c %u $DEVEL_MOUNT)
GROUPID=$(stat -c %g $DEVEL_MOUNT)
GROUP=$(getent group ${GROUPID} | cut -d: -f1)

if [[ -z "$GROUP" ]]
then
	GROUP=myu

	echo deluser $USER &> /dev/null
	echo addgroup -g $GROUPID $GROUP
	echo adduser -u $USERID -G $GROUP -D -s /bin/sh $USER
else
	addgroup $USER $GROUP
fi


echo su-exec $USER
