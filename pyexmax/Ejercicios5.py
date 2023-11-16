"""
Hacer un programa para mostrar los números del 1 al 10. No se debe realizar ningún pedido de datos. USANDO WHILE.
"""
def num_to_ten():
    i=0
    while i<10:
        i+=1
        print(i)
#num_to_ten()
"""
2. Hacer un programa para mostrar los números del 10 al 1. No se debe realizar ningún pedido de datos. USANDO WHILE.
"""
def num_to_one():
    i=10
    while i>0:
        print(i)
        i-=1
#num_to_one()
"""
3. Hacer un programa que solicite la edad de un grupo de personas. 
El programa deberá pedir edades hasta que se ingrese una edad menor a 18 años. 
Deberá mostrar por pantalla cuántas personas mayores se registraron.
"""
def edad_mayor_18():
    mayores=0
    edad=int(input("Enter a age : "))
    while edad>18:
        mayores+=1
        edad=int(input("Enter a age : "))
    print(mayores)
#edad_mayor_18()
"""
4. Hacer un programa que solicite dos números y luego questre los números entre el menor y
 el mayor de ellos. Acordate, usando hile.
"""
def intervalo():
    num1=int(input("Enter a number: "))
    num2=int(input("Enter a number: "))
    mayor=None
    menor=None
    if num1>num2:
        mayor=num1
        menor=num2
    else :
        mayor=num2
        menor=num1
    while menor<mayor:
        print(menor)
        menor+=1
#intervalo()
"""
5. Hacer un programa que muestre los números del 1 al 100 de 5 en 5. Ejemplo: 0,5, 10, 15, 20 100. Usando While.
"""
def mostrar_numero_100():
    i=0
    while i<101:
        print(i)
        i+=5
#mostrar_numero_100()

"""
6. Hacer un programa que solicite UN número y luego calcule y emita un cartel aclaratorio 
si el mismo es primo o no es primo. Nota: usando While. Ya lo hicimos con FOR, ahora con While.
"""
def numero_primo():
    num=int(input("Enter a number: "))
    i=1
    contador=0
    while i <num+1:
        if num%i ==0:
            contador +=1
        i+=1
    if contador==2:
        print("Es primo")
    else:
        print("No es primo")
#numero_primo()
"""
7. Hacer un programa que solicite una lista de números que corta cuando se ingresa un cero
 y luego mostrar por pantalla el máximo de ellos y la posición en la que fue ingresado.
"""
def lista_maximo_numero_posicion():
    num=int(input("Enter a  number: "))
    maximo=0
    posicion=1
    while num !=0:
        if posicion==1:
         maximo=num
         posicionMaximo=posicion
        else :
            if num>maximo:
                maximo=num
                posicionMaximo=posicion
        posicion+=1
        num=int(input("Enter a  number: "))
    print(maximo,posicionMaximo)
#lista_maximo_numero_posicion()
"""
8. Hacer un programa que solicite una lista de números que corta cuando se ingresa un cero y 
luego mostrar por pantalla el menor y el segundo menor.
"""
def lista_menor_2do_menor():
    num=int(input("Enter a  number: "))
    menor=None
    segundoMenor=None
    posicion=1
    posicionMenor=None
    posicionSegundoMenor=None
    while num !=0:
        if posicion==1:
         menor=num
         posicionMenor=posicion
        else :
            if posicion==2:
                if num<menor:
                    segundoMenor=menor
                    posicionSegundoMenor=posicion
                    menor=num
                    posicionMenor=posicion
                else:
                    segundoMenor=num
                    posicionSegundoMenor=posicion
            else:
                 if num<menor:
                    segundoMenor=menor
                    posicionSegundoMenor=posicion
                    menor=num
                    posicionMenor=posicion
                 elif segundoMenor>num:
                    segundoMenor=num
                    posicionSegundoMenor=posicion
        posicion+=1
        num=int(input("Enter a  number: "))
    print(menor,posicionMenor,segundoMenor,posicionSegundoMenor)
#lista_menor_2do_menor()
"""
9. Realizar el nuevamente el ejercicio 8 pero ahora debe devolver además
 la posición en la que fue encontrado cada uno de los minimos.
"""

"""
10. Hacer un programa que solicite una lista de números que corta cuando se ingresa un cero y 
luego emitir por pantalla el máximo de los números negativos y el minimo de los números positivos.
"""
def numero_negativos_positivos():
    maximo_negativo=None
    bn=0
    bp=0
    minimo_positivos=None
    num=float(input("Enter a  number: "))
    while num !=0:
        if num >0:
            if bp==0:
                bp=1
                minimo_positivos=num
            else:
                if minimo_positivos>num:
                    minimo_positivos=num
        else:
            if bn==0:
                bn=1
                maximo_negativo=num
            else:
                if maximo_negativo<num:
                    maximo_negativo=num
        num=float(input("Enter a  number: "))
    print(maximo_negativo,minimo_positivos)
#numero_negativos_positivos()
"""
11. Hacer un programa para ingresar una lista de números que corta cuando se Ingresa un cero 
y luego mostrar: la cantidad de números primos, la cantidad de números pares, la cantidad de
 positivos y la cantidad de negativos.
"""
def numeros_negativos_positivos_primos():
     num=int(input("Enter a  number: "))
     cantidad_postivos=0
     cantidad_negativos=0
     cantidad_pares=0
     cantidad_primos=0
     while num !=0:
        contador=0
        if num>0:
            cantidad_postivos+=1
        else:
            cantidad_negativos+=1
        if num%2==0:
            cantidad_pares+=1
        for i in range(num+1):
            if not i==0:
                if num%i==0:
                    contador+=1
        if contador==2:
            cantidad_primos+=1
        num=int(input("Enter a  number: "))
     print(cantidad_pares,cantidad_negativos,cantidad_postivos,cantidad_primos)
#numeros_negativos_positivos_primos()