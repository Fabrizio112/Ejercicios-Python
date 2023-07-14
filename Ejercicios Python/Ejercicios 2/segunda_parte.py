"""
Leer una serie de números enteros, que contenga como máximo veinte elementos, en caso de ingresar un
valor negativo o la cantidad de números ingresados supere los veinte, detener el proceso e informar mediante
un mensaje cuántos son mayores que 100."""
""" contador=0

for i in range(20):
    n=float(input("Ingresa un numero :"))
    if n<0:
        break
    else:
        if n<100:
            contador+=1
print(contador)
 """


"""2. Se dispone de diez pares ordenados (X,Y) de números, a los cuales se debe calcular la suma de todas las X y la
suma de todas las Y, imprimir los resultados."""
""" x=[1,2,3,4,5,6,7,8,9,10]
y=[1,2,3,4,5,6,7,8,9,10]
acumulador_x=0
acumulador_y=0

for i in range(10):
    acumulador_x+=x[i]
    acumulador_y+=y[i]

print(acumulador_y,acumulador_x)
 """
"""3. Calcular el total de comisiones que se debe abonar a los vendedores por sus ventas realizadas, para ello se
deberá ingresar la categoría del vendedor y el total de la venta (el proceso termina cuando se ingrese una
categoría igual a cero), la comisión se calcula con un porcentaje del total de venta según la categoría del
vendedor. Hay cuatro categorías de vendedores (1 a 3):
a. Categoría 1: cobra una comisión de 5%
b. Categoría 2: cobra una comisión de 10%
c. Categoría 3: cobra una comisión de 15%"""

""" categoria_del_vendedor=int(input("Ingrese la categoria del vendedor  "))

comisiones_totales=0
while categoria_del_vendedor!=0:
    total_de_la_venta=float(input("Ingrese el total de venta : "))
    if categoria_del_vendedor==1:
        comisiones_totales+=total_de_la_venta*0.05
        categoria_del_vendedor=int(input("Ingrese la categoria del vendedor  "))
    elif categoria_del_vendedor ==2:
        comisiones_totales+=total_de_la_venta*0.1
        categoria_del_vendedor=int(input("Ingrese la categoria del vendedor  "))
    else:
        comisiones_totales+=total_de_la_venta*0.15
        categoria_del_vendedor=int(input("Ingrese la categoria del vendedor  "))

print(comisiones_totales) """

"""4. Se dispone de veinte pares ordenados de números; se debe leer e imprimir la diferencia de cada par."""
""" pares=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16),(17,18),(19,20),(21,22),(23,24),(25,26),(27,28),(29,30),(31,32),(33,34),(35,36),(37,38),(39,40)]

for par in pares:
   diferencia=par[0]-par[1]
   print("La diferencia entre", par[0], "y", par[1], "es:", diferencia) """