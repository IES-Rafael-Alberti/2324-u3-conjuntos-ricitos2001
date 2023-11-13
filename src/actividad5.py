'''def crear_interseccion(pares,multiplosdetres):
    interseccion=pares&multiplosdetres
    return interseccion

if __name__=="__main__":
#    numeros={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    pares={2, 4, 6, 8, 10}
    multiplosdetres={3, 6, 9}
    interseccion=crear_interseccion(pares,multiplosdetres)
    print (interseccion)'''



def conjunto_pares(numeros):
    pares = {num for num in numeros if num % 2 == 0}
    return pares

def multiplos_tres(numeros):
    multiplos_de_tres = {num for num in numeros if num % 3 == 0}
    return multiplos_de_tres

def interseccion_pares_multiplos(numeros):
    numeros_pares = conjunto_pares(numeros)
    numeros_mult_tres = multiplos_tres(numeros)
    pares_y_multiplos_de_tres = numeros_pares.intersection(numeros_mult_tres)
    return pares_y_multiplos_de_tres

if __name__ == "__main__":
    # Entrada
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    # Proceso
    pares = conjunto_pares(numeros)
    multiplos = multiplos_tres(numeros)
    interseccion = interseccion_pares_multiplos(numeros)
    # Salida
    print("Números pares:", pares)
    print("Números múltiplos de tres:", multiplos)
    print("Intersección entre pares y múltiplos de tres:", interseccion)