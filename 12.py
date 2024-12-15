#12. Escribe un programa que solicite al usuario un número entero positivo y 
# luego imprima todos los números entre 1 y ese número que sean múltiplos de 7 utilizando un bucle while.

print("Programa que imprima todos los números entre 1 y ese número que sean múltiplos de 7")

n = int(input("Ingrese un numero entero positivo: "))

if n <= 0:
    
    print("El numero ingresado es negativo o es igual a 0")
    
else:
    
    num = 1
    
    print(f"Los multiplos de 7 entre 1 y {n} son: ")
    
    while num < n:
        if num % 7 == 0:
            print (num)
            num += 1
        num += 1