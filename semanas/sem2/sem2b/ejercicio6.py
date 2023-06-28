list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list.copy():
    divid = i %2
    if divid == 0:
        list.remove(i)

print(list)
