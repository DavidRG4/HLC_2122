# Ejercicio 17

str1 = "Chema39 es profesor10 y maker"
rs = ""
str1 = str1.split(" ")
for x in str1:
    if x.isalpha():
        rs
    else:
        rs += x + " "

print(rs)
