
import yarl
import docker

print("yarl: ", yarl.__version__)
print('docker:', docker.__version__)

cli = docker.from_env()
print("ping?:", cli.ping())
for i, image in enumerate(cli.images.list()):
    if image.tags:
        print(image.short_id, image.tags)
        if i>10:
            break