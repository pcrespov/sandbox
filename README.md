# dockerfiles

My curated collection of dockerfiles

## Good Practices

- If a service can run without privileges, use ``USER`` to change to a non-root user [[1]]. All our non-root users will be named ``scu``.

- To communicate with the docker daemon, the container's user need access to socket ``/var/run/docker.sock``. The latter is in the host's ``docker`` group so we must guarantee that a) the same group (and id) exists inside the container and b) container's user includes this group.

```bash
  # should be in docker-group
  ls -lah /var/run/docker.sock

  # displays uid and gids for user scu
  id scu  
```

[1]:https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#user