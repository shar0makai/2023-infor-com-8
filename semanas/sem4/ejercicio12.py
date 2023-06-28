def convertir_temperatura(C):
    Faren = (C*9/5) + 32
    return Faren

Celsius= float(input("ingrese una temperatura en C°: "))
temp = convertir_temperatura(Celsius)
print(f" la temperatura en F° es: {temp}")
