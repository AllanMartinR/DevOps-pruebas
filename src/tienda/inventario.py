"""MÓDULO 3 - INVENTARIO (Equipo 3)

Estructura del inventario (un diccionario): {"pan": 20, "leche": 3}

Implementen TODAS las funciones. No cambien nombres ni parámetros.
Pruebas: tests/test_inventario.py
"""


def crear_inventario() -> dict:
    """Devuelve un inventario vacío ({})."""
    raise NotImplementedError("Equipo 3: implementen crear_inventario")


def agregar_stock(inventario: dict, producto: str, cantidad: int) -> dict:
    """Suma unidades al producto (si no existe, lo crea). Devuelve el MISMO inventario.
    cantidad <= 0 -> ValueError
    """
    raise NotImplementedError("Equipo 3: implementen agregar_stock")


def hay_stock(inventario: dict, producto: str, cantidad: int = 1) -> bool:
    """True si hay al menos `cantidad` unidades. Producto inexistente -> False.
    cantidad <= 0 -> ValueError
    """
    raise NotImplementedError("Equipo 3: implementen hay_stock")


def reducir_stock(inventario: dict, producto: str, cantidad: int) -> dict:
    """Resta unidades y devuelve el MISMO inventario.

    - cantidad <= 0 -> ValueError
    - Producto inexistente o stock insuficiente -> ValueError (y NO se modifica nada)
    - Si queda en 0, el producto SIGUE en el inventario con valor 0.
    """
    raise NotImplementedError("Equipo 3: implementen reducir_stock")


def productos_bajo_stock(inventario: dict, minimo: int = 5) -> list:
    """Lista de nombres de productos con stock MENOR que `minimo`
    (estrictamente menor), ordenados alfabéticamente. Incluye los que tienen 0.
    """
    raise NotImplementedError("Equipo 3: implementen productos_bajo_stock")
