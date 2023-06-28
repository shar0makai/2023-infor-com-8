letra = input("Introduce un caracter: ")
 
if letra >= 'a' and letra <= 'z':
    print("el caracter es una minuscula")
elif letra.isdigit():
    print("el caracter es un numero")
else:
    if letra >= 'A' and letra <= 'Z':
        print("el caracter es mayuscula")