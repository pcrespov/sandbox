FROM alpine:latest

RUN adduser -D -u 8004 scu

WORKDIR /home/scu

# All these copy *content* of ``folder`` in cwd
#COPY --chown=scu:scu folder .
#COPY --chown=scu:scu folder/ .
#COPY --chown=scu:scu folder ./

COPY --chown=scu:scu folder folder
COPY --chown=scu:scu folder here
COPY --chown=scu:scu folder/ there/

CMD ["/bin/sh", "-c", "ls"]