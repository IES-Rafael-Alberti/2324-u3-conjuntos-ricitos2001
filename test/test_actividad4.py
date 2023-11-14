import pytest
from src.actividad4 import conjunto_frutas_comunes
@pytest.mark.parametrize(
    "set_frutas1,set_frutas2,frutas_comunes",
    [
        ({'pera', 'manzana', 'platano', 'naranja', 'uva'},{'pera', 'manzana', 'uva', 'sandia', 'durazno'},{'pera', 'manzana', 'uva'})
    ]
)
def test_conjunto_frutas_comunes_params(set_frutas1,set_frutas2,frutas_comunes):
    assert conjunto_frutas_comunes(set_frutas1,set_frutas2)==frutas_comunes

from src.actividad4 import conjunto_frutas_solo_en_frutas1
@pytest.mark.parametrize(
    "set_frutas1,set_frutas2,frutas_solo_en_frutas1",
    [
        ({'pera', 'manzana', 'platano', 'naranja', 'uva'},{'pera', 'manzana', 'uva', 'sandia', 'durazno'},{'platano', 'naranja'})
    ]
)
def test_conjunto_frutas_solo_en_frutas1_params(set_frutas1,set_frutas2,frutas_solo_en_frutas1):
    assert conjunto_frutas_solo_en_frutas1(set_frutas1,set_frutas2)==frutas_solo_en_frutas1
    
from src.actividad4 import conjunto_frutas_solo_en_frutas2
@pytest.mark.parametrize(
    "set_frutas1,set_frutas2,frutas_solo_en_frutas2",
    [
        ({'pera', 'manzana', 'platano', 'naranja', 'uva'},{'pera', 'manzana', 'uva', 'sandia', 'durazno'},{'sandia', 'durazno'})
    ]
)
def test_conjunto_frutas_solo_en_frutas2_params(set_frutas1,set_frutas2,frutas_solo_en_frutas2):
    assert conjunto_frutas_solo_en_frutas2(set_frutas1,set_frutas2)==frutas_solo_en_frutas2