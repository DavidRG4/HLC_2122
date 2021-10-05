# Ejercicio 14

str_list = ["Chema", "Alejandro", "", "Juan Diego", None, "Diana", ""]
str_list = set(str_list)
str_list.remove(None)
str_list.remove("")
print(str_list)
