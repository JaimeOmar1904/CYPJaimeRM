SUMPAR = 0
SUMIMP = 0
CUEPAR = 0
for i in range(0,271,1):
    NUM = int(input("Escribe un nuemro entero: "))
    if NUM !=0:
        if ((-1) ** NUM)>0:
            SUMPAR += NUM
            CUEPAR += 1
        else:
            SUMIMP += NUM
PROPAR = SUMPAR / CUEPAR
print(f"El promedio de los numeros pares son: {PROPAR} y la acumulación de los numeros pares y impares son:{SUMIMP}")
print("Fin del programa")
