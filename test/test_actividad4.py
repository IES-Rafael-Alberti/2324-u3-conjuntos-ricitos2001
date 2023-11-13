'''import pytest
from src.actividad4 import crear_lista_frutas
@pytest.mark.parametrize(
    "frutas_comunes,frutas_solo_en_frutas1,frutas_solo_en_frutas2,lista_frutas",
    [
        ({'manzana', 'pera', 'uva'},{'platano', 'naranja'},{'sandia', 'durazno'},"{'manzana', 'pera', 'uva'}\n{'platano', 'naranja'}\n{'sandia', 'durazno'}")
    ]
)
def test_crear_lista_frutas_params(frutas_comunes,frutas_solo_en_frutas1,frutas_solo_en_frutas2,lista_frutas):
    assert crear_lista_frutas(frutas_comunes,frutas_solo_en_frutas1,frutas_solo_en_frutas2)==lista_frutas'''