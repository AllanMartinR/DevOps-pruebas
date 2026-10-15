"""MÓDULO 6 - ENVÍOS (Equipo 6)

Implementen TODAS las funciones. No cambien nombres ni parámetros.
Pruebas: tests/test_envios.py
"""

# Tarifa base (hasta 1 kg) y días de entrega por zona (NO cambiar estos valores)
TARIFAS = {"local": 50, "nacional": 100, "internacional": 300}
DIAS = {"local": 1, "nacional": 3, "internacional": 10}


def calcular_costo(peso_kg: float, zona: str) -> float:
    """Costo de envío = tarifa base de la zona + 20 por cada kg ADICIONAL
    (cualquier fracción de kg adicional cuenta como kg completo).

    Ejemplos: 1 kg local -> 50.0 | 1.5 kg local -> 70.0 | 2 kg nacional -> 120.0

    - La zona no distingue mayúsculas/minúsculas ni espacios al inicio/final.
    - Zona inválida (o que no es str) -> ValueError
    - peso <= 0 o peso > 30 -> ValueError (30 kg sí es válido)
    - Devuelve float.
    """
    raise NotImplementedError("Equipo 6: implementen calcular_costo")


def envio_gratis(total_compra: float) -> bool:
    """True si el total de la compra es >= 999."""
    raise NotImplementedError("Equipo 6: implementen envio_gratis")


def dias_entrega(zona: str) -> int:
    """Días de entrega según DIAS. Misma normalización de zona que calcular_costo.
    Zona inválida -> ValueError
    """
    raise NotImplementedError("Equipo 6: implementen dias_entrega")


def costo_final(peso_kg: float, zona: str, total_compra: float) -> float:
    """Costo de envío considerando promoción.

    - Si envio_gratis(total_compra) y la zona NO es internacional -> 0.0
    - En cualquier otro caso -> calcular_costo(peso_kg, zona)
    - Los datos inválidos (zona, peso) siempre lanzan ValueError, aunque el
      envío fuera gratis.
    """
    raise NotImplementedError("Equipo 6: implementen costo_final")
