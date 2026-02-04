#Ejercicios del 21 al 40
#Cristian Álvarez

#Ejercicio 21
#Número par o impar: Un sistema financiero necesita saber si un número de transacción es par o impar para aplicar reglas internas.

# print("Saber si un numero es par o impar")
# numero = int(input("Ingresa un numero par saber si es par o impar: "))
# if numero % 2 == 0:
#     print(f"El numero {numero} es par")
# else: 
#     print(f"El numero {numero} es impar")
    
#-------------------------------------

#Ejercicio 22
#Puede votar: Sistema de elecciones.

# print("Saber si una persona tiene la edad minima para votar")
# edad = int(input("Ingresa tu edad para saber si puedes votar: "))
# if edad > 17:
#     print(f"Tu edad es: {edad}, eres mayor de edad y puedes votar")
# else:
#     print(f"Tu edad es: {edad}, no cumples con la edad para votar")

#-----------------------------------

#Ejercicio 23
# Descuento por compra: Tienda virtual.
# Requisitos
# Pedir valor de compra.
# Si es mayor a 100, aplicar 10% de descuento.
# Mostrar total.

# print("Saber si aplica descuento para un producto")
# valorProducto = float(input("Ingresa el valor del producto: "))
# if valorProducto > 99:
#     valorConDescuento = valorProducto - valorProducto * 0.10
#     print(f'''Aplica descuento
#           Total a pagar: {valorConDescuento}''')
# else:
#     print(f'''No aplica descuento
#           Total a pagar: {valorProducto}''')

#---------------------------------------

#Ejercicio 24
# Clasificación de notas: Sistema académico.
# Requisitos
# Pedir nota (0–100).
# Clasificar:
# A: 90–100
# B: 80–89
# C: 70–79
# D: 60–69
# F: < 60

# print("Clasificación de notas")
# nota = int(input("Ingresa una nota entre 0 y 100: "))
# if nota < 101 and nota > 89:
#     print(f"La nota es: A")
# elif nota < 90 and nota > 79:
#     print("La nota es: B")
# elif nota < 80 and nota > 69:
#     print("La nota es: C")
# elif nota < 70 and nota > 59:
#     print("La nota es: D")
# elif nota < 60:
#     print("La nota es: F")
# else:
#     print("La nota ingresada es invalida")

#--------------------------------------

# Ejercicio 25
#Año bisiesto: Calendario
# Requisitos
# Un año es bisiesto si:
# divisible entre 4
# no divisible entre 100
# o divisible entre 400

# print("Saber si un año es bosiesto")
# anio = int(input("Ingresa el año para verificar si es bisiesto: "))
# if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
#     print(f"{anio} es bisiesto")
# else:
#     print(f"{anio} no es bisiesto")

#-------------------------------------

#Ejercicio 26
# Contraseña correcta: Sistema login.
# Requisitos
# Pedir contraseña.
# Compararla con una guardada.
# Mostrar acceso permitido o denegado.

# print("Acceder si una contraseña es correcta")
# contrasenaGuardada = "GbcvD13579"
# contrasenaIngresada = input("Ingresa la contraseña: ")

# if contrasenaIngresada == contrasenaGuardada:
#     print("Acceso permitido, bienvenido")
# else:
#     print("Acceso denegado, ingresa la contraseña correcta")

#-----------------------------------

#Ejercicio 27
# # Mayor de tres números: Sistema de análisis.
# Requisitos
# Pedir tres números.
# Mostrar el mayor.

# print("Comparar 3 numeros y mostrar el mayor")
# numero1 = int(input("Ingresa el primer numero: "))
# numero2 = int(input("Ingresa el segundo numero: "))
# numero3 = int(input("Ingresa el tercer numero: "))

# if numero1 > numero2 and numero1 > numero3:
#     print(f"{numero1} es el mayor")
# elif numero2 > numero1 and numero2 > numero3:
#     print(f"{numero2} es el mayor")
# else:
#     print(f"{numero3} es el mayor")

#--------------------------------------

#Ejercicio 28
# Clasificar edad: Sistema médico.
# Requisitos
# Edad:
# 0–12 niño
# 13–17 adolescente
# 18–64 adulto
# 65+ adulto mayor

# print("Clasificar la edad")
# edadIngresada = int(input("Ingresa la edad: "))
# if edadIngresada >= 0 and edadIngresada <= 12:
#     print(f"{edadIngresada} esta en el rango de edad de niño")
# elif edadIngresada > 12 and edadIngresada <= 17:
#     print(f"{edadIngresada} esta en el rango de edad de adolescente")
# elif edadIngresada >= 18 and edadIngresada <= 64:
#     print(f"{edadIngresada} esta en el rango de edad de adulto")
# else:
#     print(f"{edadIngresada} esta en el rango de edad de adulto mayor")

#--------------------------------

#Ejercicio 29
# Múltiplo de 5: Sistema matemático.
# Requisitos
# Pedir número.
# Ver si es múltiplo de 5.

# print("Saber si un numero es multiplo de 5")
# numero = int(input("Ingresa un numero para verificar si es multiplo de 5: "))
# if numero % 5 == 0:
#     print(f"{numero} es multiplo de 5")
# else:
#     print(f"{numero} no es multiplo de 5")

#-------------------------------------

#Ejercicio 30
# Validar rango: Formulario web.
# Requisitos
# Pedir número.
# Validar si está entre 1 y 100.

# print("Verificar si el numero ingresado esta en el rango permitido")
# numero = int(input("Ingresa un numero entre 1 y 100: "))
# if numero >= 1 and numero <= 100:
#     print(f"{numero} esta dentro del rango sugerido")
# else:
#     print(f"{numero} no esta dentro del rango sugerido")

#--------------------------------------

#Ejercicio 31
# Semáforo: Sistema de tráfico.
# Requisitos
# Pedir color.
# Mostrar acción:
# rojo → detener
# amarillo → precaución
# verde → avanzar

# print("Semaforo")
# colorIngresado = input('''Ingresa un color para sugerirte la accion a seguir
#                        Rojo
#                        Amarillo o
#                        Verde: ''')
# #Convertir el texto ingresado a minusculas para evitar errores
# colorEnMinusculas = colorIngresado.lower()

# if colorEnMinusculas == "rojo":
#     print(f"Rojo: Debes detenerte")
# elif colorEnMinusculas == "amarillo":
#     print("Amarillo: Debes tener precaucion")
# elif colorEnMinusculas == "verde":
#     print("Verde: Puedes avanzar")
# else:
#     print("El color ingresado no es correcto")

#------------------------------------