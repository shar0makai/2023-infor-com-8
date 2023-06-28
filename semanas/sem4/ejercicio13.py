precio = float(input("ingrece el precio: "))
porcentaje_descuento = float(input("ingrece el porcentaje %: "))

def calcular_descuento(a,b):
    descuento = a*b/100
    return descuento
if porcentaje_descuento > 100:
    print("cantidad no valida.")
else:
    print(calcular_descuento(precio,porcentaje_descuento))