MAY = -100000
MEN = 100000
N = int(input("Ingresa cuantas variables vas poner: "))
for i in range(1,N,1):
    NUM = int(input("Ingresa una variable de tipo entero:"))
    if NUM>MAY:
        MAY = NUM
    if NUM<MEN:
        MEN = NUM
print(f"Almacena el maximo valor",MAY)
print(f"Almacena el minimo valor",MEN)
print("Fin del el programa")
