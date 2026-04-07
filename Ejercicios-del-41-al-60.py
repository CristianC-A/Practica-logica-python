#Ejericios del 41 al 60 aprendeindo Python y desarrollando habilidades de logica de programacion
#Cristian Álvarez

#Ejercicio 41
#Mostrar números del 1 al 10: Sistema de prueba que necesita mostrar una secuencia.
#Mostrar los números del 1 al 10 uno por uno.

# for i in range(1, 11):
#     print(i)
    
#-----------------------------------------    

#Ejercicio 42
#Mostrar números pares hasta 100: Sistema estadístico.
#Mostrar todos los pares entre 1 y 100.

# for i in range(1, 101):
#     if i%2 == 0:
#         print(i)
        
#---------------------------------------------
        
#Ejercicio 43
# Sumar números del 1 al 100: Sistema financiero.
#Calcular la suma total.
# suma = 0
# for i in range(101):
#     suma += i
#     print(suma)

#-----------------------------------------

#Ejercicio 44
#Tabla de multiplicar: App educativa.
# Pedir un número.
#Mostrar su tabla del 1 al 10.

# while True:
#     entrada = input("Ingresa un numero del 1 al 9: ")
    
#     if not entrada.isdigit():
#         print("Error: no ingresaste un numero. Intenta de nuevo")
#         continue
    
#     numero = int(entrada)
    
#     if numero > 9 or numero < 1:
#         print("Error: Debes ingresar un numero entre 1 y 9. Intenta de nuevo")
#         continue
    
#     print(f"La tabla del {numero}")
#     for i in range(1, 11):
#         print(f"{numero} * {i} = {numero * i}")
        
#     break

#-------------------------

#Ejercicio 45
# Contar vocales: Procesador de texto.
# Pedir palabra.
# Contar cuántas vocales tiene.

# letras = input("Ingresa una palabra para contar sus letras: ")
# contador = 0
# for letra in letras:
#     contador += 1
    
# print(f"{letras} tiene {contador} caracteres")

#-----------------------------------

#Ejercicio 46
# Pedir números hasta ingresar 0: Sistema de captura.
# Requisitos
# Pedir números.
# Terminar cuando ingrese 0.
# Mostrar cuántos ingresó.

# print("Se termina cuando ingreses 0")
# contador = 0
# while True:
#     numero_ingresado = input("Ingresa un numero, cuando ingreses 0 se termina: ")
#     if not numero_ingresado.isdigit():
#         print("No ingresaste un numero. Intenta de nuevo")
#         continue
#     elif numero_ingresado != "0":
#         contador += 1
#     elif numero_ingresado == "0":
#         print("Ingresaste 0, adios!")
#         print(f"{contador} intentos de numeros, antes de ingresar 0")
#         break
    
#==================================

#Ejercicio 47
# Factorial: Motor matemático.
# Requisitos
# Pedir número.
# Calcular factorial.

# print("Calcular el factorial de un numero ingresado")
# factorial = 1
# numero_calcular_factorial = int(input("Ingresa un numero para calcular su factorial: "))
# for i in range(1, numero_calcular_factorial+1):
#     factorial *= i

# print(f"El factorial de {numero_calcular_factorial} es: {factorial:,}")

#=======================================

# Ejercicio 48
# Serie Fibonacci: Algoritmos clásicos.
# Requisitos
# Mostrar N términos de Fibonacci.

# print("Serie Fibonacci")
# n_fibonacci = int(input("Ingresa el numero para la crear la secuencia Fibonacci: "))
# a = 0
# b = 1
# for i in range(n_fibonacci):
#     print(a)
    
#     nuevo = a + b
#     a = b
#     b = nuevo
    
#===================================

# Ejercicio 49
# Contar positivos: Sistema estadístico.
# Requisitos
# Pedir varios números.
# Contar cuántos son positivos.

print("Ingresar numeros y contar el numero de positivos")
contador = 0
numeros_ingresados = []
numeros_positivos = []
while True:
    entrada_usuario = int(input("Ingresa un numero. Si quieres terminar ingresa 0: "))
    numeros_ingresados.append(entrada_usuario)

    if entrada_usuario > 0:
        numeros_positivos.append(entrada_usuario)
        contador += 1
        continue
    elif entrada_usuario == 0:
        print("Ingrsaste 0.")
        break

print(f"Ingrsaste {contador} numeros positivos")
print(f"Todos los numeros que ingresaste: {numeros_ingresados}")
print(f"Todos los numeros positivos que ingresate: {numeros_positivos}")

#=========================================

#Ejercicio 50
# Promedio de N números
# Requisitos
# Pedir cuántos números.
# Calcular promedio.

