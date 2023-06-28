numeros = input("Introduce números, separados por comas: ")
numeros = numeros.split(',')
n = len(numeros)
for i in range(n):
    numeros[i] = int(numeros[i])
numeros = tuple(numeros)
sum = 0
for i in numeros:
    sum += i
media = sum/n
print('La media de esos números es', media)
