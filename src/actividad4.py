'''Ejercicio 3.3.4: dadas las siguientes listas:
frutas1 = "["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
1.) Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.
2.) Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes.
3.) Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1.
4.) Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2.'''
# definicion de la funcion
def conjunto_frutas_comunes(set_frutas1,set_frutas2):
    frutas_comunes=set_frutas1.intersection(set_frutas2)
    return frutas_comunes

def conjunto_frutas_solo_en_frutas1(set_frutas1,set_frutas2):
    frutas_solo_en_frutas1=set_frutas1.difference(set_frutas2)
    return frutas_solo_en_frutas1

def conjunto_frutas_solo_en_frutas2(set_frutas1,set_frutas2):
    frutas_solo_en_frutas2=set_frutas2.difference(set_frutas1)
    return frutas_solo_en_frutas2

if __name__=="__main__":
    # entrada
    frutas1 = ["manzana", "pera", "naranja", "platano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandia", "uva"]
    set_frutas1=set(frutas1)
    set_frutas2=set(frutas2)
    # procesamiento
    frutas_comunes=conjunto_frutas_comunes(set_frutas1,set_frutas2)
    frutas_solo_en_frutas1=conjunto_frutas_solo_en_frutas1(set_frutas1,set_frutas2)
    frutas_solo_en_frutas2=conjunto_frutas_solo_en_frutas2(set_frutas1,set_frutas2)
    # salida
    print(frutas_comunes)
    print(frutas_solo_en_frutas1)
    print(frutas_solo_en_frutas2)
    
