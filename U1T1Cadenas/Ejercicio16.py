# Ejercicio 16

str1 = "Tengo 39 años y 10 meses"
str1 = str1.split(" ")
rs = ""
for x in str1:
    if x.isdigit():
        rs += x

print(rs)
