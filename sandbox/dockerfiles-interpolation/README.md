# options interpolation in a docker or a docker-compose files



```
version: '3.4'
services:
  test:
    build:
      args:
        - host_gid_=$(id -u $USER)
```

results in

```
ERROR: Invalid interpolation format for "build" option in service "test": "host_gid_=$(id -u $USER)"
```