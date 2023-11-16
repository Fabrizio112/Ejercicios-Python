"""
Hacer un programa que solicite el ingreso de un número y que luego emita un cartel por pantalla aclarando si el mismo es múltiplo de 5.
"""
def is_multiple_of_five():
    num1=float(input("Enter a number: "))
    if num1%5==0:
        print("Is multiple of five")
    else:
        print("Isn´t multiple of five")
#is_multiple_of_five()

"""
2. Hacer un programa que solicite el ingreso de dos números y luego calcular: 
a. La resta si el primero es mayor que el segundo..
b. La suma si son iguales.
c. El producto si el primero es menor.
Se deberá emitir un cartel por pantalla con el resultado correspondiente.
"""
def weird_function():
    num1=float(input("Enter a number: "))
    num2=float(input("Enter a number: "))
    if num1>num2:
        return print(num1-num2," substraction result")
    elif num1==num2:
        return print(num1+num2," adition result")
    else:
        return print(num1*num2," multiply result")
#weird_function()

"""
3. Hacer un programa para ingresar dos números. Si el segundo es distinto de cero, calcular la división del primero por el segundo y 
mostrar el resultado por pantalla; caso contrario, emitir un cartel aclarando que no se puede dividir por cero.
"""
def weird_function_two():
    num1=float(input("Enter a number: "))
    num2=float(input("Enter a number: "))
    if num2!=0:
         print(num1/num2," division result")
    else:
        print("Can´t divide by cero")
#weird_function_two()
"""
4. Un importante negocio de desinfectante líquido realiza descuentos dependiendo de la cantidad de litros vendidos según la siguiente escala:
a. Si vende menos de 100 litros, no hay descuento. 
b. Si vende entre 101 y 300 litros, el descuento es del 10%.
c. Si vende entre 301 y 500 litros, el descuento es del 15% 
d. Finalmente, si la venta es de más de 500 litros, el descuento es del 25%.
Hacer un programa que solicite el ingreso del importe total de la venta y la cantidad de litros vendidos y calcule y emita el importe con el descuento aplicado.
"""
def discount_liters():
    cuantity_liters=float(input("Enter the cuantity of liters : "))
    total=float(input("Enter the total to pay : "))
    if cuantity_liters>500:
        total_to_pay=total*0.75
    elif cuantity_liters<=500 and cuantity_liters>300:
        total_to_pay=total*0.85
    elif cuantity_liters<=300 and cuantity_liters>100:
        total_to_pay=total*0.90
    else:
        total_to_pay=total
    print(total_to_pay)
#discount_liters()
"""
5. Hacer un programa que solicite el ingreso de las notas del primer parcial y del segundo parcial de una alumna de programación. El programa deberá analizar
las notas y emitir la situación de la alumna según la siguiente escala: 
a. Si tiene 8 o más en ambos parciales, emitir "aprobación directa".
b. Si no tiene 8 o más en ambos pero tiene aprobados ambos parciales (se aprueba con 6 o más), emitir "rinde examen final".
c. Si tiene menos de 6 en alguno de los dos parciales, emitir "debe recuperar
El programa debe emitir solo un cartel, el que corresponda. 
"""
def calculate_notes():
    nota1=float(input("Enter the note of your first parcial: "))
    nota2=float(input("Enter the note of your second parcial: "))
    if nota1<6 or nota2<6:
        print("Should recover")
    elif nota1>=8 and nota2>=8:
        print("Direct approval")
    else:
         print("Should take final exam")
#calculate_notes()
"""
6. Hacer un programa para ingresar por teclado la longitud de los tres lados de un triángulo y que luego determine e informe con un cartel aclaratorio a qué tipo de triángulo corresponde: 
a. Equilátero: cuando los tres lados sean iguales.
b. Isosceles: cuando dos de los tres lados sean iguales.
c. Escaleno: cuando todos los lados sean distintos
"""
def sides_of_triangle():
     side1=float(input("First side:  "))
     side2=float(input("Second side:  "))
     side3=float(input("Third side:  "))
     if side1==side2 and side1==side3:
         print("Equilatero")
     elif side1 !=side2 and side2!=side3 and side3!=side1:
         print("Escaleno")
     else:
        print("Isosceles")
#sides_of_triangle()
"""
Hacer un programa para ingresar 4 números. Luego analizar e informar por pantalla si los mismos se encuentran ordenados de forma decreciente.
"""
def ordenade():
     number1=float(input("Enter a number: "))
     number2=float(input("Enter a number: "))
     number3=float(input("Enter a number: "))
     number4=float(input("Enter a number: "))
     contador=0
     if number1<number2:
        contador +=1
     if number2<number3:
         contador +=1
     if number3<number4:
         contador +=1
     if contador==3:
         print("Estan ordenados")
     else:
         print("Desordenados",contador)
        
#ordenade()
    

