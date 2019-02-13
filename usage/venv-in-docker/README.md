
## Using virtualenv or user's installation?

```console

().venv) crespo@crespo-wkstn:~/devp/dockerfiles/usage/non-root-users/dev-target$ docker-compose -f docker-compose.yml -f docker-compose.devel.yml run foo /bin/sh
Entrypoint for target development ...
  User    :uid=0(root) gid=0(root) groups=0(root),0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)
  Workdir :/home/scu
~ $ printenv
HOSTNAME=09ff1b4fcdcb
PYTHON_PIP_VERSION=19.0.1
SHLVL=2
HOME=/home/scu
GPG_KEY=0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D
TERM=xterm
PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
LANG=C.UTF-8
MY_BUILD_MODE=development
PYTHON_VERSION=3.6.8
PIP=/home/scu/.venv/bin/pip3 --no-cache
MY_BUILD_TARGET=development
PWD=/home/scu
~ $ which pip
/usr/local/bin/pip
~ $ source .venv/bin/activate
(.venv) ~ $ pip --version
pip 19.0.2 from /home/scu/.venv/lib/python3.6/site-packages/pip (python 3.6)
(.venv) ~ $ deactivate
~ $ pip --version
pip 19.0.1 from /usr/local/lib/python3.6/site-packages/pip (python 3.6)
~ $ 

```

- Notice that system `pip` is ``PYTHON_PIP_VERSION`` but not ``~/.venv/bin/pip``
- Might be convenient to do `pip install --user ...`. Then, in development mode, we can install w/o root privileges
- 

