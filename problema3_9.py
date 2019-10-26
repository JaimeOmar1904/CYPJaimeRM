SERIE = 0
N = int(input("Escribe una variable de tipo entero:"))
for i in range(1,N,1):
    SERIE = SERIE+i**i
print(f"La suma de la serie:",SERIE)
print("Fin del programa")
