# Ejercicio 1
"""
n1 = int(input("Dame el primer numero: "))
n2 = int(input("Dame el segundo numero: "))

n3 = n1 * n2

print("la multiplicacion de estos dos es: ", n3)

"""
# Ejercicio 2
"""
totalMoney = 1000
quantity = 3
price = 450

print(
    "Tengo {} ".format(totalMoney),
    "euros para comprar {} tarjetas gráficas".format(quantity),
    "por {:d} dólares".format(price),
)
"""
# Ejercicio3
"""
p1 = "Nombre"
p2 = "Es"
p3 = "Ignatius"

print(p1, "**", p2, "**", p3)
"""
# Ejercicio4
"""
num = 8
print("El número octal del número decimal 8 es:", oct(8))
print("El número octal del número decimal 8 es {:o}".format(8))
"""

# Ejercicio 5
"""
num = 458.541315
print("{:.2f}".format(num))
"""

# Ejercicio 6
"""
print("Dime 5 numeros seguidos")
lis = [input(), input(), input(), input(), input()]
print(lis)
"""
# Ejercico 7
"""
print("Dime tres nombres seguidos en linea")
nombres = input()
n1 = nombres.split(" ")
print(n1[0])
print(n1[1])
print(n1[2])
"""
# Ejercicio 8
"""
print("Dime un numero")
n1 = int(input())
print("Dime un numero")
n2 = int(input())

nx = n1 * n2
ns = n1 + n2

if nx < 1000:
    print("La suma de estos es: ", ns)
elif nx >= 1000:
    print("La multiplicacion de estos es: ", nx)
"""
