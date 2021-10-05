# Ejercicio 7

s1 = "hD"
s1_1 = "hDf"
s2 = "ChemaDuran"
count = 0
tf = False
for x in s1:
    for y in s2:
        if y == x:
            count += 1
if count == len(s1):
    tf = True
print(tf)

tf = False
for x in s1_1:
    for y in s2:
        if y == x:
            count += 1
if count == len(s1_1):
    tf = True
print(tf)
