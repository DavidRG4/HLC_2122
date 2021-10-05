# Ejercicio 8

str1 = "Lo que yo te diga. Que la vida es así"
rs1 = str1.lower().split(" ")
count = 0
for x in rs1:
    if x == "que":
        count += 1

print("El recuentos de 'que' es ", count)
