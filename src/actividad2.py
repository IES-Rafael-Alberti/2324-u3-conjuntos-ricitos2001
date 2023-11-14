'''Ejercicio 3.3.2¶
Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, finalizando cuando se introduzca “x”. A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.
1.) Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
2.) Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
3.) Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
4.) Mostrar si todos los nombres de primaria están incluidos en secundaria.'''
# definicion de la funcion
def unir_conjuntos(lista_primaria,lista_secundaria):
    union=lista_primaria.union(lista_secundaria)
    return union

def intersectar_conjuntos(lista_primaria,lista_secundaria):
    interseccion=lista_primaria.intersection(lista_secundaria)
    return interseccion

def diferenciar_conjuntos(lista_primaria,lista_secundaria):
    diferencia=lista_primaria.difference(lista_secundaria)
    return diferencia

def comprobar_conjuntos(lista_primaria,lista_secundaria):
    comprobacion=lista_secundaria.isdisjoint(lista_primaria)
    return comprobacion

if __name__=="__main__":
    # entrada
    conjunto_primaria=set()
    conjunto_secundaria=set()
    if conjunto_primaria!='x':
        alumno_primaria=input("introduce el nombre un alumno de primaria: ")
        while alumno_primaria!="x":
            conjunto_primaria.add(alumno_primaria)
            alumno_primaria=input("introduce el nombre un alumno de primaria: ")
    if conjunto_secundaria!='x':
        alumno_secundaria=input("introduce el nombre un alumno de secundaria: ")
        while alumno_secundaria!="x":
            conjunto_secundaria.add(alumno_secundaria)
            alumno_secundaria=input("introduce el nombre un alumno de secundaria: ")
    # procesamiento
    union=unir_conjuntos(conjunto_primaria,conjunto_secundaria)
    interseccion=intersectar_conjuntos(conjunto_primaria,conjunto_secundaria)
    diferencia=diferenciar_conjuntos(conjunto_primaria,conjunto_secundaria)
    comprobacion=comprobar_conjuntos(conjunto_primaria,conjunto_secundaria)
    # salida
    print(union)
    print(interseccion)
    print(diferencia)
    print(comprobacion)