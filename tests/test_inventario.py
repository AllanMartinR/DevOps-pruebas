import pytest
from tienda.inventario import (
    crear_inventario, agregar_stock, hay_stock, reducir_stock, productos_bajo_stock,
)


def test_crear_inventario_vacio():
    assert crear_inventario() == {}


def test_agregar_stock_nuevo_y_existente():
    inv = crear_inventario()
    agregar_stock(inv, "pan", 10)
    agregar_stock(inv, "pan", 5)
    assert inv == {"pan": 15}


def test_agregar_stock_devuelve_el_mismo_inventario():
    inv = crear_inventario()
    assert agregar_stock(inv, "pan", 1) is inv


@pytest.mark.parametrize("cantidad", [0, -3])
def test_agregar_stock_cantidad_invalida(cantidad):
    with pytest.raises(ValueError):
        agregar_stock(crear_inventario(), "pan", cantidad)


def test_hay_stock():
    inv = agregar_stock(crear_inventario(), "pan", 5)
    assert hay_stock(inv, "pan") is True
    assert hay_stock(inv, "pan", 5) is True
    assert hay_stock(inv, "pan", 6) is False


def test_hay_stock_producto_inexistente():
    assert hay_stock(crear_inventario(), "pan") is False


def test_reducir_stock():
    inv = agregar_stock(crear_inventario(), "pan", 10)
    reducir_stock(inv, "pan", 4)
    assert inv["pan"] == 6


def test_reducir_stock_insuficiente():
    inv = agregar_stock(crear_inventario(), "pan", 2)
    with pytest.raises(ValueError):
        reducir_stock(inv, "pan", 3)


def test_reducir_stock_inexistente():
    with pytest.raises(ValueError):
        reducir_stock(crear_inventario(), "pan", 1)


def test_productos_bajo_stock():
    inv = {"a": 10, "b": 2, "c": 5}
    assert productos_bajo_stock(inv) == ["b"]
    assert productos_bajo_stock(inv, minimo=11) == ["a", "b", "c"]
