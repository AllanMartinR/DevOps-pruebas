import pytest
from tienda.usuarios import (
    validar_correo, validar_password, validar_registro, normalizar_correo,
)


def test_r2_correo_con_doble_punto_en_dominio():
    assert validar_correo("ana@correo..com") is False


def test_r2_correo_no_string():
    assert validar_correo(None) is False


def test_r2_correo_con_espacio_al_final():
    assert validar_correo("ana@correo.com ") is False


def test_r2_password_con_espacio():
    assert validar_password("Abc def1!") is False


def test_r2_password_exactamente_8():
    assert validar_password("Abcdef1!") is True


def test_r2_password_guion_bajo_cuenta_como_simbolo():
    assert validar_password("Abcdef1_") is True


def test_r2_password_con_enie():
    assert validar_password("Contraseña1!") is True


def test_r2_password_no_string():
    assert validar_password(None) is False


def test_r2_registro_password_invalida_pero_coincide():
    assert validar_registro("ana@correo.com", "abc", "abc") == (False, ["password_invalida"])


def test_r2_normalizar_con_espacio_interno():
    with pytest.raises(ValueError):
        normalizar_correo("ana perez@correo.com")
