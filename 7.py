#7. Escribe un programa que solicite al usuario un número 
# entero positivo y luego imprima la suma de los primeros n números pares utilizando un bucle while.

print ("Programa que imprima la suma de los primeros n números pares")

n = int(input("Ingrese un numero entero positivo: "))

if n <= 0 or n % 2 != 0:
    print ("El numero ingresado no es positivo o es impar.")
    
else:
    num = 2
    suma = 0
    while num <= n:
        suma += num
        num += 2
    print (f"La suma de los primeros numeros positivos es: {suma}")