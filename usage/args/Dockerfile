FROM ubuntu:latest

#ARG bdir=argdir
ENV bdir=envdir

COPY test.sh $bdir/
RUN chmod +x $bdir/test.sh

#CMD ["/bin/bash", "-c", "./test.sh --opath=${FOO}"]
CMD ["/bin/bash", "-c", "./test.sh \
    --opath=${FOO} \
    --arg2=val2 \
    --arg3 val3 \
    "]
