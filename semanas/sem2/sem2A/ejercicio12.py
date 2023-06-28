numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    print ("El resultado es: " + str(numero1 + numero2))
else:
    print ("uno o ambos numeros son impares")
