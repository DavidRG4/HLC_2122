# Ejercicio 1
# Caso1
"""
st1 = "ChemTioaDur"
rs = st1[4:7]
print(rs)
# Caso2
st2 = "ChQueem"
print(st2[2:5])
"""
# Ejercicio 2
"""
st1 = "Hola"
st2 = "Adios"

rs = st1[:2] + st2 + st1[2:]
print(rs)
"""

# Ejercicio 3
"""
s1 = "Chema"
s1l = []
for x in s1:
    s1l.append(x)
s2 = "Duran"
s2l = []
for x in s2:
    s2l.append(x)

rs = s1l[0] + s2l[0] + s1l[2] + s2l[2] + s1l[4] + s2l[4]

print(rs)
"""

# Ejercicio 4
"""
str1 = "ChEmaDUraN"
rs1 = ""
rs2 = ""
for x in str1:
    if x == x.lower():
        rs1 += x
    else:
        rs2 += x

rs3 = rs1 + rs2
print(rs3)
"""

# Ejercicio 5
"""
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
"""
# Ejercicio 6
s1 = "Abc"
s2 = "Xyz"
rs1 = []
rs2 = []
rs3 = ""
for x in s1:
    rs1.append(x)
for x in s2:
    rs2.append(x)
rs3 = rs1[0] + rs2[2] + rs1[1] + rs2[1] + rs1[2] + rs2[0]
print(rs3)
