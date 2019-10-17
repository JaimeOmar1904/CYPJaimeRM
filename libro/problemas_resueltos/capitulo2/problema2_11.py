CLAVE = int(input("Escribe tu clave geografica (12,15,18,19,23,25 y 29): "))
NUMIN = int(input("Escribe cuantos minutos duro tu llamada: "))
if CLAVE == 12:
    COST = NUMIN*2

elif CLAVE == 15:
    COST = NUMIN*2.2

elif CLAVE == 18:
    COST = NUMIN*4.5

elif CLAVE == 19:
    COST = NUMIN*3.5

elif CLAVE == 23:
    COST = NUMIN*6

elif CLAVE == 25:
    COST = NUMIN*6

elif CLAVE == 29:
    COST = NUMIN*5

else:
    print(f"Opcion no valida")
print(f"Costo total de la llamada es ${COST} y la Clave = {CLAVE}")
print("Fin del programa")
