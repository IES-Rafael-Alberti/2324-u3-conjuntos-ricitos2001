import pytest
from src.actividad3 import conjunto_potencia
@pytest.mark.parametrize(
    "conjunto,potencia",
    [
        ({6, 1, 4},[set(), {1}, {4}, {1, 4}, {6}, {1, 6}, {4, 6}, {1, 4, 6}])
    ]
)


def test_conjunto_potencia(conjunto,potencia):
    assert conjunto_potencia(conjunto)==potencia