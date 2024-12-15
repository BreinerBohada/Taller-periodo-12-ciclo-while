#11. Escribe un programa que solicite al usuario un número entero positivo y 
# luego calcule la cantidad de dígitos del número utilizando un bucle while.

print ("Calcule la cantidad de dígitos del número.")

n = int(input("Ingrese un numero entero positivo: "))

if n <=0:
    print("Por favor ingrese un numero positivo.")
    
else:
    count = 0
    while n > 0:
        
        n //= 10
        count += 1
    print (f"El numero tiene {count} digitos.")