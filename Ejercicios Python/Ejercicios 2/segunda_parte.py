"""
Leer una serie de números enteros,
 que contenga como máximo veinte elementos, 
 en caso de ingresar un
valor negativo o la cantidad de números 
ingresados supere los veinte, detener el proceso e 
informar mediante
un mensaje cuántos son mayores que 100."""

def serie_numeros():
    i=1
    mayores_a_cien=0
    num=int(input("Ingrese un numero: "))
    while i<20 and num>0:
        i+=1
        if num >100:
            mayores_a_cien+=1
        num=int(input("Ingrese un numero: "))
    return f"Los numeros mayores a cien son {mayores_a_cien}"

#print(serie_numeros())

"""2. Se dispone de diez pares ordenados (X,Y) de números, 
a los cuales se debe calcular la suma de todas las X y la
suma de todas las Y, imprimir los resultados."""
def pares_suma():
    pares=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16),(17,18),(19,20)]
    x=0
    y=0
    for par in pares:
        x+=par[0]
        y+=par[1]
    return f"Suma de las X {x}\nSuma de las Y {y}"
#print(pares_suma())

"""3. Calcular el total de comisiones que se debe abonar a los
 vendedores por sus ventas realizadas, para ello se
deberá ingresar la categoría del vendedor y el total de la 
venta (el proceso termina cuando se ingrese una
categoría igual a cero), la comisión se calcula con un 
porcentaje del total de venta según la categoría del
vendedor. Hay cuatro categorías de vendedores (1 a 3):
a. Categoría 1: cobra una comisión de 5%
b. Categoría 2: cobra una comisión de 10%
c. Categoría 3: cobra una comisión de 15%"""

def comisiones_totales():
    categoria=int(input("Que categoria tiene (1,2 ó 3): "))
    total_comisiones=0
    while categoria>0 and categoria<=3:
        total_de_venta=float(input("Total de venta : "))
        if categoria == 1:
            total_comisiones+=total_de_venta*0.05
        elif categoria == 2:
            total_comisiones+= total_de_venta*0.10
        else:
            total_comisiones+=total_de_venta*0.15
        categoria=int(input("Que categoria tiene : "))
    return f"Comisiones totales a abonar {total_comisiones}"

#print(comisiones_totales())

"""4. Se dispone de veinte pares ordenados de números;
 se debe leer e imprimir la diferencia de cada par."""
def pares_ordenados():
    pares=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16),(17,18),(19,20),(21,22),(23,24),(25,26),(27,28),(29,30),(31,32),(33,34),(35,36),(37,38),(39,40)]
    for par in pares:
        print(par[0]-par[1])
    
#print(pares_ordenados())
