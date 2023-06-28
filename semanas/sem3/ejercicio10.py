def vocalmayus(frase):
    frasefinal = ""
    for vocal in frase:
        if vocal in ('a', 'e', 'i', 'o', 'u'):
            vocal = vocal.upper()
            frasefinal += vocal
        else: 
            frasefinal += vocal
    return frasefinal 

frase = input("Frase: ")

print(vocalmayus(frase))