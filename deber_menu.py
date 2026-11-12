def pre1():
    print(int(9.99))
def pre2():
    frase = "aprendo Python en TEC"
    print(len(frase.split()))
def pre3():
    datos = (10, 20, 30)
    datos[1] = 99
    print(datos)
def pre4():
    print("ab" * 3)
def pre5():
    a = [1, 2, 3]
    b = a
    b[0] = 5
    print(a)
def pre6():
    for x in [2, 4, 6]:
        if x == 7:
            print("Encontrado")
            break
    else:
        print("No encontrado")
def pre7():
    saldo = 350
    if saldo >= 1000:
        print("Oro")
    elif saldo >= 100:
        print("Plata")
    else:
        print("Básica")
def pre8():
    print([n ** 2 for n in [1, 2, 3, 4] if n % 2 == 0])
def pre9():
    total = 0
    n = 1
    while n <= 5:
        total += n
        n += 1
    print(total)
def pre10():
    for i in range(3):
        for j in range(2):
            print("*", end="")
def pre11():
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
def mostrar_preguntas():
    print("-"*40)
    print("-" * 10, "Menú de Preguntas: ", "-" * 10)
    
    print("1. ¿Qué imprime el siguiente código? ")
    print(" "*5,"print(int(9.99))")
    print("2. ¿Qué imprime el siguiente código?")
    print(" "*5,"frase =","aprendo Python en TEC")
    print(" "*5,"print(len(frase.split()))")
    
    print("3. ¿Qué ocurre al ejecutar el siguiente código?")
    print(" "*5,"datos = (10, 20, 30)")
    print(" "*5,"datos[1] = 99")
    print(" "*5,"print(datos)")
    print("4. ¿Qué imprime el siguiente código?")
    print(" "*5,'print("ab" * 3)')
    
    print("5. ¿Qué imprime el siguiente código? ")
    print(" "*5,'a = [1, 2, 3]')
    print(" "*5,'b = a')
    print(" "*5,'b[0] = 5')
    print(" "*5,'print(a)')
    
    print("6. ¿Qué imprime el siguiente código? ")
    print(" "*5,'for x in [2, 4, 6]:')
    print(" "*9,'if x == 7:')
    print(" "*13,'print("Encontrado")')
    print(" "*13,'break')
    print(" "*5,'else:')
    print(" "*9,'print("No encontrado")')
    
    print("7. ¿Qué imprime el siguiente código? ")
    print(" "*5,'saldo = 350')
    print(" "*5,'if saldo >= 1000:')
    print(" "*9,'print("Oro")')
    print(" "*5,'elif saldo >= 100:')
    print(" "*9,'print("Plata")')
    print(" "*5,'else:')
    print(" "*9,'print("Básica")')
    
    print("8.¿Qué imprime el siguiente código? ")
    print(" "*5,'print([n ** 2 for n in [1, 2, 3, 4] if n % 2 == 0])')
                
    print("9. ¿Qué imprime el siguiente código?")
    print(" "*5,'total = 0')
    print(" "*5,'n = 1')
    print(" "*5,'while n <= 5:')
    print(" "*9,'total += n')
    print(" "*9,'n += 1')
    print(" "*5,'print(total)')
    
    print("10. ¿Cuántas veces se imprime «*» en el siguiente código?")
    print(" "*5,'for i in range(3):')
    print(" "*9,'for j in range(2):')
    print(" "*13,'print("*", end="")')
    
    print("11. Ejercicio de Pares e impares")
    print(" "*5,'Pida números enteros con input() hasta que el usuario escriba fin. ')
    print(" "*5,'Guárdelos en una lista y luego, con comprensiones, cree una lista de pares y otra de impares.')
    print(" "*5,'Muestre ambas listas, ordenadas, y la suma de cada una.')
    print(" "*5,'Escriba su codigo')
    print("12. Regresar al menú principal")
    

while True:
    
    print("*"*40)
    print("\nMenú de Usuario")
    print("1. Ingrese su nombre")
    print("2. Menú de preguntas")
    print("3. Salir")

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        nombre = input("Ingrese su nombre: ")
        print("Bienvenid@,", nombre)
    elif opcion == 2:
        while True:
            mostrar_preguntas()
            opcion=int(input("Ingrese una opcion: "))
            if opcion ==1:
                pre1()
            elif opcion==2:
                pre2()
            elif opcion==3:
                pre3()
            elif opcion==4:
                pre4()
            elif opcion==5:
                pre5()
            elif opcion==6:
                pre6()
            elif opcion==7:
                pre7()
            elif opcion==8:
                pre8() 
            elif opcion==9:
                pre9() 
            elif opcion==10:
                pre10()
            elif opcion==11:
                pre11()
            elif opcion==12:
                print("Regresando...")
                break
            else:
                print("Opcion invalida")
            input("\nPresione Enter para continuar...")
    elif opcion == 3:
        print("Saliendo del programa...")
        break
    else:
        print("Opcion invalida")