"""
Hacer un programa que solicite el ingreso de 10 números y que muestre el mayor de ellos por pantalla. Solo se debe emitir UN valor por pantalla.
"""
def mayor_10_numeros():
    mayor=0
    for i in range(10):
        num=float(input("Ingrese un numero"))
        if i==0:
            mayor=num
        elif mayor <num:
            mayor=num
    print(mayor)
#mayor_10_numeros()

"""
2. Hacer un programa que solicite 20 números y calcule y emita por pantalla cuántos son positivos (mayores a cero). 
Se debe mostrar un solo valor: elconteo final
"""
def cuantos_positivos():
    positivos=0
    for i in range(20):
        num=float(input("Ingrese un numero: "))
        if num>0:
            positivos +=1
    print(positivos)
#cuantos_positivos()
"""
3. Hacer un programa para mostrar los números del 1 al 10. No se debe realizar ningún pedido de datos
"""
def mostrar_diez():
    for i in range(10):
        print(i+1)

#mostrar_diez()
"""
4. Hacer un programa para mostrar los números del 10 al 1. No se debe realizar ningún pedido de datos.
"""
def mostar_uno():
    for i in range(10,0,-1):
       print(i)
#mostar_uno()
"""
5. Hacer un programa que muestre los números del 1 al 100 de 5 en 5. Ejemplo: 0,5, 10, 15, 20... 100.
"""
def mostar_cien():
    for i in range(0,105,5):
        print(i)
#mostar_cien()
"""
6. Hacer un programa que solicite UN número y luego calcule y emita un cartel aclaratorio si el mismo es primo o no es primo. Nota: un numero es primo cuando es divisible únicamente por 1 y por si mismo.
"""
def primo_o_no():
    num=int(input("Ingrese un numero: "))
    contador=0
    for i in range(num+1):
        if not i==0 :
            if num % i==0:
                contador+=1
    if contador==2:
        print("Es primo",contador)
    else:
        print("No es primo",contador)

#primo_o_no()


"""
7. Hacer un programa que solicite 10 números y luego mostrar por pantalla el máximo de ellos y la posición en la que fue ingresado.
"""
def maximo_posicion():
    maximo=None
    posicion=None
    for i in range(10):
        num=float(input("Ingrese un numero: "))
        if i==0:
             maximo=0
             posicion=i+1
        else:
            if num >maximo:
                maximo=num
                posicion=i+1
    print(maximo,posicion)
#maximo_posicion()
"""
8. Hacer un programa que solicite 20 números y luego mostrar por pantalla el menor de ellos y la posición en la que fue encontrado.
"""
def minimo_posicion():
    minimo=None
    posicion=None
    for i in range(10):
        num=float(input("Ingrese un numero: "))
        if i==0:
             minimo=num
             posicion=i+1
        else:
            if num <minimo:
                minimo=num
                posicion=i+1
    print(minimo,posicion)
#minimo_posicion()
"""
9. Hacer un programa que solicite 20 edades y luego calcule el promedio de edad de aquellas personas mayores a 18 años.
"""
def ingresar_edades():
    acumulador=None
    contador=0
    for i in range(20):
        edad=int(input("Enter your age : "))
        if edad>18:
            acumulador += edad
            contador+=1
    return print("Promedio de edades: ",acumulador/contador)
#ingresar_edades()

    
"""
10. Hacer un programa que solicite 20 números y luego emitir por pantalla el máximo de los números pares y el minimo de los números impares. 
"""
def maximo_minimos_pares_impares():
    bMp=0
    bmp=0
    maximo_pares=None
    minimo_impares=None
    for i in range(20):
        num=int(input("Enter any number : "))
        if num%2==0:
            if bMp==0:
                bMp=1
                maximo_pares=num
            else:
                if num >maximo_pares:
                    maximo_pares=num
        else:
            if bmp==0:
                bmp=1
                minimo_impares=num
            else:
                if num<minimo_impares:
                    minimo_impares=num
    print(maximo_pares,minimo_impares)

#maximo_minimos_pares_impares()
"""
11. Hacer un programa para ingresar 10 números y luego calcule y emita el mayor
de los primos de la lista. En caso de no haber ningún número primo, deberá aclararlo con un cartel.
"""
def maximo_primos():
    bp=0
    maximo_primo=None
    for i in range(10):
        num=int(input("Enter any number : "))
        contador=0
        for k in range(num+1):
            if not k==0:
                if num % k==0:
                    contador +=1
        if contador==2:
            if bp ==0:
                maximo_primo=num
                bp=1
            else:
                if maximo_primo<num:
                    maximo_primo=num
    print("El maximo primo es ",maximo_primo)

#maximo_primos()