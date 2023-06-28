def contar_palabras(o):
    p_total = o.split()
    cantidad_p = len(p_total)
    return cantidad_p

oracion = input("ingrese una oracion: ")
cantidad = contar_palabras(oracion)
print(f" la cantidad de palabras en esta oracion es de: {cantidad}")