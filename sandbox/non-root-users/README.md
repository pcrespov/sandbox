# non-root users

In [[1]] we find a good synthesis of how uids work between containers and hosts. Some important points:

- The linux kernel manages the uid/gid and kenrel-level syscalls are used to detemine access privileges
- Both the host and containers run on the same kernel, therefore the entire world of uid/gids are controlled by a single kernel [[1]].
- Names associated to uid/gid are provided by separate non-kernel tools on host/container. Nonetheless, the mapping is done at the uid/gid level.
- It is therefore convenient to restrict access of container's user into the host system [[2]].
- Specifying a user flag ``--user`` when creating a container *also overrides* the value specified in the Dockerfile.


Some of the conclusions of [[1]]:

- Restrict access to the container uid on the host
- A good solution is to enforce uid from comand line ``--user``. 
- same uids/gids inside/outside the container might be named differently inside/outside because naming is managed by different tools in each case.

But:

- There are situations in which the host and container share resources. For instance:
    - When volumes are bind mounted from host to container?
    - These volumes are not just files but also sockets e.g. /var/run/docker.sock
- Well, another possibility is to have always the same uid pre-defined in the Dockerfile

---

- [[1]] Understanding how uid and gid work in Docker containers
- [[2]] Best practices for writing Dockerfiles

[1]:https://medium.com/@mccode/understanding-how-uid-and-gid-work-in-docker-containers-c37a01d01cf 
[2]:https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
