MAT = int(input("Escribe tu matricula con numeros enteros: "))
CAL1 = float(input("La primera calificación: "))
CAL2 = float(input("La segunda calificación: "))
CAL3 = float(input("La tercera calificación: "))
CAL4 = float(input("La cuarta calificación: "))
CAL5 = float(input("La quinta calificación: "))
PRO =(CAL1 + CAL2 + CAL3+ CAL4 + CAL5)/5
if PRO>=6:
    print(f"Tu matricula es:{MAT} y tu calificaión:{PRO}")
    print(f"Aprobado")
else:
    print(f"Tu matricula es:{MAT} y tu calificación:{PRO}")
    print(f"Reprobado")
print("Fin del programa")
