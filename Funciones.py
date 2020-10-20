def separarElementos(list):
    #variables
    impar=[]
    par=[]
    #comprobacion
    if list==[]:
        return ("La lista de números no debe ser vacía.")
    for  elemento in list:
        if type(elemento) == str:
            return ("Elementos no numericos en lista")
        if elemento%2==0:
            par=par+[elemento]
        else:
            impar= impar + [elemento]
    return [par,impar]

print(separarElementos([2,4,6,8]))