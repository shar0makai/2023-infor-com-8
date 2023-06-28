oracion = input("Ingrese cualquier oración: ").lower()

p_total = oracion.split()
x = len(p_total)
print("El texto tiene en total " + str(x) + " palabras")