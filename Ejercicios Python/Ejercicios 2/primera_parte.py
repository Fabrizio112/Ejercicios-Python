"""Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 50 dividir
por 2, en caso contrario elevar el resultado al cubo."""
n1=float(input("Ingrese el valor del primer numero: "))
n2=float(input("Ingrese el valor del segundo numero: "))
n3=float(input("Ingrese el valor del tercer numero: "))
suma_de_numeros=n1+n2+n3
if suma_de_numeros>50:
    suma_de_numeros=suma_de_numeros/2
else:
    suma_de_numeros=suma_de_numeros**3

print("El resultado es ",suma_de_numeros) 

"""2. Se solicita realizar un programa que permita ingresar tres temperaturas correspondientes a diferentes momentos de un
día y determinar cuál es el promedio de las temperaturas y si existe alguna temperatura que sea mayor al promedio."""
temperatura1=float(input("Ingrese la temperatura: "))
temperatura2=float(input("Ingrese la temperatura: "))
temperatura3=float(input("Ingrese la temperatura: "))
promedio_de_temperaturas=(temperatura1+temperatura2+temperatura3)/3
print(promedio_de_temperaturas)
if promedio_de_temperaturas<temperatura1 or promedio_de_temperaturas<temperatura2 or promedio_de_temperaturas<temperatura3:
    print("Hay por lo menos una temperatura que es mayor al promedio")


"""3. Ingresar por teclado las edades de 3 postulantes para un trabajo. Informar si todos cumplen con la edad mínima
establecida para el mismo, también ingresada por teclado."""
edad1=int(input("Cual es su edad: "))
edad2=int(input("Cual es su edad: "))
edad3=int(input("Cual es su edad: "))
edad_minima_para_el_trabajo=18
if edad_minima_para_el_trabajo <= edad1 and edad_minima_para_el_trabajo <=edad2 and edad_minima_para_el_trabajo <=edad3 :
    print("Todos cumplen con la minima edad para el trabajo")
else:
     print("No todos cumplen con la minima edad para el trabajo")

"""4. Realizar un programa que tome tres números, y los muestre ordenados de mayor a menor."""
n1=float(input("Ingrese un numero ")) 
n2=float(input("Ingrese un numero ")) 
n3=float(input("Ingrese un numero ")) 
mayor=[]
if n1>n2 and n1>n3:
    mayor.append(n1)
    if n2>n3 :
        mayor.append(n2)
        mayor.append(n3)
        print(mayor)
    else:
        mayor.append(n3)
        mayor.append(n2)      
        print(mayor)
elif n2>n3:
    mayor.append(n2)
    if n1>n3:
        mayor.append(n1)
        mayor.append(n3)
        print(mayor)
    else:
        mayor.append(n3)
        mayor.append(n1)
        print(mayor)
else:
    mayor.append(n3)
    if n2>n1:
        mayor.append(n2)
        mayor.append(n1)
        print(mayor)
    else:
        mayor.append(n1)
        mayor.append(n2)
        print(mayor)
"""5. Un comercio necesita informar el importe final a pagar a un determinado proveedor. Para ello debe ingresar la
categoría (que puede ser categoría ’A’ o ’B’) y el importe original a abonar. Considerar las siguientes condiciones para el
cálculo del importe final a pagar: Si el cliente es categoría A y el monto a pagar supera a los 10000 pesos debe aplicarse
un descuento del 5 %. Si el cliente es categoría B y el importe a pagar oscila entre 15000 y 25000 pesos debe aplicarse
un descuento del 2 %. Para ambas categorías en caso de no cumplirse las condiciones especificadas no se aplicará
ningún tipo de descuento sobre el importe que se le debe abonar."""
importe_pagar=float(input("Ingrese el importe a pagar a los proveedores: "))
categoria_del_cliente=str(input("Ingrese la categoria del proveedor(A ó B):").upper())

if categoria_del_cliente =="B":
    if importe_pagar>15000 and importe_pagar<25000:
        importe_final_a_pagar=importe_pagar*0.98
    else:
        importe_final_a_pagar=importe_pagar
elif categoria_del_cliente =="A":
    if importe_pagar > 10000 :
        importe_final_a_pagar=importe_pagar*0.95
    else:
        importe_final_a_pagar=importe_pagar
else:
    print("Por favor ingrese una categoria que sea valida")

print("Usted debe pagar",importe_final_a_pagar)


#6. Leer una serie de cincuenta números enteros. Informar cuántos son mayores que 100.
contador_numeros_mayores_cien=0
for i in range(50):
    num=float(input("Ingrese un numero"))
    if num>100:
        contador_numeros_mayores_cien +=1

print("Los numeros mayores a 100 fueron : ",contador_numeros_mayores_cien)