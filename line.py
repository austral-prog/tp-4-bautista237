def line():
A = float(input("Ingrese el coeficiente A: "))
B = float(input("Ingrese el coeficiente B: "))

X1 = float(input("Ingrese el coeficiente X1: "))
X2 = float(input("Ingrese el coeficiente X2: "))

Y1 = A*X1 + B
Y2 = A*X2 + B

print(f"El coeficiente A de su ecuación de la recta es: {A}")
print(f"El coeficiente B de su ecuación de la recta es: {B}\n")

print(f"El punto P1 tiene coordenadas: ({X1}, {Y1})")
print(f"El punto P2 tiene coordenadas: ({X2}, {Y2})")

distance = ((X2-X1)**2 + (Y2-Y1)**2)**0.5

print(f"\nPara la siguiente ecuación:\n\tY = {A}X + {B}\n")
print(f"Dados los siguientes puntos:\n\tP1 ({X1}, {Y1})\n\tP2 ({X2}, {Y2})\n")
print(f"La distancia entre ellos es: {distance:.4f}")
