L1 = float(input("Escribe el lado 1 del triangulo: "))
L2 = float(input("Escribe el lado 2 del triangulo: "))
L3 = float(input("Escribe el lado 3 del triangulo: "))
S = (L1 + L2 + L3)/2
AREA = (S*(S-L1)*(S-L2)*(S-L3))**0.5
print(f"El area del triangulo es de {AREA} y su variable auxiliar es {S}")
