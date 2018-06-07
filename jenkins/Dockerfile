FROM jenkins:2.32.3

# Fromt thread https://github.com/jenkinsci/docker/issues/263

#
# docker build -t jenkins_docker .
# docker run --rm -p 8080:8080 -p 4040:4040 -v /var/run/docker.sock:/var/run/docker.sock jenkins_docker
#

USER root
RUN apt-get -qq update \
  && apt-get -qq -y install \
  curl

# Creates group and add
# There is no need to install. Can bind-mount the docker bin outside:
#
#docker run -d \
#  -v /var/run/docker.sock:/var/run/docker.sock \
#  -v $(which docker):/usr/bin/docker:ro \
#  -v /lib64/libdevmapper.so.1.02:/usr/lib/x86_64-linux-gnu/libdevmapper.so.1.02 \
#  -v /lib64/libudev.so.0:/usr/lib/x86_64-linux-gnu/libudev.so.0 \
#  -p 8080:8080 \
#  --name jenkins \
#  --privileged=true -t -i \
#  test/jenkins
#
#
RUN curl -sSL https://get.docker.com/ | sh

RUN usermod -a -G docker jenkins

USER jenkins

CMD /bin/bash


# Adds dynamically same docker group id as in host
#
# https://github.com/jenkinsci/docker/issues/263 see entry by brthor!
#
#FROM jenkins:2.7.1
#USER 0
#CMD DOCKER_GID=$(stat -c '%g' /var/run/docker.sock) && \
#  groupadd -for -g ${DOCKER_GID} docker && \
#  usermod -aG docker jenkins && \
#  sudo -E -H -u jenkins bash -c /usr/local/bin/jenkins.sh
