import pytest
from tienda.inventario import (
    crear_inventario, agregar_stock, hay_stock, reducir_stock, productos_bajo_stock,
)


def test_r2_reducir_a_cero_conserva_producto():
    inv = agregar_stock(crear_inventario(), "pan", 3)
    reducir_stock(inv, "pan", 3)
    assert inv == {"pan": 0}
    assert hay_stock(inv, "pan") is False


@pytest.mark.parametrize("cantidad", [0, -1])
def test_r2_hay_stock_cantidad_invalida(cantidad):
    with pytest.raises(ValueError):
        hay_stock({"pan": 5}, "pan", cantidad)


def test_r2_reducir_insuficiente_no_modifica():
    inv = {"pan": 2}
    with pytest.raises(ValueError):
        reducir_stock(inv, "pan", 3)
    assert inv == {"pan": 2}


def test_r2_bajo_stock_incluye_cero_y_ordena():
    inv = {"zeta": 0, "alfa": 1, "medio": 50}
    assert productos_bajo_stock(inv) == ["alfa", "zeta"]


def test_r2_reducir_cantidad_invalida():
    with pytest.raises(ValueError):
        reducir_stock({"pan": 5}, "pan", 0)
