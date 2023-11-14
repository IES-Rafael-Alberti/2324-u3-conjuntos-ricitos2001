def obtener_domicilios(ventas):
    domicilios=set()
    for venta in ventas:
        domicilios.add(venta[3])
    return domicilios

if __name__=="__main__":
    ventas=[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]
    domicilios=obtener_domicilios(ventas)
    print(domicilios)