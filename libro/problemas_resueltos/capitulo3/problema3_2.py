BAND = 'T'
SUMSER = 0
I = 2
while(I<=1800):
    SUMSER += I
    print(f"{I}")
    if BAND == 'T':
        BAND = 'F'
        I = I+3
    else:
        BAND = 'T' 
        I = I+2
print(f"{El sumser es: {SUMSER}")
