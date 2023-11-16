""" Se pide generar un conjunto de 50 numeros, 
entre 1 y 100 (incluidos) que representan las edades
 de una población humana.
En base a esos valores, almacenados en alguna 
colección adecuada, se solicita respuesta a los
 siguientes puntos:

Calcular el valor promedio (entero) de entre los 
numeros generados
Determinar cuantos valores caen en los diferentes 
cuartiles (25%, 50%, 75%)
Considerando estos datos, La población es joven 
(por debajo del 2º cuartil) ? """
import random
 
def ejercicio():
    edades_poblacion=[]
    acumulador=0
    for i in range(50):
        num = random.randint(1,100)
        edades_poblacion.append(num)
        acumulador+=num
    promedio=acumulador/len(edades_poblacion)
    primer_cuartil=0
    segundo_cuartil=0
    tercer_cuartil=0
    cuarto_cuartil=0
    for edad in edades_poblacion:
        if edad<=25:
            primer_cuartil+=1
        elif edad>25 and edad<=50:
            segundo_cuartil+=1
        elif edad>50 and edad<=75:
            tercer_cuartil+=1
        else:
            cuarto_cuartil+=1
    poblacion_joven=primer_cuartil+segundo_cuartil
    poblacion_adulta=tercer_cuartil+cuarto_cuartil
    print(f"El valor promedio entre los numeros generados :{promedio}\nPrimer Cuartil: {primer_cuartil}\nSegundo Cuartil: {segundo_cuartil}\nTercer Caurtil: {tercer_cuartil}\nCuarto Cuartil: {cuarto_cuartil}")
    if poblacion_adulta>poblacion_joven:
        print(f"La poblacion mayoritaria es adulta con: {poblacion_adulta}")
    else:
        print(f"La poblacion mayoritaria es joven con: {poblacion_joven}")
ejercicio()