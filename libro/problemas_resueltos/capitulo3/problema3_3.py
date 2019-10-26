SERIE = 0
N = int(input("Ingresa una variable de tipo entero: "))
BAND = 'T'
i = 1
for i in range(1,N,1):
    if BAND =='T':
        SERIE = SERIE+1/i
        BAND = 'F'
    else:
        SERIE = SERIE-1/i
        BAND = 'T'
print(f"La serie es: {SERIE}")
