#1. Escribe un programa que solicite al usuario un número entero
# positivo y luego imprima todos los números entre 1 y ese número
# que sean múltiplos de 5 utilizando un bucle while.

print("Imprime todos los números entre 1 y ese número que sean múltiplos de 5")

num=int(input("Ingrese un numero entero positivo: "))

n = 1

while n <= num:
    if n %5 ==0:
        print (n)
        n+=1
    n+=1