"""
8. El negocio de desinfectante antes mencionado vende además detergente suelto, y los precios se aplican según la siguiente escala:
a. 25 ARS por litro los primeros 50 litros. 
b. 20 ARS por litro si la venta es de 51 a 200 litros.
c. 15 ARS por litro si la venta es de 201 a 500 litros
d. 10 ARS por litro si la venta es de más de 500 litros.
Además, si paga en efectivo, tiene un adicional del 10% sobre el importe final.
Hacer un programa que solicite la cantidad de litros vendidos y el tipo de pago (ingresará 1 si paga en efectivo y 0 con cualquier otro medio de pago) y calcule
y emita por pantalla el monto final a abonar por el cliente.
"""
def liters_sold():
    cuantity_liters=float(input("Enter cuantity of liters: "))
    type_of_pay=int(input("Form of pay (1=cash,0=card): "))
    if cuantity_liters>500:
        total_to_pay=cuantity_liters*10
    elif cuantity_liters>200 and cuantity_liters<=500:
        total_to_pay=cuantity_liters*15
    elif cuantity_liters>50 and cuantity_liters<=200:
        total_to_pay=cuantity_liters*20
    else:
        total_to_pay=cuantity_liters*25
    if type_of_pay==1:
        total_to_pay=total_to_pay*0.90
    print(total_to_pay)
#liters_sold()
"""
9. Una importante marca de computadoras permite elegir cierta configuración del equipo a comprar. Para ello existe la siguiente escala de precios:
Además, el equipo viene con un disco que permite almacenar 500 GB de información y que se puede ampliar a 1 TB si asi lo desea, lo cual tiene un costo adicional de USD 300.
Hacer un programa que solicite la opción de procesador, la opción de memoria RAM, y si extiende el disco o no (ingresa 1 para extender y 0 para no extender) y calcule y emita por pantalla el monto de la máquina seleccionada.
Nota: si no entendes nada de compus, procesadores y eso, mira: https://youtu.be/Bm3X8+HVV-s
"""
def choose_computer():
    procesador=str(input("Enter the processor to chose (i5,i7,i9): "))
    ram=str(input("Enter the memory ram to chose(8gb,16gb,32gb): "))
    error=0
    if procesador=="i5":
        if ram == "8gb":
            total_to_pay=800
        elif ram =="16gb":
            total_to_pay=900
        elif ram =="32gb":
            total_to_pay=1000
        else:
            return print("Bad enter the value of the ram")
    elif procesador=="i7":
        if ram == "8gb":
            total_to_pay=900
        elif ram =="16gb":
            total_to_pay=1000
        elif ram =="32gb":
            total_to_pay=1400
        else:
            return print("Bad enter the value of the ram")
    elif procesador=="i9":
        if ram == "8gb":
            total_to_pay=1200
        elif ram =="16gb":
            total_to_pay=1400
        elif ram =="32gb":
            total_to_pay=2000
        else:
            error+=1
            return print("Bad enter the value of the ram")
    else:
        return print("Bad enter the value of processor")
    if error==0:
        disco=float(input("DO you want buy a hard-disk (1=Yes,0=No): "))
        if disco==1:
            total_to_pay+=300
            return  print(total_to_pay)
        else:
            return  print(total_to_pay)
    else:
        return
#choose_computer()
"""
10. Hacer un programa que solicite cuatro números y emitir un cartel aclaratorio si son todos iguales entre si, caso contrario, no emitir nada
"""
def equals():
     number1=float(input("Enter a number: "))
     number2=float(input("Enter a number: "))
     number3=float(input("Enter a number: "))
     number4=float(input("Enter a number: "))
     if number1==number2 and number2==number3 and number3==number4:
        print("All are equals")
#equals()

"""
11. Hacer un programa para ingresar tres números y luego mostrarlos ordenados de menor a mayor
"""
def ordenade():
    number1=float(input("Enter a number: "))
    number2=float(input("Enter a number: "))
    number3=float(input("Enter a number: "))
    ordenade=[]*3
    if number1 >number2:
        ordenade.insert(0,number1)
        ordenade.insert(1,number2)
    else:
        ordenade.insert(1,number1)
        ordenade.insert(0,number2)
    if number3>ordenade[0]:
        aux=ordenade[0]
        ordenade.insert(0,number3)
        if aux >ordenade[1]:
            ordenade.insert(2,ordenade[1])
            ordenade.insert(1,aux)
        else:
            ordenade.insert(2,aux)
    elif number3>ordenade[1]:
        ordenade.insert(2,ordenade[1])
        ordenade.insert(1,number3)
    else: 
        ordenade.insert(2,number3)
    print(ordenade)
#ordenade()

"""
12. Hacer un programa para ingresar tres números y emitir un cartel aclaratorio si la suma de los dos primeros es mayor al producto del segundo con el tercero.
"""
def operation_weird_3():
    number1=float(input("Enter a number: "))
    number2=float(input("Enter a number: "))
    number3=float(input("Enter a number: "))
    if (number1+number2) > (number2*number3):
        print("Is bigger")
#operation_weird_3()