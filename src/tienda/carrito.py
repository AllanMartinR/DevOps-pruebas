"""MÓDULO 1 - CARRITO DE COMPRAS (Equipo 1)

Estructura del carrito (un diccionario):
    {"pan": {"precio": 10.0, "cantidad": 2}, "leche": {"precio": 25.5, "cantidad": 1}}

Implementen TODAS las funciones. No cambien nombres ni parámetros.
Pruebas: tests/test_carrito.py
"""


def crear_carrito() -> dict:
    """Devuelve un carrito vacío ({})."""
    raise NotImplementedError("Equipo 1: implementen crear_carrito")


def agregar_producto(carrito: dict, nombre: str, precio: float, cantidad: int = 1) -> dict:
    """Agrega un producto al carrito y devuelve el MISMO carrito.

    - Si el producto ya existe, suma la cantidad y conserva el precio original.
    - precio <= 0  -> ValueError
    - cantidad <= 0 -> ValueError
    """
    raise NotImplementedError("Equipo 1: implementen agregar_producto")


def quitar_producto(carrito: dict, nombre: str, cantidad: int | None = None) -> dict:
    """Quita un producto y devuelve el MISMO carrito.

    - cantidad=None -> elimina el producto completo.
    - Si cantidad >= a la que hay en el carrito -> elimina el producto completo.
    - Si cantidad es menor -> solo resta esa cantidad.
    - Producto que no está en el carrito -> KeyError
    - cantidad <= 0 (cuando no es None) -> ValueError
    """
    raise NotImplementedError("Equipo 1: implementen quitar_producto")


def calcular_total(carrito: dict) -> float:
    """Suma precio * cantidad de todos los productos, redondeado a 2 decimales.
    Carrito vacío -> 0 (0.0).
    """
    raise NotImplementedError("Equipo 1: implementen calcular_total")


def contar_articulos(carrito: dict) -> int:
    """Total de UNIDADES en el carrito (suma de cantidades). Vacío -> 0."""
    raise NotImplementedError("Equipo 1: implementen contar_articulos")
