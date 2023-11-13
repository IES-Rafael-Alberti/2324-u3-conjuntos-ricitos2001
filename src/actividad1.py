'''if __name__=="__main__":
    clientes=[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]
    for cliente in clientes:
        print (cliente)
    # monto = precio (tercer valor de la tupla)'''

def obtener_domicilios_compra(lista_compras):
    domicilios = {}
    for compra in lista_compras:
        cliente, mes, monto, domicilio = compra
        domicilios[cliente] = domicilio
    return list(domicilios.values())

if __name__ == "__main__":
    # Entrada (lista de las compras)
    compras = [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]
    # Proceso
    domicilios_unicos = obtener_domicilios_compra(compras)
    # Salida
    print(domicilios_unicos)