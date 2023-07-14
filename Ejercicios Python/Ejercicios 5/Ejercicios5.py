""" Se pide generar un conjunto de 50 numeros, entre 1 y 100 (incluidos) que representan las edades de una población humana.
En base a esos valores, almacenados en alguna colección adecuada, se solicita respuesta a los siguientes puntos:

Calcular el valor promedio (entero) de entre los numeros generados
Determinar cuantos valores caen en los diferentes cuartiles (25%, 50%, 75%)
Considerando estos datos, La población es joven (por debajo del 2º cuartil) ? """
import random

coleccion_numeros=[]
primer_cuartil=0
segundo_cuartil=0
tercer_cuartil=0
cuarto_cuartil=0

acumulador=0
for i in range (50):
    numero= random.randint(1,100)
    acumulador+=numero
    if numero<=25:
        primer_cuartil+=1
    elif numero>25 and numero<=50:
        segundo_cuartil+=1
    elif numero>50 and numero<=75:
        tercer_cuartil+=1
    else:
        cuarto_cuartil+=1
    coleccion_numeros.append(numero)

poblacion_joven=primer_cuartil+segundo_cuartil
poblacion_adulta=tercer_cuartil+cuarto_cuartil

promedio=acumulador/50
print("La coleccion de numeros es de : {},\n El promedio de los numeros es de : {}".format(coleccion_numeros,promedio))
print("Informacion de los Cuartiles :\nPrimer Cuartil: {},\nSegundo Cuartil :{},\nTercer Cuartil: {},\n Cuarto Cuartil :{}".format(primer_cuartil,segundo_cuartil,tercer_cuartil,cuarto_cuartil))

if poblacion_joven>poblacion_adulta:
    print("La poblacion que mas predomina es la Poblacion Joven con {} personas frente a la Poblacion Adulta con {} personas".format(poblacion_joven,poblacion_adulta))
elif poblacion_adulta>poblacion_joven:
    print("La poblacion que mas predomina es la Poblacion Adulta con {} personas frente a la Poblacion Joven con {} personas".format(poblacion_adulta,poblacion_joven))
else:
    print("Hubo un empate entre las poblaciones")