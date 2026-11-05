notas=[10,8,9,5]
print(notas)
notas.append(20)
notas.insert(1,10)
print(notas)
print(notas[1])
print(len(notas))
print(notas[-1])
print(sum(notas))
print(max(notas))
print(min(notas))
notas.remove(9)
print(notas)
print(sorted(notas))
print(notas[2:])
print(notas[:2])
print(notas[::-1])

#tuplas
meses=("enero","febrero","marzo","mayo","junio","julio","agosto","septiembre",
       "octubre","noviembre", "diciembre")
print(meses[0])
print(meses[-1])
#meses[3]="otro valor"

#diccionarios
estudiante={
    "cedula":"0150749950",
    "nombre":"Daniela Corte",
    "correo":"daniela.corte.est@tecazuay.edu.ec",
    "celular":"0994641381",
    "nota":[10,9,5,4]
}
print(estudiante["nombre"])
print(estudiante.get("nombre"))
print(estudiante.keys())

#conjuntos
conjunto_a={1,1,5,4,6,8}
conjunto_b={1,9,6,5,4}
print(conjunto_a & conjunto_b)
print(conjunto_a | conjunto_b)
