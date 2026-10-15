import pytest
from tienda.carrito import (
    crear_carrito, agregar_producto, quitar_producto, calcular_total, contar_articulos,
)


def test_crear_carrito_vacio():
    assert crear_carrito() == {}


def test_agregar_producto_nuevo():
    c = crear_carrito()
    agregar_producto(c, "pan", 10.0)
    assert c == {"pan": {"precio": 10.0, "cantidad": 1}}


def test_agregar_devuelve_el_mismo_carrito():
    c = crear_carrito()
    assert agregar_producto(c, "pan", 10.0, 2) is c


def test_agregar_mismo_producto_suma_cantidad():
    c = crear_carrito()
    agregar_producto(c, "pan", 10.0, 2)
    agregar_producto(c, "pan", 10.0, 3)
    assert c["pan"]["cantidad"] == 5


@pytest.mark.parametrize("precio,cantidad", [(0, 1), (-5, 1), (10, 0), (10, -1)])
def test_agregar_valores_invalidos(precio, cantidad):
    with pytest.raises(ValueError):
        agregar_producto(crear_carrito(), "pan", precio, cantidad)


def test_quitar_producto_completo():
    c = agregar_producto(crear_carrito(), "pan", 10.0, 3)
    quitar_producto(c, "pan")
    assert "pan" not in c


def test_quitar_producto_parcial():
    c = agregar_producto(crear_carrito(), "pan", 10.0, 3)
    quitar_producto(c, "pan", 1)
    assert c["pan"]["cantidad"] == 2


def test_quitar_producto_inexistente():
    with pytest.raises(KeyError):
        quitar_producto(crear_carrito(), "pan")


def test_calcular_total():
    c = crear_carrito()
    agregar_producto(c, "pan", 10.0, 2)
    agregar_producto(c, "leche", 25.5, 1)
    assert calcular_total(c) == 45.5


def test_total_carrito_vacio():
    assert calcular_total(crear_carrito()) == 0


def test_contar_articulos():
    c = crear_carrito()
    agregar_producto(c, "pan", 10.0, 2)
    agregar_producto(c, "leche", 25.5, 3)
    assert contar_articulos(c) == 5
    assert contar_articulos(crear_carrito()) == 0
