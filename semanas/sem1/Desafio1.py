nombre = input("ingrese el nombre del vendedor: ")
ganancia = float(input("ingrese el monto vendido: "))

print (f'Nombre: {nombre} \nMonto Vendido:{ganancia}\nComision ganada:{round(ganancia*0.06,2)}')