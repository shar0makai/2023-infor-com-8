altura = int(input("Introduce la altura del triángulo (entero positivo): "))
for anchura in range(altura):
    print((str(altura + anchura)) * (anchura + 1))