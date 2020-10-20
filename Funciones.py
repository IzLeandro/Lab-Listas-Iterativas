#importaciones
import random
def separarElementos(list):
    #variables
    impar=[]
    par=[]
    if list==[]:    #comprobacion n1
        return ("La lista de números no debe ser vacía.")
    for  elemento in list:
        if type(elemento) == str:        #comprobacion n2
            return ("Elementos no numericos en lista.")
        if elemento%2==0:
            par=par+[elemento]
        else:
            impar= impar + [elemento]
    return [par,impar]

def buscarElemento(list,find=None):
    #variables
    res=0
    if find==None:    #validaciones
        return ('Debe indicar el numero que desea buscar.')
    for elemento in list:
        if elemento == find:
            res+=1
    return res

def crearListaVocales(list):
    #variables
    consVocales=['a','e','i','o','u']
    resultVocales=[]
    for elemento in list:
        if type(elemento) != str: #comprobacion
            continue
        if elemento in consVocales:
            resultVocales=resultVocales+[elemento]
    return resultVocales

def crearLista(num):
    #variables
    lista=[]
    while num!=0:
        lista=lista + [random.randint(1,99)]
        num-=1
    print("Se generó la lista",lista,", El mayor es:", max(lista) ,"El menor es:", min(lista) ,"y hay una diferencia de:",(max(lista)-min(lista)))
    return ""

def insertarElemento(elem1,elem2,lista):
    #variables
    nuevaLista=[]
    for i in lista:
        nuevaLista= nuevaLista + [i]
        if i == elem1:
            nuevaLista = nuevaLista + [elem2]
    return nuevaLista

def eliminarRepetidos(lista):
    #variables
    nuevaLista=[]
    for i in lista:
        if i not in nuevaLista:
            nuevaLista= nuevaLista + [i]
    return nuevaLista

def sucesionUlam(num):
    #variables
    lista=[num]
    if num<=0:
        return "El numero debe ser mayor que 0"
    while num!=1:
        if num%2==0:
            num=num/2
            lista=lista + [int(num)]
        else:
            num=(num*3) + 1
            lista=lista + [int(num)]
    return lista

