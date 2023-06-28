def encontrar_maximo(valores):
    mayor = valores[0]

    for i in range(1, len(valores)):
        if valores[i] > mayor:
            mayor = valores[i]
    
    return mayor

lista=[]
valor=int(input("Ingrese valor (0 para finalizar): "))
while valor != 0:
    lista.append(valor)
    valor=int(input("Ingresar valor (0 para finalizar): "))

print(encontrar_maximo(lista))