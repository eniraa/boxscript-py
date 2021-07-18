# -*- coding: utf-8 -*-
# flake8: noqa
from setuptools import setup

packages = ["boxscript"]

package_data = {"": ["*"]}

install_requires = ["Cython>=0.29.24,<0.30.0", "numpy>=1.21.0,<2.0.0"]

setup_kwargs = {
    "name": "boxscript",
    "version": "0.1.0",
    "description": 'BoxScript is a language based on the idea of "boxes".',
    "long_description": None,
    "author": "Pyxiis",
    "author_email": "47072520+pyxiis@users.noreply.github.com",
    "maintainer": None,
    "maintainer_email": None,
    "url": None,
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "python_requires": ">=3.9,<4.0",
}
from build import *

build(setup_kwargs)

setup(**setup_kwargs)
