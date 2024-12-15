#5. Escribe un programa que solicite al usuario un número entero 
# positivo y luego imprima todos los números primos menores o iguales 
# a ese número utilizando un bucle while.

print ("Programa que imprima todos los números primos menores o iguales al número ingresado")

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input("Ingresa un número entero positivo: "))

n = 2
while n <= numero:
    if es_primo(n):
        print(n, end=" ")
    n += 1 
