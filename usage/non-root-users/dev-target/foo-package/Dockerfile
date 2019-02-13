FROM python:3.6-alpine as base
LABEL maintainer=pcrespov

# uid=8004(scu) gid=8004(scu) groups=8004(scu)
RUN adduser -D -u 8004 -s /bin/sh scu

RUN apk add --no-cache \
      su-exec

# The idea is to mount build-context onto $HOME
ENV HOME /home/scu
ENV MY_PIP  /home/scu/.venv/bin/pip3 --no-cache
ENV MY_BUILD_TARGET base

EXPOSE 8080

WORKDIR /home/scu

# copies from build-context to workdir/
# Should copy ONLY stuff that is needed to build the image
#COPY --chown=scu:scu \
#      foo-package/docker \
#      foo-package/docker

#RUN ls -la foo-package && echo "asdf"


# -------------------------- Build stage -------------------
FROM base as build

ENV MY_BUILD_TARGET build

RUN apk add --no-cache \
      libc-dev

RUN python3 -m venv $HOME/.venv &&\
    $MY_PIP install --upgrade \
      pip \
      wheel \
      setuptools


# install base 3rd party packages to accelerate runtime installs
#
COPY --chown=scu:scu \
      foo-package/requirements/*.txt \
      foo-package/requirements/

RUN $MY_PIP install -r foo-package/requirements/base.txt &&\
    ls -la foo-package


# --------------------------Cache stage -------------------
# CI in master buils & pushes this target to speed-up image build
#
FROM build as cache
ENV MY_BUILD_TARGET cache

# copies it all
COPY --chown=scu:scu \
      foo-package \
      $HOME/foo-package

WORKDIR /home/scu/foo-package
RUN $MY_PIP install . &&\
    $MY_PIP list



# --------------------------Production stage -------------------
# Final cleanup up to reduce image size and startup setup
#
FROM cache as production

WORKDIR /home/scu

RUN rm -rf $HOME/foo-package/src &&\
    rm -f $HOME/foo-package/**.py

ENV MY_BUILD_TARGET production
ENV MY_BOOT_MODE production

ENTRYPOINT [ "/bin/sh", "foo-package/docker/entrypoint.sh" ]
CMD [ "/bin/sh", "foo-package/docker/boot.sh"]


# --------------------------Development stage -------------------
# Source code accessible in host but runs in container
#
FROM build as development

WORKDIR /home/scu/foo-package
RUN $MY_PIP install -r requirements/dev.txt


WORKDIR /home/scu
VOLUME /home/scu/foo-package

ENV MY_BUILD_TARGET development
ENV MY_BOOT_MODE development

ENTRYPOINT [ "/bin/sh", "foo-package/docker/entrypoint.sh" ]
CMD [ "/bin/sh", "foo-package/docker/boot.sh"]
