# Ejercicio 18

str1 = "/*Chema es @profesor & maker!!"
str1 = (
    str1.replace("/", "#")
    .replace("*", "#")
    .replace("@", "#")
    .replace("&", "#")
    .replace("!", "#")
)
print(str1)
