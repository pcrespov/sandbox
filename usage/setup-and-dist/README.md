# Setup and distribution of python modules


- [Distribution of python modules](https://docs.python.org/3.7/distributing/index.html)
- [Installing packages tutorial](https://packaging.python.org/tutorials/installing-packages/)
- [setuptools](https://setuptools.readthedocs.io/en/latest/)
- [Lies, More lies and python packaging documentation on package-data](http://blog.codekills.net/2011/07/15/lies,-more-lies-and-python-packaging-documentation-on--package_data-/) - not sure this critic is up-to-date

### Problem1: sample_package 

 How to include data files (e.g. configs) in distributions and how to access to them at runtime?

 The section [Including Data Files](https://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files) is a bit misleading ...

```bash
$ source .venv/bin/activate
$ pip install .
$ sample-package 

loading sample_package
echoing : None
resource_exists(sample_package.resources,config/ci.yml) = True
resource_stream(sample_package.resources,config/ci.yml) = <_io.BufferedReader name='/home/crespo/devp/dockerfiles/.venv/lib/python3.6/site-packages/sample_package/config/ci.yml'>
resource_isdir(sample_package.resources,config/ci.yml) = False
resource_filename(sample_package.resources,config/ci.yml) = /home/crespo/devp/dockerfiles/.venv/lib/python3.6/site-packages/sample_package/config/ci.yml
```