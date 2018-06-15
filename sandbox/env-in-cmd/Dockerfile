FROM ubuntu

ENV FOO "/path/to/foo"

COPY test.sh .
RUN chmod +x test.sh

#CMD ["/bin/bash", "-c", "./test.sh --opath=${FOO}"]
CMD ["/bin/bash", "-c", "./test.sh \
    --opath=${FOO} \
    --arg2=val2 \
    --arg3 val3 \
    "]
