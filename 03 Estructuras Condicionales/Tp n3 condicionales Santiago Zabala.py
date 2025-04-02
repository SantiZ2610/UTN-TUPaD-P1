############ Ejercicio 1

#Edad = float(input("ingrese su edad: "))

#if Edad > 18:
#    print("Es mayor de edad.")

############ Ejercicio 2

#nota= float(input("Ingrese su nota: "))

#if nota >= 6:
#    print("APROBADO")
#else:
#    print("DESAPROBADO")

############ Ejercicio 3

#num_par= int(input("Ingrese un numero par: "))

#if num_par % 2==0:
#    print("Ha ingresado un numero par")
#else:
#    print ("Ingrese un numero par")

############ Ejercicio 4

#Edad= int(input("Ingrese su edad: "))

#if Edad < 12:
#    print("Eres un niño/a.")
#elif Edad >= 12 and Edad<=18:
#    print("Eres un adolescente.")
#elif Edad >= 18 and Edad <=30:
#    print("Eres un adulto/a joven")
#else:
#    print("Eres un adulto/a")

############ Ejercicio 5

#contrasenia = input("Ingrese una contraseña: ")

#if 8 <= len(contrasenia) and len(contrasenia) <= 14:
#    print("Ha ingresado una contraseña correcta")
#else:
#    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

############ Ejercicio 6
#import random
#from statistics import mode, median, mean

#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#moda= mode(numeros_aleatorios)
#mediana= median(numeros_aleatorios)
#media= mean(numeros_aleatorios)

#print(moda,mediana, media)

#if media > mediana > moda:
#    sesgo = "Sesgo positivo (a la derecha)"
#elif media < mediana < moda:
#    sesgo = "Sesgo negativo (a la izquierda)"
#else:
#    sesgo = "Sin sesgo"

#print(f"Lista de números: {numeros_aleatorios}")
#print(f"Moda: {moda}")
#print(f"Mediana: {mediana}")
#print(f"Media: {media}")
#print(f"Resultado: {sesgo}")

############ Ejercicio 7

#texto = input("Ingrese una frase o palabra: ")

#if texto[-1].lower() in "aeiou":
#    texto += "!"
#else:
#    texto = texto  # Se mantiene igual si no termina en vocal

#print(texto)

############ Ejercicio 8

#nombre = input("Ingrese su nombre: ")
#print ("Las opciones son 1 para Mayusculas, 2 para minusculas y 3 para la primera letra en mayusculas")
#opcion = int(input ("Ingrese opcion: "))

#if opcion == 1:
#    print(nombre.upper())
#elif opcion == 2:
#    print(nombre.lower())
#elif opcion == 3:
#    print(nombre.title())
#else:
#    print("ingrese opcion correcta")

############ Ejercicio 9

#magnitud = float(input("Ingrese la magnitud del terromoto: "))

#if magnitud < 3:
#    print ("Muy leve (imperceptible).")
#elif magnitud >= 3 and magnitud < 4:
#    print("Leve (ligeramente perceptible).")
#elif magnitud >= 4 and magnitud < 5:
#    print("Moderado (sentido por personas, pero generalmente no causa daños).")
#elif magnitud >= 5 and magnitud < 6:
#    print("Fuerte (puede causar daños en estructuras débiles).")
#elif magnitud >= 6 and magnitud < 7:
#    print("Muy Fuerte (puede causar daños significativos)")
#elif magnitud >= 7:
#    print("Extremo (puede causar graves daños a gran escala)")

############ Ejercicio 10

#hemisferio = input("¿En qué hemisferio se encuentra (N/S)? ").upper()
#mes = int(input("¿Qué mes del año es (1-12)? "))
#dia = int(input("¿Qué día del mes es (1-31)? "))

#if hemisferio == 'N':
#    if (mes == 12 and dia >= 21) or mes in (1, 2) or (mes == 3 and dia <= 20):
#        print("Invierno")
#    elif (mes == 3 and dia >= 21) or mes in (4, 5) or (mes == 6 and dia <= 20):
#        print("Primavera")
#    elif (mes == 6 and dia >= 21) or mes in (7, 8) or (mes == 9 and dia <= 20):
#        print("Verano")
#    else:
#        print("Otoño")
#elif hemisferio == 'S':
#    if (mes == 12 and dia >= 21) or mes in (1, 2) or (mes == 3 and dia <= 20):
#        print("Verano")
#    elif (mes == 3 and dia >= 21) or mes in (4, 5) or (mes == 6 and dia <= 20):
#        print("Otoño")
#    elif (mes == 6 and dia >= 21) or mes in (7, 8) or (mes == 9 and dia <= 20):
#        print("Invierno")
#    else:
#        print("Primavera")
#else:
#    print("Hemisferio no válido")