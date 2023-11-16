"""
-Crear una lista por comprension que contenga el primer caracter de cada palabra
-Crear una lista por comprension que contenga la longitud de cada palabra
-Utilizando reduce calcular la cantidad total de caracteres que contienen todas las palabras de la lista
"""
from functools import reduce

"""
list=["Aruba","Jamaica","Bermuda","Bahama","Key Largo","Montigo"]


primer_letra=[palabra[0] for palabra in list]
longitud_palabra=[len(palabra) for palabra in list]

def cantidad_caracteres(lista):
    contador_caracteres=reduce( lambda acumulador,x : acumulador + len(x), lista,0)
    return contador_caracteres

cantidad_total_caracteres=cantidad_caracteres(list)
 """
"""
Utilizando las rutinas random,crear una lista por comprension que contenga 50 numeros al azar ,enteros 
entre 1,100
- Utilizando filter crear una lista que contenga solo los mayores a 50 y otra solo los menores
o iguales a 50
-Utilizando Map ,crear una lista que contenga todos los numeros impares pero con el signo invertido(negativos)
-Utilizando Reduce, obtener la sumatoria de la lista generada en el item anterior
"""
""" import random

lista_numeros=[random.randint(1,100) for i in range(50)]
mayores_cincuenta=[num for num in lista_numeros if num>50]
menores_o_iguales_cincuenta=[num for num in lista_numeros if num<=50]
lista_impares=[num for num in lista_numeros if num%2!=0]

numeros_impares=list(map(lambda x:-x,lista_impares))
sumatoria_impares=reduce(lambda acc,x:acc+x,numeros_impares,0)
print(lista_numeros)
print(mayores_cincuenta)
print(menores_o_iguales_cincuenta)
print(lista_impares)
print(numeros_impares)
print(sumatoria_impares) """