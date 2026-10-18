import pytest
from tienda.envios import calcular_costo, dias_entrega, costo_final


def test_r2_peso_maximo_permitido():
    assert calcular_costo(30, "local") == 630.0


def test_r2_peso_arriba_del_maximo():
    with pytest.raises(ValueError):
        calcular_costo(30.01, "local")


def test_r2_peso_menor_a_un_kilo_solo_base():
    assert calcular_costo(0.5, "nacional") == 100.0


@pytest.mark.parametrize("zona", ["NACIONAL", " Nacional ", "nacional"])
def test_r2_zona_normalizada(zona):
    assert calcular_costo(1, zona) == 100.0
    assert dias_entrega(zona) == 3


def test_r2_zona_no_string():
    with pytest.raises(ValueError):
        calcular_costo(1, None)


def test_r2_gratis_con_zona_normalizada():
    assert costo_final(1, " Local ", 1000) == 0.0


def test_r2_datos_invalidos_fallan_aunque_sea_gratis():
    with pytest.raises(ValueError):
        costo_final(1, "luna", 5000)
    with pytest.raises(ValueError):
        costo_final(0, "local", 5000)
