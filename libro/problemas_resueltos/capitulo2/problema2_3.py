print(f"Raices reales")
A = float(input("Escribe la letra A: "))
B = float(input("Escribe la letra B: "))
C = float(input("Escribe la letra C: "))
DIS = B**2-4*A*C
if DIS>=0:
    X1 = ((-B)+DIS**0.5)/2*A
    X2 = ((-B)-DIS**0.5)/2*A
    print(f"X1={X1} Y X2={X2}")
print("Fin de programa")
