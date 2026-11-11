#Declaracion de funciones
def saludar():
    print("Hola, Daniela")
saludar()

#Función con parametro

def calcular_edad (anio_nacimiento, anio_actual):
    print("La Edad es: ",anio_actual-anio_nacimiento)
a=int(input("Ingrese su año de nacimiento: "))
b=int(input("Ingrese el año actual: "))
calcular_edad(a,b)

#Funciones con retorno
def calacular_iva(precio,iva):
    return precio*iva
resultado=calacular_iva(10,0.15)
print("El IVA es: ",resultado)

def calacular_iva(precio,iva=0.15):
    return precio*iva
resultado=calacular_iva(100)
print("El IVA es: ",resultado)

resultado=calacular_iva(100,0.14)
print("El IVA es: ",resultado)

#Funciones con listas
def calcular_par(numeros):
    for n in numeros:
        if n%2==0:
            print("El numero ",n," es par")
        else:
            print("El numero ",n," es impar")
lista_numeros=range(0,1000,2)
calcular_par(lista_numeros)
lista_numeros=range(5,0,-1)
for e in lista_numeros: 
    print(e,end=" ")

#Funciones con tuplas
def suma_numeros(*a):
    return sum(a)
print("La suma es: ",suma_numeros(1,2,3))

#Funciones con diccionarios
def estudiantes(**lista_estudiantes):
    suma_total=0
    for nombre,edad in lista_estudiantes.items():
        print("El estudiante",nombre,"tiene", edad,"años")
        suma_total+=edad
    print("El total de edades es: ",suma_total)
estudiantes(Veronica=20, Juan=25,Maria=30,Pablo=21,Domenica=20,Karen=20,Pedro=21)


