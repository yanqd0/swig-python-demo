#!/usr/bin/env python
# -*- coding:utf-8 -*-

""" setup script """
import runpy

from setuptools import Extension, find_packages, setup
from setuptools.command.build_py import build_py

EXAMPLE_EXT = Extension(
    name='_example',
    sources=[
        'src/example/example.c',
        'src/example/example.i',
    ],
)

STD_EXT = Extension(
    name='_stl_example',
    swig_opts=['-c++'],
    sources=[
        'src/example/stl_example.cpp',
        'src/example/stl_example.i',
    ],
    include_dirs=[
        'src/example',
    ],
    extra_compile_args=[  # The g++ (4.8) in Travis needs this
        '-std=c++11',
    ]
)


# Build extensions before python modules,
# or the generated SWIG python files will be missing.
class BuildPy(build_py):
    def run(self):
        self.run_command('build_ext')
        super(build_py, self).run()


INFO = runpy.run_path('src/example/_meta.py')

setup(
    name='swig-example-demo',
    description='A Python demo for SWIG',
    version=INFO['__version__'],
    author=INFO['__author__'],
    license=INFO['__copyright__'],
    author_email=INFO['__email__'],
    url=INFO['__url__'],
    keywords=['SWIG', 'demo'],

    packages=find_packages('src'),
    package_dir={'': 'src'},
    ext_modules=[EXAMPLE_EXT, STD_EXT],
    cmdclass={
        'build_py': BuildPy,
    },

    python_requires='>=3.4',
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pytest-pep8',
        'pytest-flakes',
    ],
)
