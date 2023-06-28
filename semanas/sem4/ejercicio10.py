num = int(input("ingrese un numero: "))

def facto(n):
    if n==1:
        return n
    else:
        return n*facto(n-1)

print(facto(num))