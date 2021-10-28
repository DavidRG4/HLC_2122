# Ejercicio 10
tupla = (45, 45, 45, 45)
iguales = True
for i in range(len(tupla)):
    if tupla[i] != tupla[0]:
        iguales = False
print(iguales)
