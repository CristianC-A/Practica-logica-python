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

# pedirEdad = int(input("Ingresa tu edad: "))

# if pedirEdad >= 18:
#     print(f"Tu edad es {pedirEdad}, Bienvenid@")
# elif pedirEdad < 18 & pedirEdad >= 6:
#     print(f"Tu edad es {pedirEdad}. Lo siento, no puedes ingresar")
# elif pedirEdad > 120:
#     print(f"Tu edad es {pedirEdad}. Imposibleee")
# elif pedirEdad <= 5 & pedirEdad >= 0:
#     print(f'Tu edad es {pedirEdad},aun eres un bebe, no puedes ingresar')

#----------------------------------

#Ejercicio 5
#Conversor Celsius → Fahrenheit
# la formula para pasar de celcius a fahrenheit es: °F = (°C × 9/5) + 32;

# print("Conversor de temperatura en medidad de celsius a fahrenheit")

# temperaturaEnCelcius = int(input("Ingresa la temperatura que quieres convertir a Fahrenheit: "))
# temperaturaEnFahrenheit = (temperaturaEnCelcius * 9/5) + 32

# print(f"La temperatura {temperaturaEnCelcius} en grados celcius es igual a {temperaturaEnFahrenheit} en grados Fahrenheit")

#----------------------------------

#Ejercicio 6
#Área de un rectángulo

# print("Calculadora de area de un rectangulo")
# baseRectangulo = int(input("Ingresa la base del rectangulo: "))
# alturaRectangulo = int(input("Ingresa la altura del rectangulo: "))
# areaRectangulo = (baseRectangulo * alturaRectangulo)
# print(f"El area del rectangulo es: {areaRectangulo}")

#----------------------------------

#Ejercicio 7
#Perímetro de un cuadrado

# print("Calculadora de perimetro de un cuadrado")
# ladoCuadrado = int(input("Ingresa el valor del lado del cuadrado: "))
# perimetroCuadrado = ladoCuadrado * 4
# print(f"El perimetro del cuadrado es: {perimetroCuadrado}")

#----------------------------------

#Ejercicio 8
#Doble de un número

# print("Calculadora de puntos dobles")
# numeroDePuntos = int(input("Ingresa la cantidad de puntos a calcular: "))
# puntosDobles = numeroDePuntos * 2
# print(f"La cantidad de puntos dobles es de : {puntosDobles}")

#----------------------------------

#Ejercicio 9
#Mitad de un número

# print("Calculadora de la mitad de un numero")
# numeroACalcular = float(input("Ingresa el numero para calcular su mitad: "))
# mitadCalculada = float(numeroACalcular / 2)
# print(f"La mitad de {numeroACalcular} es: {mitadCalculada}")

#----------------------------------
#Ejercicio 10
#Calcular IVA (19%)

# print("Calcular IVA")
# valorProducto = float(input("Ingresa el valor del producto: "))
# valorIVA = float(valorProducto * 0.19)
# valorProductoConIVA = int(valorProducto + valorIVA)
# print(f"El valor total a pagar con IVA es: {valorProductoConIVA}")

#----------------------------------

#Ejercicio 11
#Calcular el area de un triangulo

# print("Calculadora de area de un triangulo")
# base = int(input("Ingresa la base del triangulo: "))
# altura = int(input("Ingresa la altura del triangulo: "))
# areaTriangulo = (base * altura) / 2
# print(f"El area del triangulo es igual a: {areaTriangulo}")

#-----------------------------------

#Ejercicio 12
#Kilómetros a metros

# print("Calculadora de kilometros a metros")
# kilometros = float(input("Ingresa la cantidad de kilometros a convetir a metros: "))
# metros = kilometros * 1000
# print(f"{kilometros} kilometros equivalen a: {metros} metros")

#------------------------------------

# Ejercicio 13
#Horas a segundos

# print("Calculadora de horas a segundos")
# horas = float(input("Ingresa la cantidad de horas que quieres convertir a segundos: "))
# horasASegundos = (horas * 60) * 60
# print(f"{horas} horas equivalen a: {horasASegundos} segundos.")

#-----------------------------------

#Ejercicio 14
#Promedio de 3 notas

# print("Calcular el promedio de 3 notas")
# nota1 = float(input("Ingresa la primer nota: "))
# nota2 = float(input("Ingresa la segunda nota: "))
# nota3 = float(input("Ingresa la tercer nota: "))
# notaPromedio = (nota1 + nota2 + nota3) / 3
# print(f"El promedio de las notas ingresadas es de: {notaPromedio}")

#---------------------------

#Ejercicio 15
# Salario anual

# print("Calcular un salario anual con un sueldo mensual fijo")
# salarioMensual = float(input("Ingrese el salario mensual: "))
# salarioAnual = salarioMensual * 12
# print(f"El salario anual es de: {salarioAnual}")

#-----------------------------

#Ejercicio 16
# Área del círculo

# print("Calcular el area de un circulo pidiendo el radio")
# radio = float(input("Ingresa el radio del circulo: "))
# areaCirculo = 3.1416 * (radio ** 2)
# print(f"El area del circulo es de: {areaCirculo}")

#-----------------------------

#Ejercicio 17
#Cuadrado de un número

# print("Calcular el resultado de un numero al cuadrado")
# numero = float(input("Ingresa un numero para calcular su resultado al cuadrado: "))
# numeroAlCuadrado = numero ** 2
# print(f"El resultado de {numero} al cuadrado es de: {numeroAlCuadrado}")

#------------------------------

#Ejercicio 18
# Mayor de dos números

# print("Comparar 2 numeros para mostrar el mayor de los 2")
# numero1 = float(input("Ingresa el primer numero: "))
# numero2 = float(input("Ingresa el segundo numero: "))
# if numero1 > numero2:
#     print(f"{numero1} es mayor que {numero2}")
# elif numero2 > numero1:
#     print(f"{numero2} es mayor que {numero1}")
# else:
#     print("Los numeros son iguales")

#-----------------------------------

#Ejercicio 19
#Positivo o negativo

# print("Observar si el numero es negativo o positivo")
# numero = int(input("Ingresa un  numero: "))
# if numero > 0:
#     print(f"{numero} es positivo")
# elif numero == 0:
#     print("El numero ingresado es 0. El 0 no cuenta como negativo ni como positivo")
# else:
#     print(f"{numero} es negativo")

#---------------------------------

#Ejercicio 20
# Frase con datos

print("Frase con datos como nombre y edad")
nombre = input("ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
print(f"Hola mundo, soy {nombre} y tengo {edad} años")

