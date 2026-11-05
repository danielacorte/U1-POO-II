for i in range(10):
    print(i)
print("-----------------")
for i in range(2,10):
    print(i)
print("-----------------")
for i in range(2,10,3):
    print(i)
print("-----------------")
for i in range(10,0,-1):
    print(i)
print("-----------------")
#1-100 si es par o impar
for i in range(1,101):
    if i%2==0:
        print(i," Es par")
    else:
        print(i," Es impar")
print("-------------------")
notas=[6,8,9,10,3]
for elemento in notas:
    print(elemento)