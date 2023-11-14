import pytest
from src.actividad2 import unir_conjuntos
@pytest.mark.parametrize(
    "conjunto_primaria,conjunto_secundaria,union",
    [
        ({'cesar', 'ana'},{'cesar'},{'cesar', 'ana'})
    ]
)

def test_unir_conjuntos_params(conjunto_primaria,conjunto_secundaria,union):
    assert unir_conjuntos(conjunto_primaria,conjunto_secundaria)==union

from src.actividad2 import intersectar_conjuntos
@pytest.mark.parametrize(
    "conjunto_primaria,conjunto_secundaria,interseccion",
    [
        ({'cesar', 'ana'},{'cesar'},{'cesar'})
    ]
)

def test_intersectar_conjuntos_params(conjunto_primaria,conjunto_secundaria,interseccion):
    assert intersectar_conjuntos(conjunto_primaria,conjunto_secundaria)==interseccion

from src.actividad2 import diferenciar_conjuntos
@pytest.mark.parametrize(
    "conjunto_primaria,conjunto_secundaria,diferencia",
    [
        ({'cesar', 'ana'},{'cesar'},{'ana'})
    ]
)
def test_diferenciar_conjuntos_params(conjunto_primaria,conjunto_secundaria,diferencia):
    assert diferenciar_conjuntos(conjunto_primaria,conjunto_secundaria)==diferencia

from src.actividad2 import comprobar_conjuntos
@pytest.mark.parametrize(
    "conjunto_primaria,conjunto_secundaria,comprobacion",
    [
        ({'cesar', 'ana'},{'cesar'},False)
    ]
)

def test_comprobar_conjuntos_params(conjunto_primaria,conjunto_secundaria,comprobacion):
    assert comprobar_conjuntos(conjunto_primaria,conjunto_secundaria)==comprobacion
