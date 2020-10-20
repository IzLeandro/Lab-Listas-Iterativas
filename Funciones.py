def separarElementos(list):
    #variables
    impar=[]
    par=[]
    #comprobacion n1
    if list==[]:
        return ("La lista de números no debe ser vacía.")
    for  elemento in list:
        #comprobacion n2
        if type(elemento) == str:
            return ("Elementos no numericos en lista.")
        if elemento%2==0:
            par=par+[elemento]
        else:
            impar= impar + [elemento]
    return [par,impar]

def buscarElemento(list,find=None):
    #variables
    res=0
    #validaciones
    if find==None:
        return ('Debe indicar el numero que desea buscar.')
    for elemento in list:
        if elemento == find:
            res+=1
    return res

