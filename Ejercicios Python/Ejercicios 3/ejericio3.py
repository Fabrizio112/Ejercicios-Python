"""
1. Desarrollar un programa en Python que permita cargar por teclado una sucesión de números. El usuario
deberá cargar un 0(cero) para indicar el final del proceso de carga. El cero no debe considerarse un dato a
procesar. El programa debe:
a. Determinar cuántos de los números ingresados son mayores que n1 y menores que n2 (cargar
previamente por teclado los números n1 y n2).
b. Determinar el porcentaje que el total de números calculado en el punto 1 representa en el total de
números cargados."""

""" def cargar_numeros():
    proceso_de_carga=float(input("Continuar la Carga (Si/1,No/0) :"))
    n1=float(input("Cuanto vale N1: "))
    n2=float(input("Cuanto vale N2: "))
    mayores_n1=0
    menores_n2=0
    numeros_totales=0
    while proceso_de_carga!=0:
        numero=float(input("Ingresa un numero: "))
        if numero>n1:
            mayores_n1+=1
        elif numero<n2:
            menores_n2+=1
        numeros_totales+=1
        proceso_de_carga=float(input("Continuar la Carga (Si=1,No=0) :"))
    porcentaje_mayores_n1=(mayores_n1*100)/numeros_totales
    porcentaje_menores_n2=(menores_n2*100)/numeros_totales
    print("El porcentaje total de mayores a n1 en relacion al total de numeros cargados es de {} y el porcentaje de total de menores a n2 en relacion al total de numeros cargados es de : {}".format(porcentaje_mayores_n1,porcentaje_menores_n2))

cargar_numeros() """
"""
1. Desarrollar un programa de Python que permita cargar por teclado una secuencia de números. El usuario
cargará un 0(cero) para indicar el final del proceso de carga. El cero no debe considerarse un dato a procesar.
El programa debe:
a. Determinar el porcentaje que cantidad de números pares representa en la cantidad total de números
ingresados.
b. Determinar si la secuencia estaba formada sólo por números menores o iguales que 20.
"""
""" def cargar_numeros():
    proceso_de_carga=float(input("Continuar la Carga (Si/1,No/0) :"))
    pares=0
    numeros_menores_20=0
    numeros_totales=0
    while proceso_de_carga!=0:
        numero=float(input("Ingresa un numero: "))
        if numero%2==0:
            pares+=1
        if numero<=20:
            numeros_menores_20+=1
        numeros_totales+=1
        proceso_de_carga=float(input("Continuar la Carga (Si=1,No=0) :"))
    porcentaje_pares=(pares*100)/numeros_totales
    print("El porcentaje total de numeros pares en relacion al total de numeros cargados es de {} ,la cantidad de numeros menores o iguales a 20 fueron : {}".format(porcentaje_pares,numeros_menores_20))

cargar_numeros() """
"""
1. Se solicita realizar un programa que permita ingresar por teclado dos valores a y b, siendo a positivo y b
mayor que a (validarlo). Sumar todos los números múltiplos de a comprendidos en un rango [a, b]."""

""" def ingresar_dos_valores(a,b):
    if a<0 or b<a :
        return print("Uno de los 2 valores no es valido intenta otra vez")
    numeros=0
    for i in range(int(a),int(b)+1):
        print(i)
        if i%a ==0:
            numeros+=i
    print(numeros)

valor1=float(input("Ingresa un valor: "))
valor2=float(input("Ingresa un valor: "))
ingresar_dos_valores(valor1,valor2) """

"""2. Cargar una sucesión de n números enteros y positivos (validar que cada número que se cargue sea mayor a
cero). Mostrar la cantidad de números de la sucesión cargada que son múltiplos del primer número cargado
de la sucesión.
"""
""" def sucesion_rara(n):
    primer_numero=0
    contador_numeros_multiplos=0
    for i in range(n):
        numero=int(input("Ingrese un numero positivo y entero por favor: "))
        if numero<0:
            return print("No es postivo el numero")
        if i==0:
            primer_numero=numero
        if i!=0:
            if numero%primer_numero==0:
                contador_numeros_multiplos+=1
    print(contador_numeros_multiplos)

cuantos_numeros=int(input("Cuantos numeros vas a cargar : "))
sucesion_rara(cuantos_numeros) """
"""
1. Cargar una sucesión de n números enteros y positivos (validar que cada número que se cargue sea mayor a
cero) calcular y mostrar:
a. La cantidad de números pares.
b. El promedio de números pares.
c. El porcentaje de números pares respecto del total de los números de la sucesión.
"""
""" def sucesion_rara(n):
    pares=0
    acumulador_numeros_pares=0
    total_numeros=0
    acumulador_numeros=0
    for i in range(n):
        numero=int(input("Ingrese un numero positivo y entero por favor: "))
        if numero<0:
            return print("No es postivo el numero")
        total_numeros+=1
        acumulador_numeros+=numero
        if numero%2==0:
            pares+=1
            acumulador_numeros_pares+=numero
    porcentaje_numeros_pares=(acumulador_numeros_pares*100)/acumulador_numeros
    promedio_numeros_pares=acumulador_numeros_pares/pares
    print("La cantidad de numeros pares es de : {}, el promedio de numeros pares es de : {}, el porcentaje de numeros pares es de : {}".format(pares,promedio_numeros_pares,porcentaje_numeros_pares))

cuantos_numeros=int(input("Cuantos numeros vas a cargar : "))
sucesion_rara(cuantos_numeros) """