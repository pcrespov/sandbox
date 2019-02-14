
import yarl
import docker

print("yarl: ", yarl.__version__)
print('docker:', docker.__version__)

cli = docker.from_env()
print("ping?:", cli.ping())
for image in cli.images.list():
    print(image.short_id, image.tags)