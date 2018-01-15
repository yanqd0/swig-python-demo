#!/usr/bin/env python
# -*- coding:utf-8 -*-

""" setup script """
import runpy

from setuptools import find_packages, setup

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
    package_data={'example': ['_example.so']},

    python_requires='>=3.4',
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
