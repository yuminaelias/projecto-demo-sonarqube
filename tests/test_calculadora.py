from src.calculadora import somar_precos, somar_quantidades


def test_somar_precos():
    assert somar_precos([10, 20, 30]) == 60


def test_somar_quantidades():
    assert somar_quantidades([1, 2, 3]) == 6
