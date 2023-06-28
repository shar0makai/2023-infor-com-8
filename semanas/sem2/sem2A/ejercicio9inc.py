n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))
if (n1 > n2 and n1 > n3):
    print(str(n1) + " es el mayor")
elif (n2 > n1 and n2 > n3):
    print(str(n2) + " es el mayor")
elif (n2 == n1 and n2 == n3):
    print("ningun numero es mayor")
else:
    print(str(n3) + " es el mayor")