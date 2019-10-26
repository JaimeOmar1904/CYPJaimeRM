SUMOTR = 0
SUMPOS = 0
CUEPOS = 0
N = int(input("Ingresa una variable de tipo entero: "))
for i in range(0,N,1):
    NUM  = int(input("Variable de tipo entero: "))
    if NUM>0:
        SUMPOS += NUM
        CUEPOS += 1
    else:
        SUMOTR += NUM
PROGEN = (SUMPOS + SUMOTR)/N
PROPOS = (SUMPOS/CUEPOS)
print(f"Los numeros positivos son:{CUEPOS} propos es:{PROPOS}  y progen es: {PROGEN}")
