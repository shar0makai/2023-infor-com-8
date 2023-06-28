test_str = input("Ingrese una oracion: ")
 
all_freq = {}
 
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

print("cada letra se repite de la siguenete manera:\n "
      + str(all_freq))