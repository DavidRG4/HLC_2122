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
