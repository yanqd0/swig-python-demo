import time

import example


def test_my_variable():
    assert 3.0 == example.cvar.My_variable


def test_fact():
    assert 120 == example.fact(5)


def test_get_time():
    py_time = time.time()
    py_time = time.localtime(py_time)
    py_time = time.asctime(py_time)
    c_time = example.get_time().strip()
    assert py_time == c_time


def test_my_mod():
    assert 1 == example.my_mod(7, 3)
