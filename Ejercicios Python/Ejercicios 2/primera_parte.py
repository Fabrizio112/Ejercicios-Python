"""Se necesita desarrollar un programa que permita calcular la suma de tres números. 
Si el resultado es mayor a 50 dividir
por 2, en caso contrario elevar el resultado al cubo."""

def suma_tres_numeros():
    num1=float(input("Ingrese un numero : "))
    num2=float(input("Ingrese un numero : "))
    num3=float(input("Ingrese un numero : "))
    resultado_suma=num1 + num2 + num3
    if resultado_suma > 50:
        resultado_suma= resultado_suma/2
        return resultado_suma
    else:
        return resultado_suma **3
#print(suma_tres_numeros())



"""2. Se solicita realizar un programa que permita ingresar
 tres temperaturas correspondientes a diferentes momentos de un
día y determinar cuál es el promedio de las temperaturas 
y si existe alguna temperatura que sea mayor al promedio."""

def temperaturas():
    temp1=float(input("Ingrese una temperatura : "))
    temp2=float(input("Ingrese una temperatura : "))
    temp3=float(input("Ingrese una temperatura : "))
    promedio_temperaturas= temp1+temp2+temp3 /3
    if temp1>promedio_temperaturas or temp2>promedio_temperaturas or temp3>promedio_temperaturas:
        return f"El promedio de temperaturas es {promedio_temperaturas},hay una temperatura mayor al promedio "
    else:
        return f"El promedio de temperaturas es :{promedio_temperaturas} y no hay ninguna temperatura mayor al promedio"
    

#print(temperaturas())

"""3. Ingresar por teclado las edades de 3 postulantes
 para un trabajo. 
Informar si todos cumplen con la edad mínima
establecida para el mismo, también ingresada por teclado."""
def edad_trabajo():
    edad_minima=18
    edad1=float(input("Ingrese una edad : "))
    edad2=float(input("Ingrese una edad : "))
    edad3=float(input("Ingrese una edad : "))
    if edad1 >= edad_minima and edad2 >=edad_minima and edad3 >=edad_minima:
        return "Todos cumplen la edad minima"
    else: 
        return "No todos cumplen la edad minima"

#print(edad_trabajo())

"""4. Realizar un programa que tome tres números, y los muestre ordenados de mayor a menor."""
def mayor_menor():
    numeros=[]
    for i in range(0,3):
        num=float(input("Ingrese un numero: "))
        numeros.append(num)
    numeros.sort(reverse=True)
    return numeros

#print(mayor_menor())

"""5. Un comercio necesita informar el importe final a 
pagar a un determinado proveedor. 
Para ello debe ingresar la categoría (que puede ser categoría ’A’ o ’B’) 
y el importe original a abonar. Considerar las siguientes condiciones para el
cálculo del importe final a pagar: 
Si el cliente es categoría A y el monto a pagar supera a
 los 10000 pesos debe aplicarse un descuento del 5 %.
Si el cliente es categoría B y el importe a pagar oscila 
entre 15000 y 25000 pesos debe aplicarse
un descuento del 2 %. 
Para ambas categorías en caso de no cumplirse las 
condiciones especificadas no se aplicará
ningún tipo de descuento sobre el importe que se le debe abonar."""

def proveedor_negocio():
    categoria=(input("Que categoria es usted (A ó B): ")).upper()
    importe_total=float(input("Ingrese el importe total: "))
    if categoria == "A":
        if importe_total > 10000:
            importe_total= importe_total*0.95
        return importe_total
    elif categoria =="B":
        if importe_total >= 15000 and importe_total <= 25000:
            importe_total=importe_total*0.98
        return importe_total
    else:
        return "Mal ingresada la categoria"


#print(proveedor_negocio())

#6. Leer una serie de cincuenta números enteros. Informar cuántos son mayores que 100.

def cincuenta_numeros():
    numeros=[]
    mayores_cien=0
    for i in range(50):
        num=float(input("Ingrese un numero :"))
        numeros.append(num)
    
    for num in numeros :
        if num > 100:
            mayores_cien+=1
    return f"Los numeros mayores a 100 son {mayores_cien}"

#print(cincuenta_numeros())