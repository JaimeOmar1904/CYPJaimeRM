COMPRA = float(input("Cantidad a pagar es de: $"))
if COMPRA<500:
    PAGAR = COMPRA
    print(f"Su compra es de ${COMPRA} y el total a pagar es ${PAGAR}")
elif COMPRA<=1000:
    PAGAR = COMPRA-(COMPRA*0.05)
    print(f"Su compra es de ${COMPRA} y el total a pagar es ${PAGAR}") 
else:
    if COMPRA<=7000:
        PAGAR = COMPRA-(COMPRA*0.11)
        print(f"Su compra es de ${COMPRA} y el total a pagar es ${PAGAR}")
    elif COMPRA<=15000:
        PAGAR = COMPRA-(COMPRA*0.18)
        print(f"Su compra es de ${COMPRA} y el total a pagar es ${PAGAR}")
    else:
        PAGAR = COMPRA-(COMPRA*0.25)
        print(f"Su compra es de ${COMPRA} y el total a pagar es ${PAGAR}")
print("Fin del programa")
