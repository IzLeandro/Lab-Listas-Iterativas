#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 20/10/2020 10:00am 
#Fecha de última Modificación: 22/10/2020 4:28pm
#Versión: 3.8.5

#import de funciones
from Funciones import *

def llamada1():
    var=eval(input("Ingrese una lista: "))
    try:
        print(type(var))
        print(var)
    except:
        print("Verifique que el valor agregado sea una lista.")
        return ""
llamada1()
def menu():
    print("-* Funciones disponibles. *-")
    print("1. Separar listas.")
    print("2. Buscar elementos.")
    print("3. Extryendo vocales.")
    print("4. Lista random.")
    print("5. Agregar en lista.")
    print("6. Eliminar elementos repetidos.")
    print("7. Suceción ULAM.")
    print("8. Alternativos.")
    print("9. Ascendente.")
    print("10. Replicar.")
    print("11. Diferencia de conjuntos.")
    print("12. Unión de conjuntos.")
    print("13. Intercepción de conjuntos.")
    print("14. Multiplicación de listas.")
    entrada= input("Ingrese una opción: ")
    if entrada=="1":
        return