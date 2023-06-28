oracion = input("Ingrese cualquier oración: ").lower()
letra1 = input("Ingrese una letra: ").lower()
letra2 =  input("Ingrese una segunda letra: ").lower()
letra3 = input("Ingrese una tercer letra: ").lower()

#Ejercicio 1, identificar cuantas veces una letra aparece en la oracion escrita.
contador = 0
contador2 = 0
contador3 = 0
for l1 in oracion:
    if l1 == letra1:
        contador += 1
for l2 in oracion:
    if l2 == letra2:
        contador2 += 1
for l3 in oracion:
    if l3 == letra3:
        contador3 += 1

print("La letra '" + letra1 + "' se repite " + str(contador) + " vez/veces")
print("La letra '" + letra2 + "' se repite " + str(contador2) + " vez/veces")
print("La letra '" + letra3 + "' se repite " + str(contador3) + " vez/veces")

#Ejercicio 2, contar la cantidad de letras que tiene en total la oracion:
p_total = oracion.split()
x = len(p_total)
print("El texto tiene en total " + str(x) + " palabras")

#Ejercicio 3, identificar cual es la primera y ultima letra:
oracion_lista = list(oracion)
pri_letra = oracion_lista[0]
ult_letra = oracion_lista[-1]
print("La primera letra es: " + str(pri_letra) + " y la letra es: " + str(ult_letra))

#Ejercicio 4, invertir la oracion:
o_espejo = oracion[::-1]
print("La oración en el orden inverso es: " + str(o_espejo))

#Ejercicio 5, afirmar si la palabra "python" se encuentra en la oracion: 
if "python" in oracion:
    print("La palabra 'Python' se encuentra en la oración.")
else:
    print("La palabra 'Python' no se encuentra en la oración.")