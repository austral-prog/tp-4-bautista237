   from math import sqrt
def line():
    A=float(input("Ingrese el coeficiente A: "))
    B=float(input("Ingrese el coeficiente B: "))
    X1=float(input("Ingrese el coeficiente X1: "))
    X2=float(input("Ingrese el coeficiente X2: "))
    Y1=(AX1+B)
    Y2=(AX2+B)
    distancia=(sqrt((X2-X1)2+(Y2-Y1)2))
    print("El coeficiente A de su ecuación de la recta es:",A)
    print("El coeficiente B de su ecuación de la recta es:",B)
    print("El coeficiente X1 de su ecuación de la recta es:",X1)
    print("El coeficiente X2 de su ecuación de la recta es:",X2)
    print(f"\nPara la siguiente ecuación:\n\tY = {A}X + {B}\n\nDados los siguientes puntos:\n\tP1 ({X1}, {Y1})\n\tP2 ({X2}, {Y2})\n\nLa distancia entre ellos es: {distancia}")
