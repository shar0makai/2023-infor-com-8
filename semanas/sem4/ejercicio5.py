def es_divisible(a,b):
    if a % b == 0:
        return "el primer numero es divisible por el segundo"
    else:
        return "el primer numero NO es divisible por el segundo"

num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese otro numero: "))

division = es_divisible(num1,num2)

print(division)