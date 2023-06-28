palabra = input("Introduce una palabra: ")

def es_palindromo(pal):
    if str(pal) == str(pal)[::-1]:
        return"es un palindromo"
    else:
        return"no es palindromo"

print(es_palindromo(palabra))