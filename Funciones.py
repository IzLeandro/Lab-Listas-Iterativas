#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 20/10/2020 10:00am 
#Fecha de última Modificación: 20/10/2020 4:28pm
#Versión: 3.8.5

#importaciones
import random
#Funciones
#Reto 1. Separar Listas
def separarListas(list):
    """
        Funcionamiento:retorna una lista con dos sublistas, la primera de ellas contiene todos los números pares y la segunda los números impares. 
        Entradas: list(list) lista numérica
        Salidas: lista con dos sublistas (list). 
    """
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
#Reto 2. Buscar Elemento. 
def buscarElemento(list,find=None):
    """
        Funcionamiento:determina cuántas veces aparece un número en una lista 
        Entradas: list(list) lista numérica, find(int) número a encontrar
        Salidas: cantidad de veces que aparece el número (int). 
    """
    res=0
    if find==None:    #validaciones
        return ('Debe indicar el numero que desea buscar.')
    for elemento in list:
        if elemento == find:
            res+=1
    return res
#Reto 3. Extrayendo Vocales.
def crearListaVocales(list):
    """
        Funcionamiento: crea una nueva lista que contiene solo las vocales de la lista recibida
        Entradas: list(list) lista de letras
        Salidas: lista que contiene solo las vocales de la lista recibida (list). 
    """
    consVocales=['a','e','i','o','u']
    resultVocales=[]
    for elemento in list:
        if type(elemento) != str: #comprobacion
            return 'La lista solo debe contener letras'
        if elemento in consVocales:
            resultVocales=resultVocales+[elemento]
    return resultVocales
#Reto 4. Lista Random.
def crearLista(num):
    """
        Funcionamiento: crea una lista con la cantidad de elementos numéricos random
        Entradas: num(int) cantidad de números de la lista a formar
        Salidas: la lista, el mayor de la lista, el menor de la lista y la diferencia entre los dos 
    """
    lista=[]
    while num!=0:
        lista=lista + [random.randint(1,99)]
        num-=1
    print("Se generó la lista",lista,", El mayor es:", max(lista) ,"El menor es:", min(lista) ,"y hay una diferencia de:",(max(lista)-min(lista)))
    return ""
#Reto 5. Agregar en lista.
def insertarElemento(elem1,elem2,lista):
    """
        Funcionamiento: crea una nueva lista que cada vez que aparece el elemento 1 en la lista original agrega inmediatamente un elemento 2 a la lista nueva
        Entradas: elem1(str) elemento 1, elem2(str) elemento 2, lista(list) lista de strings
        Salidas: nuevalista(list) lista con los nuevos elementos
    """
    nuevaLista=[]
    for i in lista:
        nuevaLista= nuevaLista + [i]
        if i == elem1:
            nuevaLista = nuevaLista + [elem2]
    return nuevaLista
#Reto 6. Eliminar elementos repetidos 
def eliminarRepetidos(lista):
    """
        Funcionamiento: remueve de una lista dada, los elementos repetidos, dejando una única aparición del elemento.
        Entradas: lista(list) lista de letras o números
        Salidas: nuevalista(list) lista sin los elementos repetidos
    """
    nuevaLista=[]
    for i in lista:
        if i not in nuevaLista:
            nuevaLista= nuevaLista + [i]
    return nuevaLista
#Reto 7 - Sucesión de ULAM
def sucesionUlam(num):
    """
        Funcionamiento: reciba un número entero positivo mayor que 0 y retorne la sucesión de Ulam
        Entradas: num(int) número entero
        Salidas: lista(list) lista con la sucesión Ulam
    """
    lista=[num]
    if num<=0:
        return "El numero debe ser mayor que 0"
    while num!=1:
        if num%2==0:
            num=num/2
        else:
            num=(num*3) + 1
        lista=lista + [int(num)]
    return lista
#Reto 8 - Alternativos
def esPar(num):
    """
        Funcionamiento: dice si un número es par o no
        Entradas: num(int) número entero
        Salidas: True o False(bool) 
    """
    if num%2==0: 
        return True
    return False
def alternada(list):
    """
        Funcionamiento:  verifica si los elementos de una lista son alternados entre pares e impares.
        Entradas: list(list) lista numérica
        Salidas: True o False(bool) 
    """
    for i in range(0,len(list)-1):
        if esPar(list[i]):
            if esPar(list[i+1]):
                return False
        if esPar(list[i])==False:
            if esPar(list[i+1])==False:
                return False
    return True
#Reto 9 Ascendente
def listaAscendente(list):
    """
        Funcionamiento: recibe una lista y devuelve True si los elementos de la lista están en orden ascendiente y False en caso contrario. 
        Entradas: list(list) lista numérica
        Salidas: True o False(bool) 
    """
    for i in range(0,len(list)-1):
         if list[i]>list[i+1]:
             return False
    return True
#Reto 10 Replicar
def replicar(list,num):
    """
        Funcionamiento: replica los elementos de una lista una cantidad n de veces
        Entradas: list(list) lista numérica, num(int) cantidad de veces a replicar los elementos
        Salidas: newlist(list) lista con los elementos replicados
    """
    newlist=[]
    for elemento in list:
        newlist+=[elemento]*num
    return newlist
#Reto 11 Diferencia de Conjuntos
def difConjuntos(list1,list2):
    """
        Funcionamiento: resta dos listas de numeros haciendo otra lista con los números restantes
        Entradas: list1(list) lista numérica, list2(list) lista numérica
        Salidas: newlist1(list) lista con los elementos que quedaron, newlist2(list) lista con los elementos que quedaron
    """ 
    newlist1=[]
    newlist2=[]
    for elemento in list1:
        if elemento not in list2:
            newlist1+=[elemento]
    for elemento in list2:
        if elemento not in list1:
            newlist2+=[elemento]      
    print('A-B')
    print(newlist1)
    print('B-A')
    print(newlist2)
    return ''
#Reto 12 Unión de Conjuntos
def unionConjuntos(list1,list2):
    """
        Funcionamiento: Recibe dos listas de números enteros y los une en una sola lista sin duplicados
        Entradas: list1(list) lista numérica, list2(list) lista numérica
        Salidas: newlist(list) lista de los elementos de las listas originales unidos sin duplicados
    """ 
    newlist=[]
    for elemento in list1:
        if elemento not in newlist:
            newlist+=[elemento]
    for elemento in list2:
        if elemento not in newlist:
            newlist+=[elemento]  
    return newlist
#Reto 13 – Intercepción de Conjuntos 
def intercepcionConjuntos(list1,list2):
    """
        Funcionamiento: recibe como entrada dos listas de números enteros positivos y que retorna la intersección de ambas listas
        Entradas: list1(list) lista numérica, list2(list) lista numérica
        Salidas: newlist(list) lista con los elementos comunes de las listas originales
    """ 
    newlist=[]
    for elemento in list1:
        if elemento in list2 and elemento not in newlist:
            newlist+=[elemento]
    for elemento in list2:
        if elemento in list1 and elemento not in newlist:
            newlist+=[elemento]  
    return newlist
#Reto 14 – Multiplicación de Listas
def multiplicarListas(list1,list2):
    """
        Funcionamiento: multiplica los elementos de dos listas
        Entradas: list1(list) lista numérica, list2(list) lista numérica
        Salidas: newlist(list) lista con los elementos comunes de las listas originales o un string que dice que las listas son de diferente tamaño
    """ 
    newlist=[]
    if len(list1)!=len(list2):
        return 'Las listas son de diferente tamaño'
    for i in range(0,len(list1)):
        newlist+=[list1[i]*list2[i]]
    return newlist
