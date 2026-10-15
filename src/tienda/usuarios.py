"""MÓDULO 4 - USUARIOS (Equipo 4)

Implementen TODAS las funciones. No cambien nombres ni parámetros.
Pruebas: tests/test_usuarios.py
"""


def validar_correo(correo: str) -> bool:
    """True si el correo es válido. Reglas:

    - Es un str, sin espacios.
    - Tiene exactamente un '@'.
    - Hay texto antes y después del '@'.
    - El dominio (después del '@') contiene al menos un '.', no empieza ni
      termina con '.', y no tiene '..' (partes vacías).
    No hace strip: " ana@correo.com" es inválido por el espacio.
    """
    raise NotImplementedError("Equipo 4: implementen validar_correo")


def validar_password(password: str) -> bool:
    """True si la contraseña es válida. Reglas:

    - Es un str de al menos 8 caracteres.
    - Al menos una mayúscula, una minúscula y un número.
    - Al menos un símbolo (cualquier carácter que no sea letra, número ni espacio;
      el guion bajo '_' cuenta como símbolo).
    - No contiene espacios.
    """
    raise NotImplementedError("Equipo 4: implementen validar_password")


def validar_registro(correo: str, password: str, confirmacion: str) -> tuple:
    """Valida un registro completo. Devuelve (es_valido, errores).

    `errores` es una lista con estos códigos, en ESTE orden, solo los que apliquen:
        "correo_invalido"      -> validar_correo falla
        "password_invalida"    -> validar_password falla
        "password_no_coincide" -> password != confirmacion

    Ejemplos:
        validar_registro("ana@correo.com", "Abcdef1!", "Abcdef1!") -> (True, [])
        validar_registro("ana", "abc", "abd") ->
            (False, ["correo_invalido", "password_invalida", "password_no_coincide"])
    """
    raise NotImplementedError("Equipo 4: implementen validar_registro")


def normalizar_correo(correo: str) -> str:
    """Quita espacios al inicio/final y pasa a minúsculas.
    "  Ana@Correo.COM " -> "ana@correo.com"
    Si el resultado no es un correo válido -> ValueError
    """
    raise NotImplementedError("Equipo 4: implementen normalizar_correo")
