import pytest
from src.actividad6 import encontrar_consonantes
@pytest.mark.parametrize(
    "vocales,consonantes",
    [
        ({'a', 'e', 'i', 'o', 'u'},{'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'})
    ]
)
def test_encontrar_consonantes(vocales,consonantes):
    assert encontrar_consonantes(vocales) == consonantes
from src.actividad6 import encontrar_letras_comunes
@pytest.mark.parametrize(
    "palabra,consonantes,letras_palabra",
    [
        ("hola",{'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'},{'a', 'h', 'l', 'o'})
    ]
)
def test_encontrar_letras_comunes(palabra,consonantes,letras_palabra):
    assert encontrar_letras_comunes(palabra,consonantes) == letras_palabra
