def es_capicua(numero):
        return numero == numero[::-1]

num = input("ingrese un numero: ")

print(es_capicua(num))