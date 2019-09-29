SUE = int(input("Cual es tu sueldo:$ "))
PRE = bool(int(input("Ganas menos de $1000 pesos (0 NO / 1 SI):")))
if SUE<1000 and  PRE == True:
    AUM = SUE*0.15
    NSUE = SUE + AUM
    print(f"Tu sueldo nuevo es de ${NSUE}")
print(f"Fin del programa")
