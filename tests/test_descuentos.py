import pytest
from tienda.descuentos import (
    aplicar_porcentaje, aplicar_cupon, descuento_por_volumen, calcular_ahorro,
)


def test_porcentaje_basico():
    assert aplicar_porcentaje(200, 10) == 180.0


def test_porcentaje_limites_validos():
    assert aplicar_porcentaje(100, 0) == 100.0
    assert aplicar_porcentaje(100, 100) == 0.0


@pytest.mark.parametrize("total,pct", [(100, -1), (100, 101), (-1, 10)])
def test_porcentaje_invalido(total, pct):
    with pytest.raises(ValueError):
        aplicar_porcentaje(total, pct)


def test_cupones_validos():
    assert aplicar_cupon(100, "DEVOPS10") == 90.0
    assert aplicar_cupon(200, "PROMO20") == 160.0
    assert aplicar_cupon(100, "MEGA50") == 50.0


def test_cupon_inexistente():
    with pytest.raises(ValueError):
        aplicar_cupon(100, "GRATIS")


@pytest.mark.parametrize("total,esperado", [
    (100, 100.0), (200, 190.0), (500, 450.0), (1000, 850.0),
])
def test_descuento_por_volumen(total, esperado):
    assert descuento_por_volumen(total) == esperado


def test_volumen_total_negativo():
    with pytest.raises(ValueError):
        descuento_por_volumen(-5)


def test_calcular_ahorro():
    assert calcular_ahorro(200, 180) == 20.0
    assert calcular_ahorro(100, 100) == 0.0


def test_ahorro_final_mayor_que_original():
    with pytest.raises(ValueError):
        calcular_ahorro(100, 150)
