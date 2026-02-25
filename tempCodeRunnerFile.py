numeroAMultiplicar = int(input("Ingresa un numero del 1 al 9: "))
resultadoMultiplicacion = 0
if numeroAMultiplicar > 9 and numeroAMultiplicar < 1:
    print("Debias ingresar un numero del 1 al 9")
elif True:
    for i in range(1, 11):
        resultadoMultiplicacion = numeroAMultiplicar * i
        print(f"{numeroAMultiplicar} *  {i} = {resultadoMultiplicacion}")