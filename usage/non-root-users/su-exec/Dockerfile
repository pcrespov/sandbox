FROM alpine


RUN adduser -D -u 8004 scu
ENV HOME /home/scu


RUN apk add --no-cache \
      su-exec

RUN pip install --user --no-cache-dir aiohttp

VOLUME /home/scu/src/

ENTRYPOINT [ "/bin/sh", "entrypoint.sh" ]
CMD boot.sh
