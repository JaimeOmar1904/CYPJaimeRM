MED = 0
CHI = 0
GRA = 0
N = int(input("Cuales son los numeros de ventas del vendedor: "))
for i in range(1,N,1):
    V = float(input("De cuanto es tu venta:$ "))
    if V<=200:
        CHI += 1
    else:
        if V<400:
            MED += 1
        else:
            GRA += 1
print(f"CHI es:",CHI)
print(f"La acumulacion de ventas menores:",MED)
print(f"GRA es:",GRA)
print("Fin del programa")
