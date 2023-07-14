"""
Se quiere calcular e imprimir el cuadrado de cada número de una serie de n elementos, los que se leen de a
uno por vez."""
""" lista=[]
cantidad_numeros=int(input("Ingresa la cantidad de numeros que vas a ingresar a continuacion en tu lista : "))
for i in range(cantidad_numeros):
    numero=float(input("Ingresa un numero : "))
    lista.append(numero**2)
for i in range(len(lista)):
    print(lista[i]) """

"""2. Ingresar n números enteros y calcular el promedio de los números ingresados y el porcentaje de números
mayores a 100 respecto del total."""
""" numeros_a_ingresar=int(input("Ingresa la cantidad de numeros que vas a ingresar a continuacion : "))
mayores_cien=0
cantidad_total =0
for i in range(numeros_a_ingresar):
    numero=float(input("Ingresa un numero : "))
    cantidad_total+=numero
    if numero>100:
        mayores_cien+=1
print("El promedio de los numeros es_ ",cantidad_total/numeros_a_ingresar,"y los mayores a 100 fueron : ",mayores_cien)
 """
"""3. Se ingresan los datos de las ventas de un comercio, código del producto, cantidad vendida y precio unitario, se
pide informar:
a. La cantidad de ventas ingresadas.
b. El importe total de ventas.
c. La cantidad de ventas cuyo valor esté comprendido entre 100 y 300 unidades.
d. Indicar si hubo una cantidad de ventas inferior a 50 unidades."""

""" ventas_ingresadas=0;
importe_total_ventas=0
cantidad_ventas_entre_300_100=0
cantidad_ventas_inferior_50=0
codigo_de_producto=int(input("Ingrese el codigo de producto por favor :"))

while codigo_de_producto !=0:
    ventas_ingresadas+=1
    cantidad_vendida=int(input("Ingrese cantidad vendida : "))
    precio_unitario_articulo=float(input("Ingrese el precio unitario del articulo : "))
    importe_de_venta=cantidad_vendida*precio_unitario_articulo
    if cantidad_vendida>=100 and cantidad_vendida<=300:
        cantidad_ventas_entre_300_100+=1
    elif cantidad_vendida<50:
        cantidad_ventas_inferior_50+=1
    importe_total_ventas+=importe_de_venta
    codigo_de_producto=int(input("Ingrese el codigo de producto por favor :"))

print("La cantidad de ventas ingresadas fue de : {}, El importe total de las ventas fue de : {} ,la cantidad de ventas comprendidas entre 300 y 100 fue de : {}, y la cantidad de ventas inferiores a 50 fue de : {},".format(ventas_ingresadas,importe_total_ventas,cantidad_ventas_entre_300_100,cantidad_ventas_inferior_50) )

 """
"""4. Desarrollar un programa que permita ingresar las coordenadas de n puntos en el plano, e informe: En qué
cuadrante se encuentra cada uno. Determinar cuántos puntos se encuentran en el primer o tercer cuadrante"""
""" a=float(input("Ingrese la primera coordenada: "))
b=float(input("Ingrese la primera coordenada: "))
coordenadas=(a,b)
if coordenadas[0]>0 and coordenadas[1]>0:
    print("Estas en el primer Cuadrante")
elif coordenadas[0]<0 and coordenadas[1]>0:
     print("Estas en el Segundo Cuadrante")
elif coordenadas[0]<0 and coordenadas[1]<0:
     print("Estas en el Tercer Cuadrante")
else:
    print("Estas en el Cuarto Cuadrante") """