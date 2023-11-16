"""
-Crear un archivo de texto llamado "archivo.txt" en modo escritura
-Escribir en 3 lineas separadas, la siguiente frase de Stephen Hawking

"Estamos quedandonos sin espacio y los únicos espacios a los que podemos ir son otros mundos"
"Solo somos una raza avanzada de monos en un planeta menor de una estrella promedio"
"Si entiendes el Universo . de alguna form lo controlas"

-Cerrar el archivo
"""
def funcion_archivo():
    archivo=open("archivo.txt","w")
    archivo.write("Estamos quedandonos sin espacio y los únicos espacios a los que podemos ir son otros mundos\n")
    archivo.write("Solo somos una raza avanzada de monos en un planeta menor de una estrella promedio\n")
    archivo.write("Si entiendes el Universo, de alguna forma lo controlas\n")
    archivo.close()

#funcion_archivo()

"""
-Abrir el archivo creado "archivo.txt" en modo lectura
-Leer de a una por vez cada linea del archivo
-Grabar en una variable la longitud de cada linea de texto
-Presentar por pantalla la cantidad total de carateres del texto
-¿Se podria hacer de alguna otra manera?
-Pruebe editando el archivo con algun editor y corriendo nuevamente el programa para ver si cuenta bien el texto modificado

"""

def funcion_archivo2():
    archivo=open("archivo.txt","r")
    textos=archivo.readlines()
    longitud_textos=[]
    cantidad_total_caracteres=0
    for texto in textos:
        longitud_textos.append(len(texto))
        cantidad_total_caracteres+=len(texto)
    
   

#funcion_archivo2()