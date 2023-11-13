def encontrar_consonantes(vocales):
    alfabeto = set('abcdefghijklmnopqrstuvwxyz')
    consonantes = alfabeto - vocales
    return consonantes

def encontrar_letras_comunes(palabra, consonantes):
    letras_palabra = set(letra for letra in palabra)
    letras_palabra.intersection(consonantes)
    return letras_palabra

if __name__ == "__main__":
    # Entrada
    vocales = {'a', 'e', 'i', 'o', 'u'}
    palabra = input("Introduce una palabra: ").lower()
    # Procesamiento
    consonantes = encontrar_consonantes(vocales)
    letras_palabra=encontrar_letras_comunes(palabra, consonantes)
    # Salida
    print(consonantes)
    print(letras_palabra)
