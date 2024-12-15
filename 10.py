#10. Escribe un programa que solicite al usuario dos números enteros 
#positivos y luego imprima la suma de todos los números entre ellos (inclusive) utilizando un bucle while.

print ("Programa que imprima la suma de todos los números entre ellos (inclusive).")

n = int(input("Ingrese un primer numero: "))

num = int(input("Ahora un segundo numero (debe ser mayor al numero anterior): "))

suma = 0

if n > num or n <= 0 or num <= 0:
    print ("El numero ingresado es menor que el primero o es negativo")
else:
    while n <= num:
        suma += n
        n += 1
    print("La suma de todos los numeros entre los numeros ingresados es: ", suma)