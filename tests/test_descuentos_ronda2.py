import pytest
from tienda.descuentos import (
    aplicar_porcentaje, aplicar_cupon, descuento_por_volumen, calcular_ahorro,
)


def test_r2_cupon_minusculas_y_espacios():
    assert aplicar_cupon(100, "  devops10 ") == 90.0


def test_r2_cupon_no_string():
    with pytest.raises(ValueError):
        aplicar_cupon(100, None)


def test_r2_volumen_justo_debajo_del_umbral():
    assert descuento_por_volumen(199.99) == 199.99
    assert descuento_por_volumen(499.99) == 474.99


def test_r2_porcentaje_decimal():
    assert aplicar_porcentaje(80, 12.5) == 70.0


def test_r2_ahorro_redondeado():
    assert calcular_ahorro(10.1, 9.09) == 1.01
