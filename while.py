otra = bool(int(input("Hay más alumnos(0 No, 1 Si:")))
suma = 0.0
cont = 0
while(otra == True):
    cal = float(input("calificación:"))
    cont += 1
    suma += cal
    otra = bool(int(input("Hay más alumnos(0 No, 1 Si:")))
print("Suma",suma)
print("Promedio:",suma/cont)
print("Fin del programa")
