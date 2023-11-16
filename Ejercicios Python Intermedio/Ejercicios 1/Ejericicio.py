"""Desarrolle una clase PUNTO, que representa una punto en el plano
La clase contiene dos atributos, X, Y, que son los números que 
representa ese punto en el plano
Se debe definir un constructor __init__ que permita crear un 
número pasándole las dos coordenadas.
La clase debe incorportar un método __str__ que permita 
mostrar un punto como (X,Y)
La clase debe incorporar un método getCuadrante que 
indique en qué cuadrante se encuentra el punto, 
teniendo en cuenta el grafico adjunto.
La clase debe incorporar un método getDistanciaOrigen 
que indique la distancia del punto al origen (0,0) 
según la fórmula indicada.
"""
class Punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"X:{self.x}\nY:{self.y}"
    def getCuadrante(self):
        if self.x>0 and self.y>0 :
            print("Pertenece al cuadrante 1")
        elif self.x<0 and self.y<0:
            print("Pertenece al cuadrante 3")
        elif self.x>0 and self.y<0:
            print("Pertenece al cuadrante 4")
        else:
            print("Pertenece al cuadrante 2")
    def getDistanciaOrigen(self):
        if self.x >0:
            print(f"X es positivo esta a {self.x} numeros de la posicion inicial")
        elif self.x<0:
            print(f"X es negativo esta a {self.x} numeros de la posicion inicial")
        if self.y >0:
            print(f"Y es positivo esta a {self.y} numeros de la posicion inicial")
        elif self.y<0:
            print(f"Y es negativo esta a {self.y} numeros de la posicion inicial")

fabri=Punto(-24,50) 
""" 
Desarrollar una clase Lado, que representa un lado de una figura geométrica
Dicho lado debe tener un único atributo, que es su longitud
Desarrollar una clase Figura (geométrica)
La figura geométrica debe tener AL MENOS tres lados
La figura debe tener un constructor __init__
La figura debe tener un método perimetro() que devuelva el perímetro de la figura
Desarrollar tres clases que hereden de Figura
Una clase Triángulo
Una clase Cuadrado
Una clase Rectángulo
Cada clase debe tener un constructor __init__ que reciba los parámetros necesarios
Cada clase debe tener un método perimetro() que devuelva el perímetro de la figura
 """

class Lado:
    def __init__(self,longitud):
        self.longitud=longitud

class Figura:
    def __init__(self,lado1,lado2,lado3):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3
    def perimetro(self):
        return self.lado1.longitud +self.lado2.longitud + self.lado3.longitud
    
class Triangulo(Figura):
    def __init__(self, lado1, lado2, lado3):
        super().__init__(lado1, lado2, lado3)
    def perimetro(self):
        return super().perimetro()
    
class Cuadrado(Figura):
    def __init__(self, lado1, lado2, lado3,lado4):
        super().__init__(lado1, lado2, lado3)
        self.lado4=lado4
    def perimetro(self):
        return super().perimetro() + self.lado4.longitud
    
class Rectangulo(Figura):
    def __init__(self, lado1, lado2, lado3,lado4):
        super().__init__(lado1, lado2, lado3)
        self.lado4=lado4
    def perimetro(self):
        return super().perimetro()+ self.lado4.longitud

""" lado_1=Lado(30)
lado_2=Lado(10)
lado_3=Lado(5)
lado_4=Lado(10)


triangulo=Figura(lado_1,lado_2,lado_3) """
