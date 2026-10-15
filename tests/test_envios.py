import pytest
from tienda.envios import calcular_costo, envio_gratis, dias_entrega, costo_final


@pytest.mark.parametrize("peso,zona,esperado", [
    (1, "local", 50.0),
    (1, "nacional", 100.0),
    (1, "internacional", 300.0),
    (2, "nacional", 120.0),
    (1.5, "local", 70.0),
    (2.1, "local", 90.0),
])
def test_calcular_costo(peso, zona, esperado):
    assert calcular_costo(peso, zona) == esperado


@pytest.mark.parametrize("peso", [0, -1])
def test_peso_invalido(peso):
    with pytest.raises(ValueError):
        calcular_costo(peso, "local")


def test_peso_excede_limite():
    with pytest.raises(ValueError):
        calcular_costo(31, "local")


def test_zona_invalida():
    with pytest.raises(ValueError):
        calcular_costo(1, "luna")


def test_envio_gratis():
    assert envio_gratis(999) is True
    assert envio_gratis(998.99) is False


def test_dias_entrega():
    assert dias_entrega("local") == 1
    assert dias_entrega("nacional") == 3
    assert dias_entrega("internacional") == 10


def test_dias_zona_invalida():
    with pytest.raises(ValueError):
        dias_entrega("luna")


def test_costo_final_gratis():
    assert costo_final(1, "local", 1000) == 0.0


def test_costo_final_sin_promocion():
    assert costo_final(1, "local", 100) == 50.0


def test_costo_final_internacional_no_es_gratis():
    assert costo_final(1, "internacional", 5000) == 300.0
