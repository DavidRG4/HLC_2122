lista1 = [5, 10, 15, 20, 25, 50, 20]
for i in range(len(lista1)):
    if lista1[i] == 20:
        lista1[i] = 200
        break
print(lista1)
