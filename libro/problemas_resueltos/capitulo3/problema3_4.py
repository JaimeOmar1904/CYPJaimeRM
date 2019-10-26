NOM = 0
SUEI = bool(int(input("Hay más sueldos de trabajadores(0 No, 1 si): "))) 
while(SUEI == True):
    SUE = float(input("Dame el sueldo del trabajador:"))
    if SUE<1000:
        NSUE = SUE*1.15
        NOM += NSUE
    else:
        NSUE = SUE*1.12
        NOM += NSUE
    SUEI = bool(int(input("Hay más sueldos de trabajadores(0 No, 1 si): ")))
    print(f"El nuevo sueldo del trabajador es de $",NSUE)
print(f"El sueldo acumulado de los trabajadores es de $",NOM,NOM)
