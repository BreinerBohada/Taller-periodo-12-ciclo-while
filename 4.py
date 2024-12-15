#4. Escribe un programa que solicite al usuario un número entero 
# positivo y luego imprima si el número es un número de Armstrong utilizando un bucle while.

print ("Calcular si un numero es un numero de armstrong.") 

def es_numero_armstrong (num):
    digitos = str(num)
    cantidad_digitos = len(digitos)
    
    suma = 0
    temp = num
    
    while temp > 0:
        digito = temp % 10 
        suma += digito ** cantidad_digitos
        temp //= 10
        
    return suma == num

numero = int(input("Ingresa un numero entero positivo: "))

if es_numero_armstrong (numero):
    print (f"{numero} es un numero de armstrong.")
    

print (f"{numero} no es un numero de armstrong.")
    