"""
Hacer un programa para ingresar un número y luego se emita por pantalla un cartel aclaratorio si "Es mayor a 10" o "No es mayor a 10"
"""
def is_greater_than_ten():
    num1=float(input("Enter a number please : "))
    if num1>10:
        print("{} ,Is greater than ten".format(num1))
    elif num1<10:
        print("{},Is less than ten".format(num1))
    else :
        print("{},Is same to ten ".format(num1))

""" is_greater_than_ten() """

"""
2. Hacer un programa para ingresar dos números distintos y luego se muestre por pantalla el menor de ellos.
Nota: no te olvides del ambiente ideal. Qué es eso? Mirá: https://youtu.be/TTvnrt.1KUZM?t=931
"""
def compare_two_numbers_less():
    num1=float(input("Enter a number please : "))
    num2=float(input("Enter a number please : "))
    if num1>num2:
        print("{} is less than {}".format(num2,num1))
    elif num2>num1: 
        print("{} is less than {}".format(num1,num2))
    else:
        print("Same")
""" compare_two_numbers_lower() """
"""
3. Hacer un programa para ingresar dos números y que luego emita por pantalla el mayor de ellos o un cartel aclaratorio "Son iguales" en el caso de que así sea.
Nota: los números pueden ser iguales.
"""
def compare_two_numbers_greater():
    num1=float(input("Enter a number please : "))
    num2=float(input("Enter a number please : "))
    if num1>num2:
        print("{} is greater than {}".format(num1,num2))
    elif num2>num1: 
        print("{} is greater than {}".format(num2,num1))
    else:
        print("Same")
""" compare_two_numbers_greater() """
"""
4. Hacer un programa para ingresar un número y luego se emita un cartel por pantalla "Positivo" si el número es mayor a cero, "Negativo" si el número es
menor a cero o "Cero" si el número es igual a cero.
Nota: requiere más de in IF! Repasá cómo se escribirían:
https://youtu.be/TTvnrL1KUZM?t=1180
"""
def greater_same_less_cero():
    num1=float(input("Enter a number please : "))
    if num1>0:
         print("Positive")
    elif num1<0:
        print("Negative")
    else:
        print("Cero")
""" greater_same_less_cero() """
"""
5. Hacer un programa para ingresar un número y mostrar por pantalla un cartel aclaratorio si el mismo es PAR o IMPAR.
Nota: leé sobre el operador "Resto". En el próximo video lo explicaremos!
"""
def even_or_odd():
    num1=float(input("Enter a number please : "))
    if num1%2==0:
         print("Even")
    else :
        print("Odd")

""" even_or_odd() """

"""
6. Una casa de video juegos otorga un descuento dependiendo del importe de la compra realizada según los siguientes valores:
• Si el importe es menor a ARS 1000, no hay descuento. • Si el importe es ARS 1000 o más pero menor a ARS 5000, aplica un
descuento del 10%. Si el importe es ARS 5000 o más, aplica un cuento del 18%.Hacer un programa para ingresar un importe de venta y luego muestre por pantalla el importe final con el descuento que corresponda.
"""
def discount_buy():
    buy=float(input("Enter your buy: "))
    if buy >=5000:
        discount_final=buy*0.85
    elif buy>=1000 and buy<5000:
        discount_final=buy*0.90
    else:
        discount_final=buy
    print(discount_final)

""" discount_buy() """

"""
 7. Hacer un programa para ingresar cuatro números distintos y luego mostrar porpantalla el mayor de ellos.
"""
def bigger():
      num1=float(input("Enter a number please : "))
      num2=float(input("Enter a number please : "))
      num3=float(input("Enter a number please : "))
      num4=float(input("Enter a number please : "))
      if num1>num2:
          bigger=num1
      else:
          bigger=num2
      if mayor>num3:
         bigger=bigger
      else:
          mayor=num3
      if bigger >num4:
          bigger=bigger
      else:
          mayor=num4
      print( bigger)
""" bigger() """
"""
8. Hacer un programa para ingresar cuatro números distintos y luego mostrar por pantalla el menor de ellos.
"""
def smaller():
      num1=float(input("Enter a number please : "))
      num2=float(input("Enter a number please : "))
      num3=float(input("Enter a number please : "))
      num4=float(input("Enter a number please : "))
      if num1>num2:
          smaller=num2
      else:
          smaller=num1
      if smaller>num3:
         smaller=num3
      else:
          smaller=smaller
      if smaller>num4:
          smaller=num4
      else:
          smaller=smaller
      print( smaller)
""" smaller() """
"""
9. Hacer un programa para ingresar cinco números distintos y luego mostrar por pantalla el mayor y el menor de ellos. 
"""
def bigger_and_smaller():
      num1=float(input("Enter a number please : "))
      num2=float(input("Enter a number please : "))
      num3=float(input("Enter a number please : "))
      num4=float(input("Enter a number please : "))
      num4=float(input("Enter a number please : "))
      if num1>num2:
          smaller=num2
          bigger=num1
      else:
          smaller=num1
          bigger=num2
      if smaller>num3:
         smaller=num3
         bigger=bigger
      else:
          smaller=smaller
          bigger=num3
      if smaller >num4:
          smaller=num4
      else:
          smaller=smaller
          bigger=num4
      print( smaller,bigger)
""" bigger_and_smaller() """

"""
10. Hacer un programa para ingresar cuatro números y luego mostrar por pantalla
cuáles son mayores a 100. 
"""
def how_many_greater_than_100():
      num1=float(input("Enter a number please : "))
      num2=float(input("Enter a number please : "))
      num3=float(input("Enter a number please : "))
      num4=float(input("Enter a number please : "))
      bigger_one_hundred=0
      if num1>100:
         bigger_one_hundred  +=1
      if num2>100:
          bigger_one_hundred +=1
      if num3>100:
          bigger_one_hundred +=1
      if num4>100:
          bigger_one_hundred +=1
      print(bigger_one_hundred)
    

""" how_many_greater_than_100() """
"""
11. Hacer un programa para ingresar cuatro números y luego mostrar por pantalla cuántos son menores a 100.
"""
def how_many_less_than_100():
      num1=float(input("Enter a number please : "))
      num2=float(input("Enter a number please : "))
      num3=float(input("Enter a number please : "))
      num4=float(input("Enter a number please : "))
      smaller_than_one_hundred=0
      if num1<100:
           smaller_than_one_hundred  +=1
      if num2<100:
           smaller_than_one_hundred +=1
      if num3<100:
           smaller_than_one_hundred +=1
      if num4<100:
          smaller_than_one_hundred +=1
      print( smaller_than_one_hundred)
""" how_many_less_than_100() """
"""
 12.
 Hacer un programa para ingresar un valor que estará expresado en minutos. Si los minutos superan los 60,
   pasar el valor a horas, de lo contrario dejarlo en minutos. Mostrar el resultado en pantalla aclarando 
   si se muestran minutos u horas.
"""
def time():
    time=float(input("Enter your time in minutes :"))
    if time>60:
        return print(time/60,"hours" )
    else:
        return print(time , "minutes")
time()