#
#
# https://docker-py.readthedocs.io/en/stable/
#

import docker
import logging

logging.basicConfig(level=logging.DEBUG)
_LOGGER = logging.getLogger(__name__)

if __name__ == "__main__":
    client = docker.from_env()

    # ``docker image ls``
    images = client.images.list(all=False)
    _LOGGER.info("Images in host %d:\n\t-%s", \
        len(images), \
        "\n\t- ".join(map(str, images)) )

    # ``docker ps``
    containers = client.containers.list()
    _LOGGER.info("Containers running in host %d:\n\t-%s", \
        len(containers), \
        "\n\t- ".join(map(str, containers)) )

    # request to log into masu
    res = client.login(registry="masu.speag.com/v2", username="z43", password="z43")
    _LOGGER.info("client.login->%s", res)
    