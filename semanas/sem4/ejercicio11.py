def contar_vocales(ora):
	v = 0
	for letra in ora:
		if letra.lower() in "aeiou":
			v += 1
	return v

oracion = input("ingrese una oracion: ")
cantidad = contar_vocales(oracion)
print(f" hay {cantidad} vocales")