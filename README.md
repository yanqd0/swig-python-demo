# SWIG Python demo

[![Travis](https://travis-ci.org/yanqd0/swig-python-demo.svg?branch=master)](https://travis-ci.org/yanqd0/swig-python-demo)
[![Requirements](https://requires.io/github/yanqd0/swig-python-demo/requirements.svg?branch=master)](https://requires.io/github/yanqd0/swig-python-demo/requirements/?branch=master)
[![License](https://img.shields.io/github/license/yanqd0/swig-python-demo.svg)](https://github.com/yanqd0/swig-python-demo/blob/master/LICENSE)

This is a demo for using [SWIG] to communicate C/C++ in Python.

中文介绍：《[在setup.py中配置SWIG模块 · 零壹軒·笔记](https://note.qidong.name/2018/03/swig-setup-py/)》

[SWIG]:http://www.swig.org/

## Project Structure

```
swig-python-demo
├── LICENSE
├── Makefile
├── setup.cfg
├── setup.py
├── src
│   └── example
│       ├── example.c
│       ├── example.h
│       ├── example.i
│       ├── __init__.py
│       ├── _meta.py
│       ├── stl_example.cpp
│       ├── stl_example.hpp
│       └── stl_example.i
└── tests
    ├── test_example.py
    └── test_stl_example.py
```

There is only 1 Python module named `example`.
However, there are 2 extensions behind.
One ([example.c](src/example/example.c)) is by C,
and the other is by C++ with STL ([stl_example.cpp](src/example/stl_example.cpp)).

The key secret is in [setup.py](setup.py).

There is also a [Makefile](Makefile) to explain how [SWIG] works.

## Usage

```sh
virtualenv -p python3 .env
source .env/bin/activate
pip install -r requirements.txt
pip install -e .
pytest
```

The compilation and packaging happens in `pip install -e .`
