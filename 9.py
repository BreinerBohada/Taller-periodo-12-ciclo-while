#9. Escribe un programa que solicite al usuario un número entero 
# positivo y luego imprima todos los números entre 1 y ese número en orden inverso utilizando un bucle while.

print("programa que imprima todos los números entre 1 y ese número en orden inverso")

n = int(input("Ingrese un numero entero positivo: "))

num = 1

if n <= 1:
    print("El numero ingresado es negativo o es igual a 1")

else:
    while n > num:
        n -= 1
        print (n)
