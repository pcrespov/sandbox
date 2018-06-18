# This demos how to have access to docker daemon from a non-root user 

FROM ubuntu:latest

RUN apt-get -qq update && \ 
    apt-get -qq -y install \
        curl

# installs docker API and creates group docker
RUN curl -sSL https://get.docker.com/ | sh

# create a non-root user called `scm` with uid=8004 and corresponding group scu
#
# NOTE: the docker group uuid will correspond to the one created upon build
#       and does not necessarily correspond to the one at the host!
#       
RUN useradd --system --uid 8004 scu  &&\ 
    usermod -aG docker scu

USER scu

VOLUME /home/scu
VOLUME /var/run/docker.sock

CMD ["docker", "ps"]

# $ id $UIDs

# rw-rw---- 1 root docker 0 Jun 18 08:17 /var/run/docker.sock