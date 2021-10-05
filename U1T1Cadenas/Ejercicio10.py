# Ejercicio 10

str1 = "Apple"
count = 0
rs = ""
for x in str1:
    rs += x + "=" + str(str1.count(x)) + " "
print(rs)
