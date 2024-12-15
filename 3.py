#3. Escribe un programa que solicite al usuario un número entero positivo 
# y luego calcule la suma de todos los números divisibles por 3 desde 1 
# hasta ese número utilizando un bucle while.

print ("Calcule la suma de todos los números divisibles por 3 desde 1 hasta ese número")

n = int(input("Ingrese un numero limite: "))

num = 1

suma = 0

while num <= n:
    if num % 3 == 0:
        print (num)
        suma = suma + num
        num += 1
    num += 1

print (f"La suma de los numeros divisibles por 3 es: {suma}")