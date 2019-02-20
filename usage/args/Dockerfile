FROM ubuntu:latest

ARG VCS_REF
ARG VCS_REF_CLIENT

#ARG bdir=argdir
ENV bdir=envdir

COPY test.sh $bdir/
RUN chmod +x $bdir/test.sh

RUN /bin/bash ${bdir}/test.sh \
        --set osparc.vcsRef="$VCS_REF" \
        --set osparc.vcsRefClient=$VCS_REF_CLIENT


#CMD ["/bin/bash", "-c", "./test.sh --opath=${FOO}"]
CMD ["/bin/bash", "-c", "${bdir}/test.sh \
    --opath=${FOO} \
    --arg2=val2 \
    --arg3 val3 \
    --set osparc.vcsRef=\"${VCS_REF}\" \
    --set osparc.vcsRefClient=\"${VCS_REF_CLIENT}\" \
    "]
