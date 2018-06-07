FROM node:8.9.2 as base-stage

LABEL maintainer=pcrespov

#
#
# docker build -t test .
# docker run -it -v $(pwd):/home/scu/mount test
#
#

#
# [1]:https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#user
# [2]: https://docs.docker.com/engine/reference/builder/#user
# - https://stackoverflow.com/questions/24308760/running-app-inside-docker-as-non-root-user
#

# USERS and OWNERSHIP
#
# According to [1], if a service can run without privileges, use ``USER`` to 
# change to a non-root user.
#
# USER sets the user when running the image and for any RUN, CMD and ENTRYPOINT 
# instructions that follow it in the Dockerfile [2]
#
#
# Now, when running the container, the owner of mounted directories change:
#
# Mounted volumes get associated to user with the same UID as host. 
# If not mounted, they get associated to root.
# If no user with same id, then it is assigned to root.
#
#
# User id of host:
# - Usually, the user id for users created on Linux systems now starts from 1000. 
# On Fedora/CentOS systems it used to be from 500. It is specified in 
#/etc/login.defs file. So, a user with uid 1000 is the first normal user 
# (non-root user) created on the system. Or if your system starts giving uid 
# from 500, then another non-root (non administrator) user with uid 1000.
#
#
# Conclusion:
#
#  - user and relevant groups (e.g. docker) ouside and inside the docker MUST
#   have the same id number
#
#
#
#
#

#RUN apt-get -qq update \
#    && apt-get -qq -y install \
#    curl

#RUN curl -sSL https://get.docker.com/ | sh

# (1) new non-root user
#RUN userdel --force node
#RUN groupadd --gid 1000 scu && \
#    useradd --comment "simcore user" --uid 1000 --gid scu --shell /bin/bash --create-home scu

# (2) rename node as 'scu'
# base image comes with a pre-defined non-root node:node with id=1000. We reuse it
RUN groupmod --new-name scu node && \
    usermod --login scu --move-home --home /home/scu node

# https://stackoverflow.com/questions/36185035/how-to-mount-docker-socket-as-volume-in-docker-container-with-correct-group
# docker build --build-arg DOCKER_GROUP_ID=`getent group docker | cut -d: -f3` -t my-jenkins-image .

#ARG DOCKER_GROUP_ID=1001

# the docker group inside  the container ends up having the same group id as the
#  docker group outside of  the container. You can do this using build arguments 
# for your docker build:
# docker build --build-arg DOCKER_GROUP_ID=`getent group docker | cut -d: -f3` -t my-jenkins-image .

# 
#USER root
#RUN curl -o /root/docker.tgz https://get.docker.com/builds/Linux/x86_64/docker-1.12.5.tgz && \
#    tar -C /root -xvf /root/docker.tgz && \
#    mv /root/docker/docker /usr/local/bin/docker && \
#    rm -rf /root/docker*
#RUN curl -L https://github.com/docker/compose/releases/download/1.7.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \
#    chmod +x /usr/local/bin/docker-compose
#RUN groupadd -g $DOCKER_GROUP_ID docker && gpasswd -a scu docker
#RUN groupadd -for -g ${DOCKER_GROUP_ID} docker && gpasswd -a scu docker

#RUN gpasswd -a scu docker

USER scu
ENV HOME /home/scu


# These get created as scu
RUN mkdir /home/scu/wkdir && \
    mkdir /home/scu/mount && \
    touch /home/scu/wkdir/foo
#    chown -R scu:scu /home/scu

# copies defaults to root
COPY --chown=scu:scu . /home/scu/wkdir/

WORKDIR /home/scu/wkdir

VOLUME /home/scu/mount
VOLUME /var/run/docker.sock

#CMD DOCKER_GID=$(stat -c '%g' /var/run/docker.sock) && \
#    groupadd -for -g ${DOCKER_GID} docker && \
#    usermod -aG docker scu && \
#    /bin/bash

CMD /bin/bash
