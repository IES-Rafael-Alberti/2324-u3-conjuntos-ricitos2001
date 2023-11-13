def crear_lista_frutas(frutas_comunes,frutas_solo_en_frutas1,frutas_solo_en_frutas2):
    lista_frutas=str(frutas_comunes)+"\n"+str(frutas_solo_en_frutas1)+"\n"+str(frutas_solo_en_frutas2)
    return lista_frutas

if __name__=="__main__":
    frutas1 = ["manzana", "pera", "naranja", "platano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandia", "uva"]
    set_frutas1=set(frutas1)
    set_frutas2=set(frutas2)
    frutas_comunes=set_frutas1.intersection(set_frutas2)
    frutas_solo_en_frutas1=set_frutas1.difference(set_frutas2)
    frutas_solo_en_frutas2=set_frutas2.difference(set_frutas1)
    lista_frutas=crear_lista_frutas(frutas_comunes,frutas_solo_en_frutas1,frutas_solo_en_frutas2)
    print(lista_frutas)
