#print tiene 4 formas de uso
"""
1 .- con comas
2 .- con signo '+'
3 .- con la función format ()
4 .- Es con una variable de format ()
"""
# con comas , concatenar agregado
# un espacio y haciendo casting de tipo
edad = 10
nombre = "Juan"
estatura = 1.67
print (edad , estatura , nombre )
#Con '+' hace lo mismo pero no hace el casting automático
#No agrega espacio
print(str(edad) + str(estatura) + nombre)
# Función format ()

print("Nombre:{} Edad:{} Estatura:.{}".format(nombre, edad))

# 3.- función format()
print("Nombre: (1) Edad: (0) ".format (nombre, edad ,estatura))

# 4.- con una variante de format () simplificada
print(f"Nombre: \"(nombre)\" \nEdad:\t(edad) ")
print("Solo hoy dos tipos de personas, las que saben binario y las que no",end=" ")
print("otra linea")
