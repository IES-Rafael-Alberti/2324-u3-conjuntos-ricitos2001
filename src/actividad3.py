def conjunto_potencia(s):
    elementos = list(s)
    total_elementos = len(elementos)
    total_subconjuntos = 1 << total_elementos
    potencia = [set() for _ in range(total_subconjuntos)]
    for subconjunto_numero in range(total_subconjuntos):
        for elemento_numero in range(total_elementos):
            if (subconjunto_numero >> elemento_numero) & 1:
                potencia[subconjunto_numero].add(elementos[elemento_numero])
    return potencia

if __name__ == "__main__":
    # Entrada
    conjunto_original = {4, 1, 6}
    # Proceso
    lista_potencia = conjunto_potencia(conjunto_original)
    # Salida
    print(lista_potencia)