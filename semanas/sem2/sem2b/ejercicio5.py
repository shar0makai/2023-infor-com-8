conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
menor=None
mayor=None

for numero in conjunto:
    if menor==None and mayor==None:
        menor=numero
        mayor=numero
    else:
        if numero<menor:
            menor=numero
        if numero>mayor:
            mayor=numero
print(f"el numero mayor es {mayor}")