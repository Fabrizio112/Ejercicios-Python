class Banco:
    def __init__(self,nombre):
        self.nombre=nombre
        self.cuentas=[]
    def listar_cuentas(self):
        for cuenta in self.cuentas:
            print(f"Titular: {cuenta.titular}\nMonto de cuenta: {cuenta.monto}")
    def mostrar_total_depositos(self):
        montos_totales=0
        for cuenta in self.cuentas:
            montos_totales+=cuenta.monto

class Cuenta:
    def __init__(self,titular,monto):
        self.titular=titular
        self.monto=monto
    def __str__(self):
        return f"Titular de cuenta :{self.titular}\nMonto de la cuenta: {self.monto}"
    def depositar(self,monto):
        self.monto+=monto
    def extraer(self,monto):
        self.monto-=monto

class PlazoFijo(Cuenta):
    def __init__(self, titular, monto,interes_anual,plazo):
        super().__init__(titular, monto)
        self.interes_anual=interes_anual
        self.plazo=plazo
    def __str__(self):
        return super().__str__()+ f"Interes Anual :{self.interes_anual}\n Dias del Plazo Fijo : {self.plazo}"

class CajaDeAhorro(Cuenta):
    def __init__(self, titular, monto):
        super().__init__(titular, monto)
    def __str__(self):
        return super().__str__()
    
def main ():
    banco = Banco('Banco Santander')

    ca1 = CajaDeAhorro('Fabrizio',1500)
    pf1 = PlazoFijo('Fabri',3000,0.98,30)

    banco.cuentas.append(ca1)
    banco.cuentas.append(pf1)
    print (banco.mostrar_total_depositos())

main()    