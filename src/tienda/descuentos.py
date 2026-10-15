"""MÓDULO 2 - DESCUENTOS (Equipo 2)

Implementen TODAS las funciones. No cambien nombres ni parámetros.
Pruebas: tests/test_descuentos.py
Todos los resultados se redondean a 2 decimales.
"""

# Cupones válidos y su porcentaje de descuento (NO cambiar estos valores)
CUPONES = {
    "DEVOPS10": 10,
    "PROMO20": 20,
    "MEGA50": 50,
}


def aplicar_porcentaje(total: float, porcentaje: float) -> float:
    """Devuelve el total con el porcentaje de descuento aplicado.

    Ejemplo: aplicar_porcentaje(200, 10) -> 180.0
    - total < 0 -> ValueError
    - porcentaje fuera de 0..100 -> ValueError (0 y 100 sí son válidos)
    """
    raise NotImplementedError("Equipo 2: implementen aplicar_porcentaje")


def aplicar_cupon(total: float, codigo: str) -> float:
    """Aplica un cupón de CUPONES al total.

    - No distingue mayúsculas/minúsculas y ignora espacios al inicio/final.
    - Código que no existe (o que no es str) -> ValueError
    """
    raise NotImplementedError("Equipo 2: implementen aplicar_cupon")


def descuento_por_volumen(total: float) -> float:
    """Descuento automático según el monto de compra:

        total >= 1000 -> 15%
        total >= 500  -> 10%
        total >= 200  -> 5%
        menos de 200  -> sin descuento

    total < 0 -> ValueError
    """
    raise NotImplementedError("Equipo 2: implementen descuento_por_volumen")


def calcular_ahorro(total_original: float, total_final: float) -> float:
    """Cuánto se ahorró: total_original - total_final (2 decimales).
    Si total_final > total_original -> ValueError
    """
    raise NotImplementedError("Equipo 2: implementen calcular_ahorro")
