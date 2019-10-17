A = int(input("Cual es la tipo de enfermedad que tienes: "))
B = int(input("Cual es la edad del pasiente: "))
C = int(input("Cuantos dias estuviste en el hospital: "))

if A == 1:
    COSTOT = C*25

elif A == 2:
    COSTOT = C*16

elif A == 3:
    COSTOT = C*20

elif A == 4:
    COSTOT = C*32

if (B >= 14 and B <= 22):
    COSTOT = COSTOT*1.10
print(f"Su edad es {B} y su tiempo de hospitalización es {C} dias y debe pagar ${COSTOT}")
