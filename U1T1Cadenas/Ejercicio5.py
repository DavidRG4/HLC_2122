# Ejercicio 5
str1 = "C@#he26ma^&Du5ran"
digitos = 0
Caracteres = 0
Especiales = 0
for x in str1:
    if x.isdigit():
        digitos += 1
    elif x.islower():
        Caracteres += 1
    elif x.isupper():
        Caracteres += 1
    else:
        Especiales += 1

print("Caracteres = ", Caracteres)
print("Digitos = ", digitos)
print("Simbolos = ", Especiales)
