import pkg_resources
from pkg_resources import resource_string, resource_dir


def print_resources():
    """ This is how to access package resources
    See  https://setuptools.readthedocs.io/en/latest/setuptools.html#accessing-data-files-at-runtime    
     http://peak.telecommunity.com/DevCenter/PythonEggs#accessing-package-resources
    """
    for f in ['resource_exists', 'resource_stream', 'resource_isdir', 'resource_listdir', 'resource_filename']:
        args = __name__, "config/ci.yml"
        try:
            res = getattr(pkg_resources, f)(*args)
            print("{}({},{}) = {}".format(f, args[0], args[1], res ))
        except:
            pass