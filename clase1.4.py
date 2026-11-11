#Declaracion de funciones
def saludar():
    print("Hola, Daniela")
saludar()

#Fucnión con parametro

def calcular_edad (anio_nacimiento, anio_actual):
    print("La Edad es: ",anio_actual-anio_nacimiento)
a=int(input("Ingrese su año de nacimiento: "))
b=int(input("Ingrese el año actual: "))
calcular_edad(a,b)