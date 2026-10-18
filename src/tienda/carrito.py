def crear_carrito():
    return {}


def agregar_producto(carrito, nombre, precio, cantidad=1):
    if precio <= 0:
        raise ValueError("precio inválido")
    if cantidad <= 0:
        raise ValueError("cantidad inválida")
    if nombre in carrito:
        carrito[nombre]["cantidad"] += cantidad
    else:
        carrito[nombre] = {"precio": precio, "cantidad": cantidad}
    return carrito


def quitar_producto(carrito, nombre, cantidad=None):
    if nombre not in carrito:
        raise KeyError(nombre)
    return carrito


def calcular_total(carrito):
    return round(sum(p["precio"] * p["cantidad"] for p in carrito.values()), 2)


def contar_articulos(carrito):
    return sum(p["cantidad"] for p in carrito.values())
