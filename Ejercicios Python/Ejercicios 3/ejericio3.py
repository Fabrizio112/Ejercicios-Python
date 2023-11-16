"""
1. Desarrollar un programa en Python que permita cargar por teclado una sucesión de números. El usuario
deberá cargar un 0(cero) para indicar el final del proceso de carga. El cero no debe considerarse un dato a
procesar. El programa debe:
a. Determinar cuántos de los números ingresados son mayores que n1 y menores que n2 (cargar
previamente por teclado los números n1 y n2).
b. Determinar el porcentaje que el total de números calculado en el punto 1 representa en el total de
números cargados."""
def cargar_numeros():
    num=float(input("Enter a number: "))
    n1=float(input("Enter n1 number: "))
    n2=float(input("Enter n2 number: "))
    numeros_cargados=0
    mayores_a_n1=0
    menores_a_n2=0
    while num !=0:
        numeros_cargados+=1
        if num >n1:
            mayores_a_n1+=1
        elif num<n2:
            menores_a_n2+=1
        num=float(input("Enter a number: "))
    porcentaje_numeros_mayores=(mayores_a_n1*100)/numeros_cargados
    porcentaje_numeros_menores=(menores_a_n2*100)/numeros_cargados
    print(porcentaje_numeros_mayores,porcentaje_numeros_menores)
#cargar_numeros()
"""
1. Desarrollar un programa de Python que permita cargar por teclado una secuencia de números. El usuario
cargará un 0(cero) para indicar el final del proceso de carga. El cero no debe considerarse un dato a procesar.
El programa debe:
a. Determinar el porcentaje que cantidad de números pares representa en la cantidad total de números
ingresados.
b. Determinar si la secuencia estaba formada sólo por números menores o iguales que 20.---> Esto es una pinchila no sirve es irrrelevante
"""
def ingresar_numeros_again():
    num=float(input("Enter a number: "))
    numeros_totales=0
    numeros_pares=0
    while num !=0:
        numeros_totales+=1
        if num%2==0:
            numeros_pares+=1
        num=float(input("Enter a number: "))
    porcentaje_numeros_pares=(numeros_pares*100)/numeros_totales
    print(porcentaje_numeros_pares)
#ingresar_numeros_again()
"""
1. Se solicita realizar un programa que permita ingresar por teclado dos valores a y b, siendo a positivo y b
mayor que a (validarlo). Sumar todos los números múltiplos de a comprendidos en un rango [a, b]."""
def ingresar_2_valores():
    a=int(input("Enter a value: "))
    b=int(input("Enter b value: "))
    acumulador=0
    if not a>0 and not b>a:
        return
    else:
        for i in range (a,b+1):
            if i%a==0:
                acumulador+=i
    print(acumulador)
#ingresar_2_valores()

"""2. Cargar una sucesión de n números enteros y positivos (validar que cada número que se cargue sea mayor a
cero). Mostrar la cantidad de números de la sucesión cargada que son múltiplos del primer número cargado
de la sucesión.
"""
def sucesion_numeros_positivos():
    num=int(input("Enter a number: "))
    primero_cargado=num
    multiplos_del_primero=0
    while num>0:
        if num%primero_cargado==0:
            multiplos_del_primero+=1
        num=int(input("Enter a number: "))
    print(multiplos_del_primero)
#sucesion_numeros_positivos()
"""
1. Cargar una sucesión de n números enteros y positivos (validar que cada número que se cargue sea mayor a
cero) calcular y mostrar:
a. La cantidad de números pares.
b. El promedio de números pares.
c. El porcentaje de números pares respecto del total de los números de la sucesión.
"""
def sucesion_numeros_positivos():
    num=int(input("Enter a number: "))
    cantidad_de_pares=0
    acumulador_de_pares=0
    cantidad_total_numeros=0
    while num>0:
        cantidad_total_numeros+=1
        if num%2==0:
            acumulador_de_pares+=num
            cantidad_de_pares+=1
        num=int(input("Enter a number: "))
    porcentaje_pares=(cantidad_de_pares*100)/cantidad_total_numeros
    promedio_pares=acumulador_de_pares/cantidad_de_pares
    print(porcentaje_pares,"%\n",promedio_pares)
#sucesion_numeros_positivos()