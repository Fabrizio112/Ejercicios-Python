import random
"""
1. Desarrollar un programa en Python que permita cargar las temperaturas
promedio en cada mes del país, con estos datos se pide:
a. Mostrar la lista.
b. Mostrar el promedio anual de temperaturas.
c. Mostrar los meses del año en los que la temperatura fue mayor a la
temperatura promedio de todo el año.
d. Mostrar el promedio de temperaturas para un determinado trimestre,
ingresar el rango de los tres meses al comenzar el programa.
"""
def temperaturas_promedio():
    temperaturas={
        "enero":None,
        "febrero":None,
        "marzo":None,
        "abril":None,
        "mayo":None,
        "junio":None,
        "julio":None,
        "agosto":None,
        "septiembre":None,
        "octubre":None,
        "noviembre":None,
        "diciembre":None
    }
    acumulador_de_temperaturas=0
    for temperatura in temperaturas:
        temp=float(input("Enter temp in {}: ".format(temperatura)))
        acumulador_de_temperaturas+=temp
        temperaturas[temperatura]=temp
    promedio_anual_temperaturas=acumulador_de_temperaturas/12
    for temperatura in temperaturas:
        if temperaturas[temperatura]>promedio_anual_temperaturas:
            print("En el mes {}, la temperatura {} supero a la temperatura anual : {}".format(temperatura,temperaturas[temperatura],promedio_anual_temperaturas))
    print(temperaturas ,"\nEl promedio anual de temperaturas fue: {}".format(promedio_anual_temperaturas))
#temperaturas_promedio()

"""
1. Desarrollar un programa que permita cargar una lista de de n elementos, con
números cuyos valores estén entre 10 y 50. Con la lista se pide:
a. Mostrar la lista.
b. Mostrar el porcentaje de números pares del vector.
c. Generar y mostrar un segundo vector con todos aquellos números múltiplos de
3.
"""
def cargar_lista():
    num=float(input("Enter a number: "))
    numeros=[]
    contador_pares=0
    vector_multiplos_3=[]
    while num>=10 and num<=50:
        numeros.append(num)
        num=float(input("Enter a number: "))
    for num in numeros:
        if num%2==0:
            contador_pares+=1
        if num%3==0:
            vector_multiplos_3.append(num)
    porcentaje_de_pares=contador_pares*100/len(numeros)
    print(numeros,"\nPorcentaje de numeros pares: {}\nVector multiplos de 3 : {}".format(porcentaje_de_pares,vector_multiplos_3))
#cargar_lista()
"""
1. Desarrollar un programa de Python que permita cargar las notas de alumnos
obtenidos en el primer examen de un curso, se pide:
a. Mostrar el promedio de notas del curso.
b. Mostrar la cantidad de notas superiores al promedio.
c. Mostrar la lista de notas ordenada de manera ascendente.
d. Buscar si al menos un alumno obtuvo la nota x, siendo x una nota ingresada por
teclado
"""
def cargar_notas_alumnos():
    cantidad_alumnos=int(input("Cuantas notas va a cargar: "))
    buscar_nota=int(input("Nota a buscar: "))
    lista_notas=[]
    acumulador_notas=0
    for i in range(cantidad_alumnos):
        nota=int(input("Nota Alumno : "))
        acumulador_notas+=nota
        lista_notas.append(nota)
    promedio_notas=acumulador_notas/len(lista_notas)
    contador_notas_mayores_promedio=0
    lista_ascendente=sorted(lista_notas)
    for nota in lista_notas:
        if nota > promedio_notas:
            contador_notas_mayores_promedio+=1
        if nota== buscar_nota:
            print("Se encontro la nota que se estaba buscando")
           
    print("El promedio de las notas del curso es : {}\nHubo {} notas que fueron mayores al promedio\nLista de notas Ascendente:{}".format(promedio_notas,contador_notas_mayores_promedio,lista_ascendente))
#cargar_notas_alumnos()
"""
1. Se pide un programa que cargue n elementos numéricos aleatorios entre 1 y 100
inclusive (usar la función randint() de la librería random) en una lista y realice lo
siguiente:
a. Mostrar la lista
b. Mostrar la lista ordenada de manera descendente.
c. Buscar un elemento x dentro de la lista (x se ingresa por teclado). Si no existe,
informarlo. 
"""
def cargar_elementos_aleatorios():
    cuantos_elementos=int(input("Cuantos elementos se van a cargar: "))
    lista_aleatoria=[]
    buscar_elemento=int(input("Buscar X elemento : "))
    elemento_encontrado=0
    for i in range(cuantos_elementos):
        num=random.randint(1,100)
        lista_aleatoria.append(num)
    for num in lista_aleatoria:
        if num==buscar_elemento:
            elemento_encontrado+=1
    if elemento_encontrado >=1:
        print("Se encontro el elemento")
    else:
        print("No se encontro el elemento")
    lista_descendente=sorted(lista_aleatoria,reverse=True,)
    print(lista_aleatoria,"\n\n\n\n\n",lista_descendente)
#cargar_elementos_aleatorios()
"""
1. Desarrollar un programa que permita procesar el puntaje obtenido por n
concursantes en una competencia. Para ello, grabar en una lista los puntajes
obtenidos (generarlos con un valor aleatorio entre 1 y 100 (inclusive), se pide:
a. Mostrar los tres mejores puntajes generados.
b. Mostrar cuántos puntajes superaron el valor de 90.
c. Mostrar la diferencia entre el mayor y el menor puntaje.
d. Mostrar la cantidad de concursantes que quedaron descalificados, esto es si su
puntaje es menor a 30.
"""
def puntajes_obtenidos():
    cuantos_concursantes=int(input("Cuantos concursantes son: "))
    lista_concursantes=[]
    cantidad_superar_90=0
    cantidad_descalificados=0
    for i in range(cuantos_concursantes):
        puntaje=random.randint(1,100)
        if puntaje>90:
            cantidad_superar_90+=1
        if puntaje<30:
            cantidad_descalificados+=1
        lista_concursantes.append(puntaje)
    lista_descendente=sorted(lista_concursantes,reverse=True)
    mayor_puntaje=lista_descendente[0]
    menor_puntaje=lista_descendente[-1]
    lista_mejores_3_puntajes=[]
    diferencia=mayor_puntaje-menor_puntaje
    for i in range(3):
        lista_mejores_3_puntajes.append(lista_descendente[i])
    print("Los mejores 3 puntajes son : {}\nLa cantidad de puntajes que superaron 90 fueron: {}\nLa diferencia entre el mayor puntaje {} y el menor puntaje {} fue de : {}\nLa cantidad de descalificados fue de : {}".format(lista_mejores_3_puntajes,cantidad_superar_90,mayor_puntaje,menor_puntaje,diferencia,cantidad_descalificados))
#puntajes_obtenidos()