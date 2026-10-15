import pytest
from tienda.usuarios import (
    validar_correo, validar_password, validar_registro, normalizar_correo,
)


@pytest.mark.parametrize("correo", ["ana@correo.com", "a.b+c@sub.dominio.mx"])
def test_correos_validos(correo):
    assert validar_correo(correo) is True


@pytest.mark.parametrize("correo", [
    "", "ana", "ana@", "@correo.com", "ana@correo", "ana@@correo.com",
    "ana perez@correo.com", "ana@.com", "ana@correo.",
])
def test_correos_invalidos(correo):
    assert validar_correo(correo) is False


def test_password_valida():
    assert validar_password("Abcdef1!") is True


@pytest.mark.parametrize("password", [
    "abcdef1!",   # sin mayúscula
    "ABCDEF1!",   # sin minúscula
    "Abcdefg!",   # sin número
    "Abcdefg1",   # sin símbolo
    "Ab1!",       # muy corta
])
def test_password_invalida(password):
    assert validar_password(password) is False


def test_registro_valido():
    assert validar_registro("ana@correo.com", "Abcdef1!", "Abcdef1!") == (True, [])


def test_registro_correo_invalido():
    assert validar_registro("ana", "Abcdef1!", "Abcdef1!") == (False, ["correo_invalido"])


def test_registro_todo_mal():
    esperado = (False, ["correo_invalido", "password_invalida", "password_no_coincide"])
    assert validar_registro("ana", "abc", "abd") == esperado


def test_normalizar_correo():
    assert normalizar_correo("  Ana@Correo.COM ") == "ana@correo.com"


def test_normalizar_correo_invalido():
    with pytest.raises(ValueError):
        normalizar_correo("no-es-correo")
