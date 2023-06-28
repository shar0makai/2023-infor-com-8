oracion = input("Ingrese una oracion: ")
oracion = oracion.split(" ")
listar = []

for palabra in oracion:
        listar.append(palabra[::-1])
oracionr = " ".join(listar)


print(oracionr)