###### Ejercicio 1

#for i in range (1,101):
#    print(i)

###### Ejercicio 2 

#numero = int(input("Ingresa un número entero: "))
#numero_abs = abs(numero)

#contador = 0

#for _ in str(numero_abs):
#    contador += 1

#print("El número tiene", contador, "dígitos.")

###### Ejercicio 3

#num1 = int(input("Ingrese primer numero entero: "))
#num2 = int(input("Ingrese segundo numero entero: "))

#suma = 0 

#for i in range (num1 +1,num2):
#    suma += i

#print("La suma de los numeros entre", num1, "y", num2, "es: ",suma)

###### Ejercicio 4 

#total = 0
#numero = int(input("Ingresa un número entero (0 para terminar): "))


#while numero != 0:
#    total += numero
#    numero = int(input("Ingresa un número entero (0 para terminar): "))

#print("La suma total es:", total)

###### Ejercicio 5

#import random

#numero_secreto = random.randint(0, 9)
#intentos = 0
#adivinado = False

#print("¡Adivina el número del 0 al 9!")

#while not adivinado:
#    intento = int(input("Tu intento: "))
#    intentos += 1
#
#    if intento == numero_secreto:
#        adivinado = True
#        print("¡Correcto! Adivinaste el número en", intentos, "intentos.")
#    else:
#        print("No es ese. Intenta de nuevo.")

###### Ejercicio 6

#for i in range(100, -1, -2):
#    print(i)

###### Ejercicio 7

#limite = int(input("Ingresa un número entero positivo: "))


#suma = 0

#for i in range(limite + 1):
#    suma += i


#print("La suma de los números de 0 hasta", limite, "es:", suma)

###### Ejercicio 8

#cantidad_numeros = 100

#pares = 0
#impares = 0
#positivos = 0
#negativos = 0

#print(f"Ingrese {cantidad_numeros} números enteros:")

#for _ in range(cantidad_numeros):
#    numero = int(input("Número: "))

#    # Par o impar
#    if numero % 2 == 0:
#        pares += 1
#    else:
#        impares += 1

#    # Positivo o negativo
#    if numero > 0:
#        positivos += 1
#    elif numero < 0:
#        negativos += 1


#print("--- Resultados ---")
#print("Pares:", pares)
#print("Impares:", impares)
#print("Positivos:", positivos)
#print("Negativos:", negativos)

###### Ejercicio 9 


#cantidad_numeros = 10

#suma = 0

#print(f"Ingrese {cantidad_numeros} números enteros:")

#for _ in range(cantidad_numeros):
#    numero = int(input("Número: "))
#    suma += numero

#media = suma / cantidad_numeros

#print("La media de los", cantidad_numeros, "números es:", media)

###### Ejercicio 10 

#numero = int(input("Ingresa un número entero: "))
#invertido = 0
#negativo = numero < 0
#numero = abs(numero)


#while numero > 0:
#    digito = numero % 10
#    invertido = invertido * 10 + digito
#    numero = numero // 10


#if negativo:
#    invertido = -invertido

#print("Número invertido:", invertido) 
