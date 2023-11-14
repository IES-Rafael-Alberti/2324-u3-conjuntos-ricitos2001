'''Escriba la función conjunto_potencia(s) que reciba como parámetro un conjunto cualquiera por ejemplo: "s={6, 1, 4}" y retorne su lista potencia que es la lista de todos sus subconjuntos'''
# definicion de la funcion
def conjunto_potencia(conjunto):
    elementos = list(conjunto)
    total_elementos = len(elementos)
    total_subconjuntos = 1 << total_elementos
    potencia = [set() for _ in range(total_subconjuntos)]
    for numero_subconjunto in range(total_subconjuntos):
        for numero_elemento in range(total_elementos):
            nombre_temporal=(numero_subconjunto >> numero_elemento)
            nombre_temporal_2=(nombre_temporal) & 1
            if (nombre_temporal_2):
                potencia[numero_subconjunto].add(elementos[numero_elemento])
    return potencia

if __name__ == "__main__":
    # Entrada
    conjunto=frozenset({6, 1, 4})
    # procesamiento
    potencia=conjunto_potencia(conjunto)
    # Salida
    print(potencia)