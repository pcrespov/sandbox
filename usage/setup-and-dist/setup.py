from setuptools import (
    setup,
    find_packages
)

setup(
    name="sample-package",
    version="0.0.0",
    packages=find_packages(where='src'),
    package_dir={
        '': 'src',
    },
    include_package_data=True,
    package_data={
        '': ['config/*.yml']
    },
    entry_points={
        'console_scripts': [
            'sample-package=sample_package.__main__:main', ]
        },
    python_requires='>=3.6',
    install_requires=[
        'pyyaml>4.2b1'
    ],
)