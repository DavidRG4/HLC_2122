# Ejercicio 4
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
