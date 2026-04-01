#!/usr/bin/env python
import setuptools
from Cython.Build import cythonize
import os

os.environ["CFLAGS"] = "-O3"

if __name__ == "__main__":
    ext_modules = cythonize(
        ["baidupcs_py/common/simple_cipher.pyx"],
        language_level=3,
        compiler_directives={"linetrace": True},
    )
    ext_modules[0].name = "baidupcs_py.common.simple_cipher"

    setuptools.setup(
        name="baidupcs-py",
        packages=setuptools.find_packages(include=["baidupcs_py", "baidupcs_py.*"]),
        ext_modules=ext_modules,
    )
