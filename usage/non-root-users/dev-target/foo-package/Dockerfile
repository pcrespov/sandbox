FROM python:3.6-alpine as base
LABEL maintainer=pcrespov

# Production user: uid=8004(myu) gid=8004(myu) groups=8004(myu)
RUN adduser -D -u 8004 -s /bin/sh -h /home/myu myu

RUN apk add --no-cache \
      su-exec

# All MY_ variables are customized
ENV MY_PIP pip3 --no-cache-dir
ENV MY_BUILD_TARGET base

EXPOSE 8080

# -------------------------- Build stage -------------------
# Installs build tools and third party dependencies
#
FROM base as build

ENV MY_BUILD_TARGET build

RUN apk add --no-cache \
      libc-dev

RUN $MY_PIP install --upgrade \
      pip \
      wheel \
      setuptools

# Installs base 3rd party packages to accelerate runtime installs
WORKDIR /build
COPY  foo-package/requirements/*.txt \
      foo-package/requirements/

RUN $MY_PIP install -r foo-package/requirements/base.txt &&\
    ls -la foo-package


# --------------------------Cache stage -------------------
# CI in master buils & pushes this target to speed-up image build
#
#  + /build        WORKDIR
#    + foo-package (copied myu:myu)
#
FROM build as cache
ENV MY_BUILD_TARGET cache

# copies it all (uses .dockerignore as filter)
WORKDIR /build
COPY --chown=myu:myu foo-package foo-package

RUN $MY_PIP install ./foo-package &&\
    $MY_PIP list



# --------------------------Production stage -------------------
# Final cleanup up to reduce image size and startup setup
# Runs as myu (non-root user)
#
#  + /home/myu     $HOME = WORKDIR
#    + foo-package 
#
FROM cache as production

ENV MY_BUILD_TARGET production
ENV MY_BOOT_MODE production

WORKDIR /home/myu

RUN mv /build/foo-package/docker docker &&\
    rm -rf /build

ENTRYPOINT [ "/bin/sh", "docker/entrypoint.sh" ]
CMD [ "/bin/sh", "docker/boot.sh"]


# --------------------------Development stage -------------------
# Source code accessible in host but runs in container
# Runs as myu with same gid/uid as host
#
#  + /devel         WORKDIR
#    + foo-package  (mounted volume)
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
