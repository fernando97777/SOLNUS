# Diseñar un algoritmo que calcule la resta de dos números si el primer número es
# impar. Caso contrario, que calcule la división.

num1 = int(input("Ingrese el Numero 1: "))
num2 = int(input("Ingrese el Numero 2: "))

if num1 % 2 != 0:
    resta = num1 - num2
    print(f"La Resta es: {resta}")
else:
    division = num1 / num2
    print(f"La Division es: {division}")
