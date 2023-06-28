def eliminar_duplicados(o):
    palabras = o.split()
    sin_dup = list(dict.fromkeys(palabras))
    return sin_dup

oracion = input("ingrese una serie de palabras, separadas por espacio: ")
unir_dup = eliminar_duplicados(oracion)
print(unir_dup)