# 2. Escribe un programa que solicite al usuario dos 
# números enteros positivos y luego imprima todos los números entre ellos 
# (inclusive) utilizando un bucle while.

print("Programa que solicite al usuario dos números enteros positivos y luego imprima todos los números entre ellos (inclusive) utilizando un bucle while.")

n1 = int(input("Ingrese un primer numero: "))

n2 = int(input("Ingrese un segundo numero (Debe ser mayor al anterior): "))

if n1>n2:
    print ("Error: El segundo numero es menor al primer numero.")
else:
    while n1 <= n2:
        print (n1)
        n1 +=1