import importlib


def test_kcalc():
    assert importlib.import_module("kcalc") is not None
