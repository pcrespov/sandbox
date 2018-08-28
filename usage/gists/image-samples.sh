#!/bin/bash

# FILTERING
# https://docs.docker.com/engine/reference/commandline/images/#filtering
docker image ls --filter=reference='qx:*'

docker image ls -f reference='qx'

# Erase
docker image rm $(docker image ls -f reference='qx' -aq)