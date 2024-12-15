# 6.Escribe un programa que solicite al usuario un 
# número entero positivo y luego imprima la suma de los cuadrados de 
# todos los números desde 1 hasta ese número utilizando un bucle while.

print ("Programa que imprima la suma de los cuadrados de todos los números desde 1 hasta ese número")

n = int(input("Ingrese un numero entero positivo: "))

if n < 0:
    print ("El numero colocado no es positivo.")
else:
    suma = 0
    num = 1

    while num <= n:
        suma += num ** 2
        num += 1
print (f"La suma de los cuadrados desde 1 al numero seleccionado es igual a: {suma}")