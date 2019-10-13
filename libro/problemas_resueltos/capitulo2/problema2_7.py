print(f"Escribe 3 numeros que no sean iguales A,B,C.")
A = int(input("Escribe una variable de tipo entero A: "))
B = int(input("Escribe una variable de tipo entero B: "))
C = int(input("Escribe una variable de tipo entero C: "))
if A<B:
    if B<C:
        print(f"Los números están en orden creciente")
    else:
        print(f"Los números no están en oredn creciente")
else:
    print(f"Los números no están en orden creciente")
print("Fin del programa")
