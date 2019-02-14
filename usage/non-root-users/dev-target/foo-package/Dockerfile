FROM python:3.6-alpine as base
LABEL maintainer=pcrespov

# Production user: uid=8004(myu) gid=8004(myu) groups=8004(myu)
RUN adduser -D -u 8004 -s /bin/sh -h /home/myu myu

RUN apk add --no-cache \
      su-exec

# The idea is to mount build-context onto $HOME
ENV HOME /home/myu

# All MY_ variables are customized
#ENV MY_PIP  $HOME/.venv/bin/pip3 --no-cache-dir
ENV MY_PIP pip3 --no-cache-dir
ENV MY_BUILD_TARGET base

EXPOSE 8080

# WORKDIR /home/myu

# copies from build-context to workdir/
# Should copy ONLY stuff that is needed to build the image
#COPY --chown=myu:myu \
#      foo-package/docker \
#      foo-package/docker

#RUN ls -la foo-package && echo "asdf"


# -------------------------- Build stage -------------------
FROM base as build

ENV MY_BUILD_TARGET build

RUN apk add --no-cache \
      libc-dev

#RUN python3 -m venv $HOME/.venv &&\
RUN $MY_PIP install --upgrade \
      pip \
      wheel \
      setuptools




# install base 3rd party packages to accelerate runtime installs
WORKDIR /build
COPY  foo-package/requirements/*.txt \
      foo-package/requirements/

RUN $MY_PIP install -r foo-package/requirements/base.txt &&\
    ls -la foo-package


# --------------------------Cache stage -------------------
# CI in master buils & pushes this target to speed-up image build
#
FROM build as cache
ENV MY_BUILD_TARGET cache

# copies it all
WORKDIR /build
COPY foo-package foo-package

RUN $MY_PIP install ./foo-package &&\
    $MY_PIP list



# --------------------------Production stage -------------------
# Final cleanup up to reduce image size and startup setup
#
FROM cache as production

ENV MY_BUILD_TARGET production
ENV MY_BOOT_MODE production

WORKDIR /home/myu

RUN mv /build/foo-package/docker docker &&\
    chown myu:myu docker &&\
    rm -rf /build

ENTRYPOINT [ "/bin/sh", "docker/entrypoint.sh" ]
CMD [ "/bin/sh", "docker/boot.sh"]


# --------------------------Development stage -------------------
# Source code accessible in host but runs in container
#
FROM build as development

ENV MY_BUILD_TARGET development
ENV MY_BOOT_MODE development


# Reuse what was built
WORKDIR /build
RUN $MY_PIP install -r foo-package/requirements/dev.txt

WORKDIR /devel
VOLUME /devel

ENTRYPOINT [ "/bin/sh", "foo-package/docker/entrypoint.sh" ]
CMD [ "/bin/sh", "foo-package/docker/boot.sh"]
