import importlib

from .. import calc_k


def test_kcalc():
    assert importlib.import_module("kcalc") is not None


def test_calc_k():
    assert calc_k(0) == 1.0
