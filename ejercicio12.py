fecha=input('Ingrese la fecha ACTUAL en formato DD/MM/AAAA: ')
nacimiento=input('Ingrese la fecha de NACIMIENTO en formato DD/MM/AAAAA: ')

lista1=fecha.split("/")
lista2=nacimiento.split("/")

print(f'La edad aprox. es de: {int(lista1[2])-int(lista2[2])}')