arsu = 0
arno = 0
mersu = 50000
arce = 0
for i in range(1 , 13 , 1):
    print(f"mes {i}:")
    rno = int(input("Promedio de lluvias del mes Zona norte:"))
    rce = int(input("Promedio de lluvias del mes Zona Centro:"))
    rsu = int(input("Promedio de lluvias del mes Zona Sur:"))

    arno += rno
    arce += rce
    arsu += rsu
    if rsu<mersu:
        mersu = rsu
        mes = i
prorce = arce/12
print(f"Promedio region centro: {prorce} ")
print(f"Mes con menor lluvia de reg. sur : {mes} ")
print(f"Region del mes con menor lluvia es: {mersu}")

if arno > arce:
    if arno > arsu:
        print(f"La region con mayor lluvia es la region norte")
    else:
        print(f"La region con mayor lluvia es la region sur")
elif arce>arsu:
    print(f"La region con mayor lluvia es la region centro")
else:
    print(f"La region con mayor lluvia es la region sur")
print("Fin del programa")
               
