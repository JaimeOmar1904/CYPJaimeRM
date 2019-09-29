CAL = float(input("Cual es tu calificación: "))
PRO = bool(int(input("Tienes una calificación mayor o igual a 8 (0 NO / 1 SI):")))
if CAL >= 8 and PRO == True:
    print(f"Estas aprobado")
else:
    if CAL < 8 and PRO == False:
        print(f"Estas reprobado")
