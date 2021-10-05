# Ejercicio 9

str1 = "Galicia = 78 Andalucia = 83 Canarias = 68 Cataluña = 65"
rs1 = str1.split(" ")
suma = 0
med = 0
for x in rs1:
    if x.isdigit():
        med += 1
        suma += int(x)
med = suma / med
print("La suma total es ", suma)
print("El promedio es ", med)
