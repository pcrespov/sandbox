 
# Demonstrates
#
#
#
#
# check host's user and its groups
id $GUID

docker build -t test .

docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -u root test


# build
 -f-<<EOF
FROM ubuntu:latest
# create a non-root user called `scm` with uid=8004 and corresponding group scu
RUN useradd --system --uid 8004 --shell /bin/bash scu
USER scu
CMD ["sleep", "infinity"]
EOF

# run test
OUTPUT="$(docker run -d test)"

echo
# check that container runs with uid 8004
ps aux | grep sleep

echo
# inside as well but mapped into scu name
docker exec $OUTPUT /bin/bash -c "ps aux"

# stops
docker stop $OUTPUT
docker rm $OUTPUT


echo "Starts with uid=${UID} ---------------------------------------------"
OUTPUT="$(docker run -d --user ${UID} ubuntu:latest sleep infinity)"

echo
# check that container runs with uid 8004
ps aux | grep sleep

echo
# inside as well but mapped into scu name
docker exec $OUTPUT /bin/bash -c "ps aux"

# docker exec $OUTPUT /bin/bash --> shows "I have no name!@xxx:/$"

docker stop $OUTPUT
docker rm $OUTPUT





