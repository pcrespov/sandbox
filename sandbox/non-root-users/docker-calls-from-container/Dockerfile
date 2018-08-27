# This demos how to have access to docker daemon from a non-root user 

FROM ubuntu:latest

ARG host_gid
ARG docker_gid=1001

RUN apt-get -qq update && \ 
    apt-get -qq -y install \
        curl

# installs docker API and creates group docker
RUN curl -fsSL get.docker.com -o get-docker.sh &&\ 
    sh get-docker.sh &&\
    rm get-docker.sh


# create a non-root user called `scu` with uid=8004 and corresponding group scu
#
# NOTE: the docker group uuid will correspond to the one created upon build
#       and does not necessarily correspond to the one at the host!
#       
RUN useradd --system --uid 8004 scu  &&\ 
    groupadd --system --gid ${docker_gid} --force docker &&\
    usermod -aG docker scu  &&\
    usermod -aG ${host_gid} scu


USER scu

WORKDIR /home/scu
VOLUME /home/scu
VOLUME /var/run/docker.sock


CMD ["docker", "ps"]

# $ id $UIDs

# rw-rw---- 1 root docker 0 Jun 18 08:17 /var/run/docker.sock