SUMOTR = 0
SUMPOS = 0
CUEPOS = 0
N = int(input("Ingresa cuantas variable de tipo entero vas agregar: "))
for i in range(0,N,1):
    NUM  = int(input("Variable de tipo entero: "))
    if NUM>0:
        SUMPOS += NUM
        CUEPOS += 1
    else:
        SUMOTR += NUM
PROGEN = (SUMPOS + SUMOTR)/N
PROPOS = (SUMPOS/CUEPOS)
print(f"Los numeros positivos son",CUEPOS)
print(f"El promedio de los numeros positivos",PROPOS)
print(f"Promedio de los numeros menores",PROGEN)
