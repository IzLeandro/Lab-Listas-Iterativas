#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 20/10/2020 10:00am 
#Fecha de última Modificación: 22/10/2020 4:28pm
#Versión: 3.8.5
#import de funciones
from Funciones import *
#Funciones
def llamada1():
    entrada=[]
    try:
        entrada=eval(input("\nIngrese una lista: "))
    except:
        print("Verifique que el valor ingresado sea una lista.")
        return ""
    if type(entrada)!=list:
        print("Verifique que el valor ingresado sea una lista.")
        return ""
    print(separarListas(entrada))
    return ""

def llamada2():
    numero=None
    entrada=[]
    try:
        entrada=eval(input("\nIngrese una lista: "))
        numero=eval(input("\nIngrese el digito a buscar: "))
    except:
        if numero==None:
            print("Debe indicar el digito que desea buscar.")
            return ""
        print("Verifique que el primer valor ingresado sea una lista.")
        return ""
    if type(entrada)!=list:
        print("Verifique que el primer valor ingresado sea una lista.")
        return ""
    if type(numero)!=int:
        print("Verifique que el primer valor ingresado sea un numero entero.")
    print("El numero",numero,"aparece",buscarElemento(entrada,numero),"veces.")
    return ""

def llamada3():
    try:
        entrada=eval(input("\nIngrese una lista: "))
    except:
        print("Verifique que el valor ingresado sea una lista.")
        return ""
    if type(entrada)!=list:
        print("Verifique que el valor ingresado sea una lista.")
        return ""
    print(crearListaVocales(entrada))
    return ""

def llamada4():
    entrada=eval(input("\nIngrese numero: "))
    if type(entrada)!=int:
        print("El valor ingresado no es un numero entero.")
        return
    print(crearLista(entrada))
    return ""

def llamada5():
    try:
        entrada=eval(input("\nIngrese el primer elemento: "))
        nuevo=eval(input("\nIngrese el nuevo elemento: "))
        lista=eval(input("\nIngrese la lista: "))
    except:
        print("existe un error con los datos ingresados, recuerde utilizar comillas (\"\") para ingresar texto.")
        return ""
    if type(lista)!=list:
        print("La lista contiene un error.")
        return ""
    print(insertarElemento(entrada,nuevo,lista))
    return ""

def llamada6():
    try:
        entrada=eval(input("\nIngrese una lista: "))
    except:
        print("existe un error con los datos ingresados, recuerde utilizar comillas (\"\") para ingresar texto.")
        return ""
    if type(entrada)!=list:
        print("Debe ingresar una lista.")
        return ""
    print(eliminarRepetidos(entrada))
    return ""

def llamada7():
    try:
        entrada=eval(input("\nIngrese el numero: "))
    except:
        print("existe un error con los datos ingresados, recuerde utilizar comillas (\"\") para ingresar texto.")
        return ""
    if type(entrada)!=int:
        print("Debe ingresar un numero entero.")
        return ""
    print(sucesionUlam(entrada))
    return ""

def menu():
    print("-* Funciones disponibles. *-")
    print("1. Separar listas.")
    print("2. Buscar elementos.")
    print("3. Extryendo vocales.")
    print("4. Lista random.")
    print("5. Agregar en lista.")
    print("6. Eliminar elementos repetidos.")
    print("7. Suceción ULAM.")#terminado hasta aca
    print("8. Alternativos.")
    print("9. Ascendente.")
    print("10. Replicar.")
    print("11. Diferencia de conjuntos.")
    print("12. Unión de conjuntos.")
    print("13. Intercepción de conjuntos.")
    print("14. Multiplicación de listas.")
    print("             -* *-")
    entrada= input("Ingrese una opción: ")
    if entrada=="1":
        llamada1()
        input("Presione una tecla para continuar...")
        return ""
    if entrada=="2":
        llamada2()
        input("Presione una tecla para continuar...")
        return ""
    if entrada=="3":
        llamada3()
        input("Presione una tecla para continuar...")
        return ""
    if entrada=="4":
        llamada4()
        input("Presione una tecla para continuar...")
        return ""
    if entrada=="5":
        llamada5()
        input("Presione una tecla para continuar...")
        return ""
    if entrada=="6":
        llamada6()
        input("Presione una tecla para continuar...")
        return ""
    if entrada=="7":
        llamada7()
        input("Presione una tecla para continuar...")
        return ""
menu()