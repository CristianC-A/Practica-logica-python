#Ejericios del 41 al 60 aprendeindo Python y desarrollando habilidades de logica de programacion
#Cristian Álvarez

#Ejercicio 41
#Mostrar números del 1 al 10: Sistema de prueba que necesita mostrar una secuencia.
#Mostrar los números del 1 al 10 uno por uno.

for i in range(1, 11):
    print(i)
    
#-----------------------------------------    

#Ejercicio 42
#Mostrar números pares hasta 100: Sistema estadístico.
#Mostrar todos los pares entre 1 y 100.

for i in range(1, 101):
    if i%2 == 0:
        print(i)
        
#---------------------------------------------
        
#Ejercicio 43
# Sumar números del 1 al 100: Sistema financiero.
#Calcular la suma total.
suma = 0
for i in range(101):
    suma += i
    print(suma)

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

letras = input("Ingresa una palabra para contar sus letras: ")
contador = 0
for letra in letras:
    contador += 1
    
print(f"{letras} tiene {contador} caracteres")

#-----------------------------------

#Ejercicio 46
# 