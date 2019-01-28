FROM alpine

# create user 'scu'
RUN adduser -D -u 8004 scu

RUN apk add --no-cache \
      su-exec

ENV HOME /home/scu

# --------------------------Development stage -------------------
ARG HOST_GID_ARG=1000

# install test 3rd party packages to accelerate runtime installs
COPY --chown=scu:scu services/web/server/requirements/tests.txt requirements-tests.txt
RUN $PIP install --no-cache-dir -r requirements-tests.txt

# in dev mode we give access to `scu` to host's mapped volumes
RUN addgroup -g $HOST_GID_ARG hgrp &&\
    addgroup scu hgrp && \
    chown -R scu:scu $HOME/.venv

VOLUME /home/scu/packages
VOLUME /home/scu/services/web/server/
VOLUME /home/scu/services/web/client/

ENV SIMCORE_WEB_CONFIG development
ENV DEBUG 1
ENTRYPOINT [ "/bin/sh", ".docker/entrypoint.sh" ]
CMD boot.sh
