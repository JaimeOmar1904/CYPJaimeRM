NOM = 0
SUE = float(input("Cual es tu sueldo:"))
while SUE!=-1:
    if SUE<1000 and SUE == True:
        NSUE = SUE*1.15
    else:
        NSUE = SUE*1.12
    NOM += NSUE
    print(f"{NSUE}")
    SUE = float(input("Cual es tu sueldo:"))
print(f"Sueldo del trabajador:{NOM}")
