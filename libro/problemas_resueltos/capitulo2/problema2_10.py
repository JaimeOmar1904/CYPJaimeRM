a = int(input("introduce un entero positivo: "))
b = int(input("introduce otro valor entero positivo: "))
c = int(input("introduce otro valor entero positivo: "))
if a > b:
    if  a > c:
        print(f"a es el mayor con valor a {a}")
    elif a == c:
        print(f"a y c son iguales a {a} y son los mayores")
    else:
        print(f"c que vale {c} es el mayor")
elif a == b:
    if a > c:
        print(f"a y b son los mayores con valor {b}")
    elif a == c:
        print(f" los tres son iguales a {b}")
    else:
        print(f"c que vale {c} es el mayor")
elif b > c: 
    print(f"b que vale {b} es el mayor")
elif b == c:
    print(f"b y c son los mayores con valor { b }")
else:
    print(f"c es el mayor con valor {c}")
print("fin del programa")
