def imprimir_pares(m):
  n=0
  lista=[]
  while n<=m:
    lista.append(n*2)
    n+=1
  return lista

num1 = int(input("ingrese un numero: "))
print(imprimir_pares(num1))