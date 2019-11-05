# diccionario {'llave':'valor'}
alumno={'num_cta':'201647779','nombre':'jose','paterno':'Perez'}

alumno={'num_cta':'201647779',
        'nombre':('jose','Perez','Garcia'),
        'paterno':'Perez',
        'semestre': 1,
        'promedio':0.0,
        'materia':['CyP','algebra','Calculo','Geometria','IntroICO'],
        'regular':True,
        'lagrimas_por_examen': 5,
        'direccion':{
            'calle':'Rancho Sequito',
            'colonia':'Impulsora Popular Avicola',
            'numero':1000,
            'cp':17570,
            'del_mun':'Nezahualcoyotl',
            'estado':{
                'id':15,
                'nombre':'Estado de Mexico',
                'corto':'EdoMex'
                }
            }
        }

print(alumno['direccion']['estado']['nombre'][10::].upper())
print(alumno)
"""
print(alumno['nombre'])   
print(alumno)
print(alumno['nombre'][1])
print(alumno['direccion']['cp'])
print(alumno['direccion']['estado']['corto'])
print(alumno['materia'][3::])
print(alumno['materia'][1].upper())

print(alumno['direccion']['estado'])
"""
#Son mutables
alumno['curso_ingles']= True
print(alumno)

# funcion keys()

llaves = alumno.keys()
print(llaves)
for llave in llaves:
    print("--------")
    print(llave)
    print('..........')
    print(alumno[llave])
    print("++++++++")
#funcion values
for val in alumno.values():
    print('.....')
    print(val)
    print('++++++++++++')

# funcion items()
for elem in alumno.items():
    print('....')
    print(elem)
    print('+++++++++++')


       
