'''Dado el conjunto de números enteros:
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
1.) Crea un conjunto pares que contenga los números pares del conjunto numeros.
2.) Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
3.) Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres.'''
# definicion de la funcion
def conjunto_pares(numeros):
    pares={num for num in numeros if num % 2 == 0}
    return pares

def conjunto_multiplos_tres(numeros):
    multiplos_tres={num for num in numeros if num % 3 == 0}
    return multiplos_tres

def interseccion_conjuntos(pares,multiplos_tres):
    interseccion=pares.intersection(multiplos_tres)
    return interseccion

if __name__ == "__main__":
    # Entrada
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    # Proceso
    pares = conjunto_pares(numeros)
    multiplos_tres = conjunto_multiplos_tres(numeros)
    interseccion = interseccion_conjuntos(pares,multiplos_tres)
    # Salida
    print(pares)
    print(multiplos_tres)
    print(interseccion)