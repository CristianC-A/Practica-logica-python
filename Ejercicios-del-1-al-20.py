#Aqui resolvere 20 ejercicios basicos para practicar la logica de programacion.

#Ejercicio 1
# Pedir tu nombre y mostrar un saludo.

# pedirNombre = input("Ingresa tu nombre: ")
# saludoCompleto = f"Hola {pedirNombre}, bienvenido al sistema"
# print(saludoCompleto)

#----------------------------------

#Ejercicio2
#Calculadora de suma: Un sistema contable necesita sumar dos valores ingresados por el usuario.

# primerNumero = int(input("Ingresa el primer numero de la suma: "))
# segundoNumero = int(input("Ingresa el segundo numero de la suma: "))
# suma = primerNumero + segundoNumero
# print(suma)

#----------------------------------

#Ejercicio 3
#Operaciones básicas: Una app educativa muestra todas las operaciones entre dos números.

# pedirOperacion = int(input('''Ingresa la operacion matematica que deseas hace, escribiendo el numero de una de de las siguientes opciones:
# 1: Suma
# 2: Resta
# 3: Multiplicación
# 4: División
# 1,2,3 o 4: '''))

# numero1 = int(input("Ingresa el primer numero: "))
# numero2 = int(input("Ingresa el segundo numero: "))

# resultadoSuma = numero1 + numero2
# resultadoResta = numero1 - numero2
# resultadoMultiplicacion = numero1 * numero2
# resultadoDivision = numero1 / numero2

# if pedirOperacion == 1:
#     print(f"{numero1} + {numero2} = {resultadoSuma}")
# elif pedirOperacion == 2:
#     print(f"{numero1} - {numero2} = {resultadoResta}")
# elif pedirOperacion == 3:
#     print(f"{numero1} * {numero2} = {resultadoMultiplicacion}")
# elif pedirOperacion == 4:
#     print(f"{numero1} / {numero2} = {resultadoDivision}")
# else: "El dato ingresado es incorrecto"

#-------------------------

#Ejercicio 4
#Mayor de edad: Sistema de control de acceso a un sitio para adultos.

pedirEdad = int(input("Ingresa tu edad: "))

if pedirEdad >= 18:
    print(f"Tu edad es {pedirEdad}, Bienvenid@")
elif pedirEdad < 18 & pedirEdad >= 6:
    print(f"Tu edad es {pedirEdad}. Lo siento, no puedes ingresar")
elif pedirEdad > 120:
    print(f"Tu edad es {pedirEdad}. Imposibleee")
elif pedirEdad <= 5 & pedirEdad >= 0:
    print(f'Tu edad es {pedirEdad},aun eres un bebe, no puedes ingresar')


    

