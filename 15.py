#15. Escribe un programa que solicite al usuario un número entero positivo 
# y luego imprima el promedio de todos los números desde 1 hasta ese número utilizando un bucle while.

print ("Imprima el promedio de todos los números desde 1 hasta ese número")

n = int(input("Introduce un número entero positivo: "))


if n <= 0:
    print("Por favor, introduce un número entero positivo.")
else:
    suma = 0
    i = 1
    
    while i <= n:
        suma += i
        i += 1
    promedio = suma / n
    
    print(f"El promedio de los números desde 1 hasta {n} es: {promedio}")
