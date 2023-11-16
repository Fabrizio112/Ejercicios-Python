import math
#Ejercicio 1 : Calcular El Area de un Triangulo
#Ingresar por teclado la Base
#Altura=base**2

def area_triangulo():
    base=float(input("Base del triangulo: "))
    altura=base ** 2
    return f"El area de un triangulo es de {(base*altura) /2}"

#print(area_triangulo())

#Ejercicio 2:Calcular el tiempo total que va a tardar un vehiculo
#Distancia 800kms
#Velocidad de 122 km/h
def tiempo_total():
    distancia=800
    velocidad=122
    return f"El tiempo total que va a tardar es de {round(distancia/velocidad)} horas"

#print(tiempo_total())


#Ejercicio 3:Leer dos números y calcular: La suma de sus cuadrados. El promedio de sus cubos.

def operacion_rara():
    num1=float(input("Ingrese un numero: "))
    num2=float(input("Ingrese un numero: "))
    return f"La suma de los cuadrados es de {(num1**2)+(num2**2)}\nPromedio de sus cubos {((num1**3)+(num2**3))/2}"

#print(operacion_rara())
#Ejercicio 4: Determinar Precio al contado y con tarjeta de un articulo. 
#Precio de venta al contado (5% de descuento) Precio de venta con tarjeta (10% de recargo).
def precios():
    venta=float(input("Importe de la venta :"))
    return f"Si paga con  tarjeta le queda el articulo en {venta*1.1}\nSi paga al contado su articulo le queda en {venta*0.95}"

#print(precios())
#Ejercicio 5:Calcular el descuento y el monto a pagar por un medicamento en una farmacia todos los medicamentos 5% de descuento
#mostrar precio actual,descuento ,monto final

def descuento_farmacia():
    precio_actual=float(input("Ingrese el monto del medicamento"))
    descuento_medicamento=precio_actual*0.05
    monto_final=precio_actual-descuento_medicamento
    return f"Precio actual :{precio_actual}\nDescuento : {descuento_medicamento}\nMonto final: {monto_final}"

#print(descuento_farmacia())