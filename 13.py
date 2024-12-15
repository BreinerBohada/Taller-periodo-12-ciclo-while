#13. Escribe un programa que solicite al usuario dos números enteros positivos y 
# luego imprima la tabla de multiplicar del primer número hasta el segundo número utilizando un bucle while.

print ("Imprima la tabla de multiplicar del primer número hasta el segundo número")

n1 = int(input("Introduce el primer número entero positivo: "))
n2 = int(input("Introduce el segundo número entero positivo: "))

if n1 <= 0 or n2 <= 0:
    print("Por favor, introduce números enteros positivos.")
else:
    if n1 > n2:
        print("El primer número debe ser menor o igual que el segundo número.")
    else:
        for num in range(n1, n2 + 1):
            print(f"\nTabla de multiplicar del {num}:")
            i = 1
            while i <= 10:
                print(f"{num} x {i} = {num * i}")
                i += 1
