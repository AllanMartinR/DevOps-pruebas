import pytest
from tienda.carrito import crear_carrito, agregar_producto, quitar_producto, calcular_total


def test_r2_conserva_precio_original():
    c = agregar_producto(crear_carrito(), "pan", 10.0, 1)
    agregar_producto(c, "pan", 99.0, 1)
    assert c["pan"] == {"precio": 10.0, "cantidad": 2}


def test_r2_total_redondeado_a_2_decimales():
    c = crear_carrito()
    agregar_producto(c, "a", 0.1)
    agregar_producto(c, "b", 0.2)
    assert calcular_total(c) == 0.3


def test_r2_quitar_mas_de_lo_que_hay_elimina():
    c = agregar_producto(crear_carrito(), "pan", 10.0, 2)
    quitar_producto(c, "pan", 5)
    assert "pan" not in c


def test_r2_quitar_cantidad_exacta_elimina():
    c = agregar_producto(crear_carrito(), "pan", 10.0, 2)
    quitar_producto(c, "pan", 2)
    assert c == {}


@pytest.mark.parametrize("cantidad", [0, -1])
def test_r2_quitar_cantidad_invalida(cantidad):
    c = agregar_producto(crear_carrito(), "pan", 10.0, 2)
    with pytest.raises(ValueError):
        quitar_producto(c, "pan", cantidad)
