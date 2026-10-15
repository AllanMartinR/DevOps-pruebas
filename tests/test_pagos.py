import pytest
from tienda.pagos import (
    validar_luhn, detectar_marca, validar_vencimiento, procesar_pago,
)

VISA = "4111111111111111"


@pytest.mark.parametrize("numero", [
    VISA, "4111 1111 1111 1111", "4111-1111-1111-1111",
    "5555555555554444", "378282246310005",
])
def test_luhn_validos(numero):
    assert validar_luhn(numero) is True


@pytest.mark.parametrize("numero", ["4111111111111112", "", "abcd", "1234"])
def test_luhn_invalidos(numero):
    assert validar_luhn(numero) is False


def test_marcas():
    assert detectar_marca(VISA) == "visa"
    assert detectar_marca("5555555555554444") == "mastercard"
    assert detectar_marca("378282246310005") == "amex"
    assert detectar_marca("6011111111111117") == "desconocida"


def test_marca_con_separadores():
    assert detectar_marca("4111 1111 1111 1111") == "visa"


def test_vencimiento_vigente():
    assert validar_vencimiento(12, 2030, 6, 2026) is True


def test_vencimiento_vencida():
    assert validar_vencimiento(5, 2026, 6, 2026) is False


def test_vencimiento_mes_actual_aun_valido():
    assert validar_vencimiento(6, 2026, 6, 2026) is True


@pytest.mark.parametrize("mes", [0, 13])
def test_vencimiento_mes_invalido(mes):
    assert validar_vencimiento(mes, 2030, 6, 2026) is False


def test_pago_aprobado():
    assert procesar_pago(VISA, 100) == {"aprobado": True, "motivo": "ok"}


def test_pago_tarjeta_invalida():
    assert procesar_pago("4111111111111112", 100) == {"aprobado": False, "motivo": "tarjeta_invalida"}


def test_pago_monto_invalido():
    assert procesar_pago(VISA, 0) == {"aprobado": False, "motivo": "monto_invalido"}
