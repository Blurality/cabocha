#!/usr/bin/env python

from distutils.core import Extension, os, setup


def cmd1(_str):
    out = os.popen(_str)
    out_lines = out.readlines()
    return out_lines[0][:-1]


def cmd2(str):
    return cmd1(str).split()


setup(
    name="cabocha-python",
    version=cmd1("./cabocha-config --version"),
    py_modules=["CaboCha"],
    ext_modules=[
        Extension(
            "_CaboCha",
            [
                "CaboCha_wrap.cxx",
            ],
            include_dirs=cmd2("cabocha-config --inc-dir"),
            library_dirs=cmd2("cabocha-config --libs-only-L"),
            libraries=cmd2("cabocha-config --libs-only-l"),
        )
    ],
)
