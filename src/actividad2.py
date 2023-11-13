def crear_lista(lista_primaria,lista_secundaria):
    union_lista=lista_primaria.union(lista_secundaria)
    interseccion_lista=lista_primaria.intersection(lista_secundaria)
    diferencia_lista=lista_primaria.difference(lista_secundaria)
    comprobar_lista=lista_secundaria.isdisjoint(lista_primaria)
    lista=str(union_lista)+"\n"+str(interseccion_lista)+"\n"+str(diferencia_lista)+"\n"+str(comprobar_lista)
    return lista

if __name__=="__main__":
    lista_primaria=frozenset()
    lista_secundaria=frozenset()
    if lista_primaria!='x':
        alumno_primaria=input("introduce el nombre un alumno de primaria: ")
        while alumno_primaria!="x":
            lista_primaria.add(alumno_primaria)
            alumno_primaria=input("introduce el nombre un alumno de primaria: ")
    if lista_secundaria!='x':
        alumno_secundaria=input("introduce el nombre un alumno de secundaria: ")
        while alumno_secundaria!="x":
            lista_secundaria.add(alumno_secundaria)
            alumno_secundaria=input("introduce el nombre un alumno de secundaria: ")
    lista=crear_lista(lista_primaria,lista_secundaria)
    print(lista)