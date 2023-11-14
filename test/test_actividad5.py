import pytest
from src.actividad5 import conjunto_pares
@pytest.mark.parametrize(
    "numeros,pares",
    [
        ({1, 2, 3, 4, 5, 6, 7, 8, 9, 10},{2, 4, 6, 8, 10})
    ]
)
def test_conjunto_pares_params(numeros,pares):
    assert conjunto_pares(numeros)==pares

from src.actividad5 import conjunto_multiplos_tres
@pytest.mark.parametrize(
    "numeros,multiplos_tres",
    [
        ({1, 2, 3, 4, 5, 6, 7, 8, 9, 10},{9, 3, 6})
    ]
)
def test_conjunto_multiplos_tres_params(numeros,multiplos_tres):
    assert conjunto_multiplos_tres(numeros)==multiplos_tres

from src.actividad5 import interseccion_conjuntos
@pytest.mark.parametrize(
    "pares,multiplos_tres,interseccion",
    [
        ({2, 4, 6, 8, 10},{9, 3, 6},{6})
    ]
)
def test_interseccion_conjuntos_params(pares,multiplos_tres,interseccion):
    assert interseccion_conjuntos(pares,multiplos_tres)==interseccion