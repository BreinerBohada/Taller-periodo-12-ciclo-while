#8. Escribe un programa que solicite al usuario un número entero 
# positivo y luego imprima los primeros n números impares utilizando un bucle while.

print ("Programa que imprima los primeros n numeros impares.")

n = int(input("Ingrese un numero entero positivo: "))

if n <= 0 or n % 2 == 0:
    print ("El numero ingresado no es postivo o es par.")
    
else:
    num = 1
    while num <= n:
        print (num)
        num += 2
