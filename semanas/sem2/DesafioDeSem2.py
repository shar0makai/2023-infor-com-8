oracion = input("Ingrese cualquier oracion: ")
letra1 = input("Ingrese 3 letras, sin espacio entre ellas: ")

#Ejercicio 1, cambiar las mayusculas por minuscula e identificar cuantas veces se repite una letra en la oracion escrita.
oracion = oracion.lower()
letra1 = letra1.lower()

contador_l1 = oracion.count(letra1[0])
contador_l2 = oracion.count(letra1[1])
contador_l3 = oracion.count(letra1[2])

print(f"La letra '{letra1[0]}' se repite {contador_l1} veces, '{letra1[1]}' se repite {contador_l2} veces y '{letra1[2]}' se repite {contador_l3} veces")

#Ejercicio 2, contar la cantidad de letras que tiene en total en la oracion:
p_total = oracion.split()
cantidad_p = len(p_total)
print("El texto tiene " + str(cantidad_p) + " palabras")

#Ejercicio 3, identificar cual es la primera y ultima letra:
oracion_lista = list(oracion)
pri_letra = oracion_lista[0]
ult_letra = oracion_lista[-1]
print("La primera letra es: " + str(pri_letra) + " y la ultima es: " + str(ult_letra))

#Ejercicio 4, invertir la oracion:
o_espejo = oracion[::-1]
print("La oracion en el orden inverso es: " + str(o_espejo))

#Ejercicio 5, afirmar si la palabra "python" se encuentra en la oracion: 
if "python" in oracion:
    print("'Python' se encuentra en la oracion.")
else:
    print("'Python' no se encuentra en la oracion.")