
def promedio(n):
    n = 0
    c= 0
    suma = 0
    while n >= 0:
        n=int(input("ingrese: "))
        if n > 0:
            c = c+1
            suma = suma +n
            return suma

print(promedio())