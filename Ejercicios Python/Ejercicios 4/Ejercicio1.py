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
""" def cargar_temperaturas():
    temperaturas_promedio=[0]*12
    rango_temperaturas=[2,3,4]
    acumulador=0
    for i in range(12):
        mes=meses_del_anio(i)
        temperatura=float(input("Ingrese la temperatura promedio en {} : ".format(mes)))
        temperaturas_promedio[i]=temperatura
        acumulador+=temperatura
    promedio_anual=acumulador/12
    print(temperaturas_promedio,"El promedio anual de temperaturas es :",promedio_anual)
    for i in range(12):
        if temperaturas_promedio[i]>promedio_anual:
            print("La temperatura en el mes de :",meses_del_anio(i),"fue mayor a la temperatura promedio anual")
        if i==rango_temperaturas[0] or i==rango_temperaturas[1] or i==rango_temperaturas[2]:
            print(temperaturas_promedio[i])
   

def meses_del_anio(n):
    meses={
        0:"enero",
        1:"febrero",
        2:"marzo",
        3:"abril",
        4:"mayo",
        5:"junio",
        6:"julio",
        7:"agosto",
        8:"octubre",
        9:"septiembre",
        10:"noviembre",
        11:"diciembre"
        }
    for mes in meses :
        if n == mes:
            return meses[n]

cargar_temperaturas()
 """
"""
1. Desarrollar un programa que permita cargar una lista de de n elementos, con
números cuyos valores estén entre 10 y 50. Con la lista se pide:
a. Mostrar la lista.
b. Mostrar el porcentaje de números pares del vector.
c. Generar y mostrar un segundo vector con todos aquellos números múltiplos de
3.
"""
""" def cargar_lista_numeros(n):
    lista=[]
    pares=0
    for i in range(n):
        numero=float(input("Ingrese un numero entre el 10 y 50 :"))
        if numero>=10 and numero<=50:
            pass
        else:
            return print("El numero {} es menor a 10 o mayor a 50".format(numero))
        if numero%2==0:
            pares+=1
        lista.append(numero)
    nueva_lista=[]
    for numero in lista:
        if numero%3==0:
            nueva_lista.append(numero)
    porcentaje_numeros_pares=(pares*100)/len(lista)
    print("La lista de numeros es : {} ,\n El porcentaje de numeros pares es de : {}, \n y el nuevo vector de multiplos de 3 es de : {}".format(lista,porcentaje_numeros_pares,nueva_lista))


numeros_a_cargar=int(input("Cuantos numeros vas a cargar: "))
cargar_lista_numeros(numeros_a_cargar) """
"""
1. Desarrollar un programa de Python que permita cargar las notas de alumnos
obtenidos en el primer examen de un curso, se pide:
a. Mostrar el promedio de notas del curso.
b. Mostrar la cantidad de notas superiores al promedio.
c. Mostrar la lista de notas ordenada de manera ascendente.
d. Buscar si al menos un alumno obtuvo la nota x, siendo x una nota ingresada por
teclado
"""
""" def cargar_notas(n):
    acumulador_notas=0
    notas=[]
    for i in range(n):
        nota=float(input("Nota del examen : "))
        acumulador_notas+=nota
        notas.append(nota)
    promedio=acumulador_notas/n
    notas_mayores_promedio=0
    nota_a_buscar=int(input("Nota a buscar :"))
    for nota in notas:
        if nota>promedio:
            notas_mayores_promedio+=1
        if nota == nota_a_buscar:
            print("Un alumno obtuvo la nota que se buscaba")
    notas.sort(reverse=False)
    print("El promedio de las notas del curso es de {},\n La cantidad de notas superiores al promedio fueron de : {}, \n Lista de Notas ordenada : {}".format(promedio,notas_mayores_promedio,notas))
alumnos=int(input("Cuantos alumnos rindieron el examen : "))
cargar_notas(alumnos) """
"""
1. Se pide un programa que cargue n elementos numéricos aleatorios entre 1 y 100
inclusive (usar la función randint() de la librería random) en una lista y realice lo
siguiente:
a. Mostrar la lista
b. Mostrar la lista ordenada de manera descendente.
c. Buscar un elemento x dentro de la lista (x se ingresa por teclado). Si no existe,
informarlo. 
"""
""" def cargar_elementos_random(n):
    lista=[]
    for i in range(n):
        numero=random.randint(1,100)
        lista.append(numero)
    elemento_a_buscar=int(input("Que numero queres saber si existe : "))
    existe_el_numero=False
    for numero in lista:
        if elemento_a_buscar == numero:
            existe_el_numero=True
    print("La lista como tal es : {}".format(lista))
    lista.sort(reverse=True)
    print("La lista ordenada de forma descendente es : {}".format(lista))
    if existe_el_numero== False:
        print("El numero no existe")
    else:
        print("El numero si existe")
    

cantidad_elementos=int(input("Cuantos elementos vas a cargar : "))
cargar_elementos_random(cantidad_elementos) """
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
""" def puntajes_jugadores(n):
    puntajes=[]
    for i in range(n):
        puntaje=random.randint(1,100)
        puntajes.append(puntaje)
    puntajes.sort(reverse=True)
    puntajes_altos=[]
    puntajes_mayores_90=0
    descalificados=0
    for i in range(len(puntajes)):
        if i==0 or i==1 or i==2:
            puntajes_altos.append(puntajes[i])
        if i==0:
            puntaje_mas_alto=puntajes[i]
        if i==(n-1):
            puntaje_mas_bajo=puntajes[i]
        if puntajes[i]>90:
            puntajes_mayores_90+=1
        if puntajes[i]<30:
            descalificados+=1
    diferencia_puntajes=puntaje_mas_alto-puntaje_mas_bajo

    print("Los 3 puntajes mas altos son :{} ,\nLos puntajes que superaron los 90 fueron : {},\nLa diferencia entre el primer puntaje \"{}\" y el ultimo puntaje \"{}\" es de : {},\nLa cantidad de descalificados es de : {}".format(puntajes_altos,puntajes_mayores_90,puntaje_mas_alto,puntaje_mas_bajo,diferencia_puntajes,descalificados))

cuantos_concursantes=int(input("Cuantos concursantes son :"))
puntajes_jugadores(cuantos_concursantes) """