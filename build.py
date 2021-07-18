# flake8: noqa

import os

try:
    import numpy
    from Cython.Build import cythonize
except ImportError:

    def build(setup_kwargs):
        pass


else:
    from distutils.command.build_ext import build_ext

    def build(setup_kwargs):
        extensions = ["boxscript/*.pyx"]

        os.environ["CFLAGS"] = "-O3"

        setup_kwargs.update(
            {
                "ext_modules": cythonize(
                    extensions,
                    language_level=3,
                    compiler_directives={"linetrace": True},
                ),
                "cmdclass": {"build_ext": build_ext},
                "include_dirs": [numpy.get_include()],
            }
        )
