A = float(input("Cuanto cuesta tu producto: $"))
if A>500:
    IMP = 20*0.30+(A-40)*0.50
    B = A+C
    print(f"{A} y {B}")
elif A>40:
    C = 20*0.30+(A-40)*0.40
    B = A+C
    print(f"{A} y {B}")
else:
    if A>20:
        C = (A-20)*0.30
        B = A+C
        print(f"{A} y {B}")
    else:
        C = 0
        B = A+C
        print(f"{A} y {B}")
print("Fin del programa")
