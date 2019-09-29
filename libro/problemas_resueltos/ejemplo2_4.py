SUE = float(input("Cual es tu sueldo:$ "))
a = bool(int(input("Ganas menos de $1000 pesos (0 NO / 1 SI):")))
if SUE < 1000 and a == True:
    NSUE = SUE*1.15
    print(f"Tu suedo nuevo es de ${NSUE}")
    print(f"Fin del programa")
else:
    if SUE >= 1000 and  a == False:
        NSUE = SUE*1.12
        print(f"Tu suedo nuevo es de ${NSUE}")
        print(f"Fin del programa")
