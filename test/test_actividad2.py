import pytest
from src.actividad2 import crear_lista
@pytest.mark.parametrize(
    "lista_primaria,lista_secundaria,lista",
    [
        ({'cesar', 'ana'},{'cesar'},"{'cesar', 'ana'}\n{'cesar'}\n{'ana'}\nFalse")
    ]
)

def test_crear_lista_params(lista_primaria,lista_secundaria,lista):
    assert crear_lista(lista_primaria,lista_secundaria)==lista

