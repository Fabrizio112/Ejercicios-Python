"""
Se quiere calcular e imprimir el cuadrado de cada número 
de una serie de n elementos, los que se leen de a
uno por vez."""
def cuadrado_numeros():
    cantidad=int(input("Cuantos numeros vas a ingresar: "))
    for i in range(cantidad):
        numero=int(input("Ingrese un numero: "))
        print(numero**2)

#cuadrado_numeros()

"""2. Ingresar n números enteros y calcular el promedio
 de los números ingresados y el porcentaje de números
mayores a 100 respecto del total."""

def promedio_numeros_ingresados():
    cantidad=int(input("Cuantos numeros vas a ingresar: "))
    acumulador=0
    cantidad_mayores_cien=0
    for i in range (cantidad):
        numero=int(input("Ingrese un numero: "))
        acumulador+=numero
        if numero>100:
            cantidad_mayores_cien+=1
    print(f"Promedio de numeros ingresados {acumulador/cantidad}\nPorcentaje de numeros mayores a cien es:{(cantidad_mayores_cien*100)/cantidad}%")

#promedio_numeros_ingresados()

"""3. Se ingresan los datos de las ventas de un comercio, 
código del producto, cantidad vendida y precio unitario, se
pide informar:
a. La cantidad de ventas ingresadas.
b. El importe total de ventas.
c. La cantidad de ventas cuyo valor esté comprendido entre 100 
y 300 unidades.
d. Indicar si hubo una cantidad de ventas inferior a 
50 unidades."""

def ventas_comercio():
    ventas=int(input("Cuantas ventas vas a ingresar: "))
    importe_total=0
    cantidad_ventas_entre=0
    cantidad_ventas_menores=0
    for i in range(ventas):
        cantidad_productos_vendidos=int(input("Cuantos productos se vendio: "))
        importe_total_ventas=float(input("Ingrese el importe total de ventas: "))
        importe_total+=importe_total_ventas
        if cantidad_productos_vendidos>=100 and cantidad_productos_vendidos<=300:
            cantidad_ventas_entre+=1
        elif cantidad_productos_vendidos<50:
            cantidad_ventas_menores+=1
    return f"La cantidad total de ventas fueron de {ventas}\nEl importe total de ventas es : {importe_total}\nLa cantidad total de ventas entre 100 y 300 es de {cantidad_ventas_entre}\nLa cantidad total de ventas menores de 50 es de {cantidad_ventas_menores}"

#print(ventas_comercio())

"""4. Desarrollar un programa que permita ingresar 
las coordenadas de n puntos en el plano, e informe: En qué
cuadrante se encuentra cada uno. Determinar cuántos 
puntos se encuentran en el primer o tercer cuadrante"""

def cuadrantes():
    puntos=int(input("Cuantos puntos vas a ingresar: "))
    cantidad_puntos_primer_cuadrante=0
    cantidad_puntos_tercer_cuadrante=0
    for i in range(puntos):
        x=float(input("Coordenadas X: "))
        y=float(input("Coordenadas Y: "))
        if x>0 and y>0:
            cantidad_puntos_primer_cuadrante+=1
        elif x<0 and y<0:
            cantidad_puntos_tercer_cuadrante+=1
    return f"Cantidad de puntos en el primer cuadrante : {cantidad_puntos_primer_cuadrante}\nCantidad de puntos en el tercer cuadrante : {cantidad_puntos_tercer_cuadrante}"

#print(cuadrantes())
