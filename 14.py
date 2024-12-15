#14. Escribe un programa que solicite al usuario un número entero positivo 
# y luego imprima la suma de los números de Fibonacci hasta ese número utilizando un bucle while.

print("Imprima la suma de los números de Fibonacci hasta ese número")

numero = int(input("Introduce un número entero positivo: "))

if numero <= 0:
    print("Por favor, introduce un número entero positivo.")
else:
    a, b = 0, 1
    suma_fibonacci = 0

    while a <= numero:
        suma_fibonacci += a
        a, b = b, a + b 
    
    print(f"La suma de los números de Fibonacci hasta {numero} es: {suma_fibonacci}")
