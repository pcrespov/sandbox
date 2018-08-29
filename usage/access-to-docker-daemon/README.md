# Access to docker daemon

How to communicate with a docker daemon from a container running with a non-root user

## Problem: client calls using docker-sdk

- install python-based [docker-sdk] in a virtualenv inside of the docker
- run a simple script that does something like ``docker ps``
- container runs with ``scu`` user (non-root)

#### Trials

- invalid docker gid argument ``DOCKER_GID_ARG`` -> fails to communicate via socket
- 

#### Solution

- bind socket as volume ``/var/run/docker.sock:/var/run/docker.sock``
- add ``scu`` to ``docker`` group. The latter needs to have **the same gid** as in the host, therefore we pass it as an Dockerfile argument at build time

[docker-sdk]:https://docker-py.readthedocs.io/en/stable/