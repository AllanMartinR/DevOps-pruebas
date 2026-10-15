"""MÓDULO 5 - PAGOS (Equipo 5)

Implementen TODAS las funciones. No cambien nombres ni parámetros.
Pruebas: tests/test_pagos.py
Pista: el algoritmo de Luhn está en Wikipedia ("Algoritmo de Luhn").
"""


def validar_luhn(numero: str) -> bool:
    """True si el número de tarjeta pasa el algoritmo de Luhn.

    - Acepta espacios y guiones como separadores ("4111 1111 1111 1111").
    - Si no es str, tiene caracteres que no son dígitos (después de quitar
      espacios y guiones) o su longitud no está entre 13 y 19 -> False.
    """
    raise NotImplementedError("Equipo 5: implementen validar_luhn")


def detectar_marca(numero: str) -> str:
    """Detecta la marca según el inicio del número (ignora espacios y guiones):

        empieza con 4                  -> "visa"
        empieza con 51, 52, 53, 54, 55 -> "mastercard"
        empieza con 34 o 37            -> "amex"
        cualquier otro caso            -> "desconocida"

    No valida Luhn. Si no es str -> "desconocida".
    """
    raise NotImplementedError("Equipo 5: implementen detectar_marca")


def validar_vencimiento(mes: int, anio: int, mes_actual: int, anio_actual: int) -> bool:
    """True si la tarjeta NO ha vencido.

    - mes debe estar entre 1 y 12, si no -> False.
    - La tarjeta vence al FINAL del mes indicado: si mes/anio es igual al
      mes_actual/anio_actual, todavía es válida.
    """
    raise NotImplementedError("Equipo 5: implementen validar_vencimiento")


def procesar_pago(numero: str, monto: float) -> dict:
    """Simula un pago. Devuelve {"aprobado": bool, "motivo": str}.

    Se revisa en este orden:
        monto <= 0         -> {"aprobado": False, "motivo": "monto_invalido"}
        Luhn inválido      -> {"aprobado": False, "motivo": "tarjeta_invalida"}
        todo bien          -> {"aprobado": True,  "motivo": "ok"}
    """
    raise NotImplementedError("Equipo 5: implementen procesar_pago")
