MAT = int(input("Cual es tu matricula: "))
CARR = str(input("Cual es tu carrea: "))
SEM = int(input("Cual es tu semestre: "))
PROM = float(input("Cual es tu promedio: "))
if CARR == 'Economia': 
    if SEM >= 6 and PROM > 8.8:
        print(f"{MAT} {CARR}Y Aceptado")

elif CARR == 'Computacion': 
    if SEM > 6 and PROM > 8.5:
        print(f"{MAT} {CARR} Y Aceptado")

elif CARR == 'Contabilidad' or CARR == 'Administracion':
    if SEM > 5 and PROM > 8.5:
        print(f"Tu matricula es {MAT} y la carrera es {CARR} estas Aceptado")
else:
    print(f"Opción no valida")
print("Fin del programa")
