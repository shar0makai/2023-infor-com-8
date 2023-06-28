def es_par(a):
    if a % 2 == 0:
        return "el numero es par"
    else:
        return "el numero NO es par"

num1 = int(input("ingrese un numero: "))

par = es_par(num1)

print(par)