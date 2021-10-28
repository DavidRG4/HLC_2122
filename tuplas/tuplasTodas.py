# Ejercicio 1
tupla = (10, 20, 30, 40, 50)
print(tupla[::-1])
# Ejercicio 2
tupla = ("Orange", [10, 20, 30], (5, 15, 25))
print(tupla[1][1])
# Ejercicio 3
tupla = (50,)
print(tupla)
# Ejercicio 4
tupla = (10, 20, 30, 40)
a, b, c, d = tupla
print(a)
print(b)
print(c)
print(d)
# Ejercicio 5
tupla1 = (11, 22)
tupla2 = (99, 88)
print(tupla1)
print(tupla2)
tupla1, tupla2 = tupla2, tupla1
print(tupla1)
print(tupla2)
# Ejercicio 6
tupla = (11, 22, 33, 44, 55, 66)
tupla2 = (
    tupla[3],
    tupla[4],
)
print(tupla2)
# Ejercicio 7
tupla = (11, [22, 33], 44, 55)
tupla[1][tupla[1].index(22)] = 222
print(tupla)
# Ejercicio 8
tupla = (("a", 23), ("b", 37), ("c", 11), ("d", 29))
print(tupla)
a, b, c, d = tupla
tupla = c, a, d, b
print(tupla)
# Ejercicio 9
tupla = (50, 10, 60, 70, 50)
veces = 0
for x in tupla:
    if x == 50:
        veces += 1
print(veces)
# Ejercicio 10
tupla = (45, 45, 45, 45)
iguales = True
for i in range(len(tupla)):
    if tupla[i] != tupla[0]:
        iguales = False
print(iguales)
