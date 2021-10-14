lista1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
lista2 = ["h", "i", "j"]
for i in range(len(lista2)):
    lista1[2][1][2].append(lista2[i])

print(lista1)
