#!/usr/bin/env sh

WHO=/tim

stat $WHO > /dev/null || (echo You must mount a file to "$WHO" in order to properly assume user && exit 1)

# Idenfifies host's user and group id
USERID=$(stat -c %u $WHO)
GROUPID=$(stat -c %g $WHO)

deluser tim > /dev/null 2>&1
addgroup -g $GROUPID tim
adduser -u $USERID -G tim -D -s /bin/sh tim

gosu tim "$@"
