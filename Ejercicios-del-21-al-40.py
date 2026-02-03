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

print("Clasificación de notas")
nota = int(input("Ingresa una nota entre 0 y 100: "))
if nota < 101 and nota > 89:
    print(f"La nota es: A")
elif nota < 90 and nota > 79:
    print("La nota es: B")
elif nota < 80 and nota > 69:
    print("La nota es: C")
elif nota < 70 and nota > 59:
    print("La nota es: D")
elif nota < 60:
    print("La nota es: F")
else:
    print("La nota ingresada es invalida")