import pytest
from tienda.pagos import validar_luhn, detectar_marca, validar_vencimiento, procesar_pago


def test_r2_luhn_muy_corto():
    assert validar_luhn("79927398713") is False  # Luhn válido pero de 11 dígitos


def test_r2_luhn_muy_largo():
    assert validar_luhn("0" * 20) is False


def test_r2_luhn_no_string():
    assert validar_luhn(4111111111111111) is False


@pytest.mark.parametrize("numero,marca", [
    ("5011111111111111", "desconocida"),
    ("5611111111111111", "desconocida"),
    ("5111111111111111", "mastercard"),
    ("3411111111111111", "amex"),
    ("", "desconocida"),
])
def test_r2_marcas_borde(numero, marca):
    assert detectar_marca(numero) == marca


def test_r2_vencimiento_cambio_de_anio():
    assert validar_vencimiento(1, 2027, 12, 2026) is True
    assert validar_vencimiento(12, 2025, 1, 2026) is False


def test_r2_monto_invalido_tiene_prioridad():
    assert procesar_pago("1234", -5) == {"aprobado": False, "motivo": "monto_invalido"}
