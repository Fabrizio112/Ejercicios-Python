"""
Generalmente es la suma, pero ya la hicimos en el video!
"""
def suma(a,b):
    return a + b

#print(suma(2,3))

"""
 2. Hacer un programa para solicitar por teclado un número y luego devolver su valor elevado al cubo.
Nota: no olvides que sólo contamos con las cuatro operaciones básicas.
"""
def numero_elevado_al_cubo():
    numero=int(input("Ingresa un numero por favor : "))
    return numero**3
#print(numero_elevado_al_cubo())


"""
 3. Hacer un programa que permita ingresar el año actual y el año de la fecha de nacimiento de una persona y luego calcule y emita por pantalla su edad.
Nota: no hay que tener en cuenta si la persona cumplió años o no,simplemente calcular.
"""
def edad_persona(): 
    año_nacimiento=int(input("Ingrese su año de nacimiento : "))
    año_actual=int(input("Ingrese el año actual : "))
    return año_actual - año_nacimiento

#print(edad_persona())
"""
4. Hacer un programa que permita ingresar los kilómetros existentes entre dos ciudades y la velocidad promedio de un vehículo. Calcular y emitir por pantalla
el tiempo aproximado que demandará llegar de un punto a otro teniendo en cuenta los datos ingresados. 
"""
def tiempo_aproximado_entre_dos_ciudades():
    km_restantes=float(input("Ingrese los km restantes: "))
    velocidad_promedio=float(input("Ingrese la velocidad promedio: "))
    return f"El tiempo que llevara recorrer {km_restantes} a {velocidad_promedio}km/h es de : {km_restantes / velocidad_promedio} horas"

#print(tiempo_aproximado_entre_dos_ciudades())


"""
5. Una casa de computación paga a sus empleados un sueldo fijo de ARS15000 más una comisión del 5% sobre el total facturado 
por cada empleado. Hacer un programa para ingresar el total facturado por un empleado 
y que luego calcule y emita por pantalla el sueldo total a cobrar por el mismo. 
"""
def total_a_cobrar():
    sueldo_fijo=15000
    total_facturado=float(input("Cuanto fue el total que facturaste este mes: "))
    comision=total_facturado*0.05
    return f"El empleado va  a cobrar {sueldo_fijo + comision}"

#print(total_a_cobrar())
"""
6. Hacer un programa para ingresar por teclado las tres notas de exámenes de un alumno y 
luego calcule y emita por pantalla el promedio final.
"""

def promedio_final():
    nota1=float(input("Ingrese su nota : "))
    nota2=float(input("Ingrese su nota : "))
    nota3=float(input("Ingrese su nota : "))
    return f"Su promedio final es de {(nota1 + nota2 + nota3) / 3}"

#print(promedio_final())
"""
7. Hacer un programa para ingresar por teclado los metros cuadrados totales de un predio y los metros cuadrados 
cubiertos; luego calcular y mostrar por pantalla el porcentaje de metros cuadrados cubiertos
 y el porcentaje de metros cuadrados descubiertos.
"""
def m2_cubiertos():
    m2_totales=float(input("Ingrese los m2 totales del predio: "))
    m2_cubiertos=float(input("Ingresa los m2 cubiertos: "))
    porcentaje_m2cubiertos = (m2_cubiertos*100) / m2_totales
    porcentaje_m2nocubiertos=100-porcentaje_m2cubiertos
    return f"El porcentaje de metros cuadrados cubiertos es {porcentaje_m2cubiertos}%\nMetros cuadrados descubiertos {porcentaje_m2nocubiertos}%"

#print(m2_cubiertos())

"""
8. Una importante cadena de delivery cuenta con una promoción por tiempo limitado 
en la que otorga un 15% de descuento sobre el total del valor de la compra realizada.
 Hacer un programa para solicitar el monto total y el mismo calcule y emita por pantalla el total 
 a cobrar con el descuento aplicado.
"""
def monto_a_pagar_delivey():
    monto_total=float(input("Ingrese el monto toal por la compra : "))
    return f"El monto total a pagar por su compra es de {monto_total - (monto_total*0.15)}"

#print(monto_a_pagar_delivey())

"""
9. Una universidad desea conocer los porcentajes de mujeres y hombres en las carreras de ciencias exactas.
 Se solicita un programa para cargar la cantidad de mujeres y la cantidad de hombres y que el mismo calcule y
   emita por pantalla los porcentajes correspondientes:
"""
def universidad_porcentajes():
    cantidad_hombres=int(input("Cantidad de hombres : "))
    cantidad_mujeres=int(input("Cantidad de mujeres : "))
    porcentaje_hombres=cantidad_hombres*100 /(cantidad_hombres+cantidad_mujeres)
    porcentaje_mujeres=cantidad_mujeres*100/(cantidad_mujeres+cantidad_hombres)
    return f"El porcentaje de hombres es de {porcentaje_hombres}% y el porcentaje de mujeres es de {porcentaje_mujeres}%"

#print(universidad_porcentajes())


"""
10. Hacer un programa que permita ingresar por teclado dos números y que luego muestre por pantalla la suma, 
la resta, la multiplicación y la división de dichos números. Se deben mostrar cuatro resultados en pantalla.
 Los números deben ser solicitados una única vez.
"""

def cuatro_operaciones():
    num1=float(input("Ingrese un numero: "))
    num2=float(input("Ingrese un numero: "))
    return f"Operaciones:\nSuma: {num1+num2}\nResta: {num1-num2}\nMultiplicacion: {num1*num2}\nDivision: {num1/num2}"

#print(cuatro_operaciones())
