perfecto = int(input("Ingrese un numero: "))

i=1
total=0
while(i<perfecto):
    if perfecto%i==0:
        total=total+i
    i=i+1

if total==perfecto:
    print("Es un numero perfecto")
else:
    print("No es un numero perfecto")