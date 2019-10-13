COMPRA = float(input("Cantidad a pagar es de:$"))
if COMPRA<500:
    PAGAR = COMPRA
    print(f"{PAGAR}")
elif COMPRA<=1000:
    PAGAR = COMPRA-(COMPRA*0.05)
    print(f"{PAGAR}") 
else:
    if COMPRA<=7000:
        PAGAR = COMPRA-(COMPRA*0.11)
        print(f"{PAGAR}")
    elif COMPRA<=15000:
        PAGAR = COMPRA-(COMPRA*0.18)
        print(f"{PAGAR}")
    else:
        PAGAR = COMPRA-(COMPRA*0.25)
        print(f"{Pagar}")
print("Fin del programa")
