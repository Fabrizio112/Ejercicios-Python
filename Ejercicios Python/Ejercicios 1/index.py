
#Ejercicio 1 : Calcular El Area de un Triangulo
#Ingresar por teclado la Base
#Altura=base**2
base_del_triangulo=float(input("Ingrese por favor la base del triangulo: "))
altura_del_triangulo=base_del_triangulo**2
area_del_triangulo=(base_del_triangulo*altura_del_triangulo)/2
print("El area del triangulo es de " ,area_del_triangulo ,"cm")

#Ejercicio 2:Calcular el tiempo total que va a tardar un vehiculo
#Distancia 800kms
#Velocidad de 122 km/h
distancia_entre_ciudades=800;
velocidad_promedio=122
tiempo_total= round(distancia_entre_ciudades/velocidad_promedio)
print("El tiempo total que va a tardar el vehiculo en llegar a Buenos Aires es de :",tiempo_total, "horas")

#Ejercicio 3:Leer dos números y calcular: La suma de sus cuadrados. El promedio de sus cubos.
n1=float(input("Ingrese un numero: "))
n2=float(input("Ingrese un numero: "))
suma_de_cuadrados=(n1**2)+(n2**2)
promedio_de_cubos=((n1**3)+(n2**3))/2
print("La suma de sus cuadrados es de ",suma_de_cuadrados, " y el promedio de sus cubos es de ", promedio_de_cubos)

#Ejercicio 4: Determinar Precio al contado y con tarjeta de un articulo. 
#Precio de venta al contado (5% de descuento) Precio de venta con tarjeta (10% de recargo).
articulo=float(input("Ingrese el importe del articulo: "))
precio_de_contado= int(articulo*0.95)
precio_con_tarjeta=int(articulo*1.10)
print("El articulo vale ",articulo, ".Pagando de contado te sale : ", precio_de_contado, "y pagando con tarjeta te sale :",precio_con_tarjeta) 

#Ejercicio 5:Calcular el descuento y el monto a pagar por un medicamento en una farmacia
medicamento=float(input("Cuanto sale el medicamento: "))
precio_medicamento_descuento=int(medicamento*0.95)
descuento_del_medicamento=int(medicamento*0.05)
print("El medicamento sale ",medicamento,"Con descuento te sale ",precio_medicamento_descuento,"El descuento es de :",descuento_del_medicamento)
