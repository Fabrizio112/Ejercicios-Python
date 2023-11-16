"""
Se dispone de una lista de 10 grupos de números enteros separados entre ellos por ceros. Se pide determinar e informar:
a. El número de grupo con mayor porcentaje de números impares positivos respecto al total de números que forman el grupo. 
b. Para cada grupo, el último número primo y en qué orden apareció en ese grupo.
Si en un grupo no hubiera números primos, informarlo con un cartel aclaratorio.
c. Informar cuántos grupos están formados por todos números ordenados de mayor a menor.
"""
def groupes_separated():
    impares_positivos=None
    posicion_impares_positivos=None
    contador_grupos_ordenados=0
    for i in range(10):
        orden=None
        bd=0
        contador=0
        primo=None
        posicionPrimo=None
        for n in range(10):
            contadorPrimo=0
            num=int(input("Enter a number: "))
            if not num%2==0 and num>0:
                contador+=1
            for p in range(num+1):
                if not p==0:
                    if num%p==0:
                        contadorPrimo+=1
            if contadorPrimo==2:
                primo=num
                posicionPrimo=n+1
            if n==0:
                orden=num
            else:
                if num<orden:
                    orden=num
                else:
                    bd=1
            if n==9:
                 if i==0:
                    impares_positivos=contador
                    posicion_impares_positivos=i+1
                 else:
                     if contador>impares_positivos:
                         impares_positivos=contador
                         posicion_impares_positivos=i+1
                 if primo==None:
                     print("No hay numeros primos aqui")
                 if bd==0:
                     contador_grupos_ordenados+=1
                 print(primo,posicionPrimo)
    print(posicion_impares_positivos,contador_grupos_ordenados)        
#groupes_separated()
"""
2. Una compañía de electricidad necesita calcular anualmente el consumo que ha registrado cada uno de sus usuarios
 y el monto pagado por cada uno de ellos. 
Para ello tiene un lote de registros por cada uno de los usuarios con los siguientes datos:
Zona (numérico entero).
Número de cliente (número de cuatro dígitos no correlativos).
Cantidad de kilovatios consumidos en el periodo.
El lote se encuentra agrupado (no ordenado) por zona y finaliza con un registro con zona igual a cero.
Se pide generar un listado con el siguiente formato:
Zona: XX
Cantidad de usuarios de la zona: XX 
Total facturado en la zona: XX
Zona: XX
Cantidad de usuarios de la zona: XX 
Total facturado en la zona: XX
El precio es escalonado según la siguiente escala:
$0.10 por kv por los primeros 100 kv de consumo,
$0.12 por kv por el consumo de 101 a 200 kvs.
$0.15 por kv por el consumo de 201 kvs en adelante.
"""

"""
Hacer un programa para ingresar los valores de los pesos de distintas encomiendas que se deben enviar a distintos clientes 
y que finaliza cuando se ingresa un peso negativo. Se deben agrupar las encomiendas en camiones que
pueden transportar hasta 200 kilos en total.
Por ejemplo:
10, 20,
140, 70, 100,
40, 10, 50, 80, 90, 30, 40, 50,
-10.
Camión 1. Camión 2 Camión 3
Camión 4 Camión 5

Se pide determinar e informar:
a. El número de camión y peso total de encomiendas (Camión 1: 170kg, Camión 2: 170kg, etc.).
b. El número de camión que transporta mayor cantidad de encomiendas (en el ejemplo anterior sería el camión 3 con 4 encomiendas).
c. La cantidad de camiones que se terminaron cargando.
"""


"""
4. Una compañía de turismo aventura registró los paquetes vendidos durante la última temporada vacacional. Para cada venta se ingresó:
Número de paquete (4 dígitos no correlativos).
• Cantidad de personas incluidas.
• Precio por persona.
Horas totales de actividades. 
Tipo de aventura ("M", Montaña. "T", Trekking. "R", Rafting. "B", Bicicleta. "C", Canopy. "E", Escalar. "K", Sky. "S", Snowboard. "J", ", Jumping. "P" Parapente).

El lote se encuentra no ordenado y agrupado por tipo de aventura y corta con número de paquete cero. En el lote no se ingresan registros cuyo tipo de aventura no se haya vendido.
A partir de dichos datos, se solicita informar:
a. La cantidad de paquetes vendidos de cada tipo de aventura.. 
b. La cantidad total de personas que disfrutaron de las aventuras durante la temporada.
c. El total recaudado por cada venta.
d. La venta con mayor importe de cada tipo de aventura.
e. El paquete con menos horas incurridias y en qué tipo de actividad fue. 
"""


"""
5. Una empresa registró las compras realizadas a sus distintos proveedores durante todo el año anterior.
 Para cada compra se registraron los siguientes datos: 
⚫ Número de proveedor (número de cuatro cifras no correlativo).
Dia (1 a 31).
Mes (1 a 12)
Tipo de Factura (Responsable inscripto: "A",Consumidor Final: "8",Monotributo: "C").
⚫ Número de Producto (número no correlativo).
Cantidad comprada. Precio unitario del producto.
Este lote finaliza con un registro con número de proveedor igual a 0.
 Los registros están agrupados por número de proveedor. En el lote anterior no aparecen
registros de los proveedores a los que que no se les hayan realizado compras. Se pide determinar e informar:
a. El monto máximo registrado en una sola compra por cada proveedor y el número de proveedor al que se le compró.
b. La inversión total de todo el año discriminada por tipo de factura.
c. La compra con menor monto registrada durante el mes de Agosto junto al número de producto comprado.
d. La cantidad de compras que se realizaron a cada proveedor.
e. El número de producto con mayor cantidad comprada en una sola compra y en qué proveedor se compró
"""