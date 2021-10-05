# Ejercicio 15

str1 = "/*Chema es @profesor & maker"
str2 = ""
rs = []
str1 = str1.replace("&", "y")
for x in str1:
    rs.append(x)
rs.remove("/")
rs.remove("*")
rs.remove("@")

for x in rs:
    str2 += x
print(str2)
