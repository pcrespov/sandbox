# non-root users

In [[1]] we find a good synthesis of how uids work between containers and hosts. Some important points:

- The linux kernel manages the uid/gid and kenrel-level syscalls are used to determine access privileges
- Both the host and containers run on the same kernel, therefore the entire world of uid/gids are controlled by a single kernel [[1]].
- Names associated to uid/gid are provided by separate non-kernel tools on host/container. Nonetheless, the mapping is done at the uid/gid level.
- It is therefore convenient to restrict access of container's user into the host system [[2]].
- Specifying a user flag ``--user`` when creating a container *also overrides* the value specified in the Dockerfile.
    - Nonetheless ``Dockerfile`` command ``USER=`` sets the privileges used to execute ``COPY`` or ``RUN`` commands during build-time
    - Then during runtime ``--user`` will *override* ``USER``


Some of the conclusions of [[1]]:

- Restrict access to the container uid on the host
- A good solution is to enforce uid from comand line ``--user``.
- same uids/gids inside/outside the container might be named differently inside/outside because naming is managed by different non-kernel tools in each case.

But:

- There are situations in which the host and container share resources. For instance:
    - When volumes are bind mounted from host to container?
    - These volumes are not just files but also sockets e.g. ``/var/run/docker.sock`` (associated to sockets group)
- Well, another possibility is to have always the same uid pre-defined in the Dockerfile

---

## Python venv w/ non-root users

One argument *not to use* python virtual environments (venv) inside a container is that the latter already provides the desired [isolation](https://stackoverflow.com/questions/48561981/activate-python-virtualenv-in-dockerfile).


```
Uninstalling pip-10.0.1:
Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/usr/local/bin/pip'
Consider using the `--user` option or check the permissions.

You are using pip version 10.0.1, however version 18.0 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
```



---

- [[1]] Understanding how uid and gid work in Docker containers
- [[2]] Best practices for writing Dockerfiles
- [[3]] Handling Permissions with Docker volumes

[1]:https://medium.com/@mccode/understanding-how-uid-and-gid-work-in-docker-containers-c37a01d01cf
[2]:https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
[3]:https://denibertovic.com/posts/handling-permissions-with-docker-volumes/
