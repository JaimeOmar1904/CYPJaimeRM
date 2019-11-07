def sumar(x , y):
    z = x + y
    return z
def restar (x , y):
    return x - y
def mi_print ( texto ):
    print(f"Este es mi print: {texto} ")
def multiplica( valor , veces ):
    if veces == None :
        print("Debes enviar el segundo argumento de la funcion")
    else:
        print( valor * veces )
def comanda( mesa, comensal , entrada , medio ,fuerte ,postre="quesadilla"):
    print(f"Mesa: {mesa} Comensal: {comensal}")
    print(f"\t Entrada: { entrada }")
    print(f"\t segundo tiempo: { medio }")
    print(f"\t Plato fuerte: { fuerte } ")
    print(f"\t Postre: { postre }")

def comanda2( **comida ):
    llaves = comida.keys()
    for elem in llaves:
        print(elem, "->", comida[elem])
        

def imprime_argumentos(*argumentos):
    for index in range(len(argumentos) ):
        print(argumentos[index])


    
def main():
    a = 10
    b = 5
    c = sumar(a,b)
    print(f"la suma de {a} y {b} es {c}")
    c = restar(a,b)
    print(f"La resta de {a} y {b} es {c}")
mi_print("Hola!!!")
multiplica( 10 , 3 )
multiplica (10 , None )
multiplica ( 'hola' , 3 )

if __name__ == '__main__':# ¿Se mando a ejecujar (interpretar) este archivo?
    main()
mi_print("Hola!!!")
multiplica( 10 , 3 )
multiplica (10 , None )
multiplica ( 'hola' , 3 )
comanda(2,1,"Ensalada" ,"Sopa de rana","Filete de pompi de sirena","Flan" )
comanda(entrada ="filete",medio="sopa de rana",fuerte="gordita",postre="sal",mesa=1,comensal=3)
comanda(entrada ="filete",medio="sopa de rana",fuerte="gordita",mesa=1,comensal=3)
imprime_argumentos('Hola',True, 3.1416, 1000, {'id':'sc01', 'nombre':'juan'})

comanda2(entrada ="filete",medio="sopa de rana",fuerte="gordita",postre="Flan",mesa=1,comensal=3, bebida= 'coca')
