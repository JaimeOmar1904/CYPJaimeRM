NUM = int(input("Escribe una variable de tipo entero:" ))
while NUM>0:
    if NUM !=1:
        NUM = int(input("Escribe una variable de tipo entero:" ))
        if ((-1)**NUM)>0:
            NUM = NUM/2
        else:
            NUM = NUM*3+1
    print(f"Su numero es:",NUM)
print(f"NUM TIENE QUE SER UN ENTERO POSITIVO")
