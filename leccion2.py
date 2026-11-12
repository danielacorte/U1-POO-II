#leccion2
#Pregunta 1
print(int(9.99))
#Pregunta2
frase = "aprendo Python en TEC"
print(len(frase.split()))
#Pregunta 3
datos = (10, 20, 30)
datos[1] = 99
print(datos)
#Pregunta 4
print("ab" * 3)
#Pregunta 5
a = [1, 2, 3]
b = a
b[0] = 5
print(a)
#Pregunta 6
for x in [2, 4, 6]:
    if x == 7:
        print("Encontrado")
        break
else:
    print("No encontrado")
#Pregunta7
saldo = 350
if saldo >= 1000:
    print("Oro")
elif saldo >= 100:
    print("Plata")
else:
    print("Básica")
#Pregunta8
print([n ** 2 for n in [1, 2, 3, 4] if n % 2 == 0])
#Pregunta9
total = 0
n = 1
while n <= 5:
    total += n
    n += 1
print(total)
#Pregunta10
for i in range(3):
    for j in range(2):
        print("*", end="")
#Pregunta11
numeros = []
# Escriba su solución aquí
while True: 
    ingreso=(input("Ingrese un número: "))
    if ingreso=="fin":
         break
    numeros.append(int(ingreso))
    pares=[num for num in numeros if num %2 ==0]
    impares=[num for num in numeros if num%2!=0]
    pares.sort()
    impares.sort()
    print("Numeros Pares: ", pares)
    print("La suma de los Numeros Pares es: ",sum(pares))
    print("Numeros Impares: ",impares)
    print("La suma de los Numeros Impares es: ",sum(impares))

