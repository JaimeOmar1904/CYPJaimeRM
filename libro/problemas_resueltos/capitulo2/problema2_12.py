SUE = int(input("Cual es el sueldo del trabajador: "))
CATE = int(input("Cual es la categoria del trabajador: "))
HE = int(input("Cuantas horas extras tienes: "))
if CATE == 1:
    PHE = 30
elif CATE == 2:
    PHE = 38
elif CATE == 3:
    PHE = 50
elif CATE == 4:
    PHE = 70
elif CATE == CATE:
    PHE = 0
if HE>30: 
    NSUE = SUE+30*PHE
else: 
 NSUE = SUE+HE*PHE

print(f"Tu nuevo sueldo es ${NSUE}")
