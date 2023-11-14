'''Dado el conjunto de letras:
vocales = {'a', 'e', 'i', 'o', 'u'}
1.) Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
2.) Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto vocales como en el conjunto consonantes.'''
# definicion de la funcion
def encontrar_consonantes(vocales):
    alfabeto = set('abcdefghijklmnopqrstuvwxyz')
    consonantes = alfabeto - vocales
    return consonantes

def encontrar_letras_comunes(palabra, consonantes):
    letras_palabra = set(letra for letra in palabra)
    letras_palabra.intersection(consonantes)
    return letras_palabra

if __name__ == "__main__":
    # entrada
    vocales = {'a', 'e', 'i', 'o', 'u'}
    palabra = input("Introduce una palabra: ").lower()
    # procesamiento
    consonantes = encontrar_consonantes(vocales)
    letras_palabra=encontrar_letras_comunes(palabra, consonantes)
    # salida
    print(consonantes)
    print(letras_palabra)
