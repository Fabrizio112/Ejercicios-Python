class Persona:
    def __init__(self,dni,nombre):
        self.dni=dni
        self.nombre=nombre
    def __str__(self):
        return f"Nombre:{self.nombre}\nDNI:{self.dni}"

class Docente(Persona):
    def __init__(self, dni, nombre,legajo,sueldo):
        super().__init__(dni, nombre)
        self.legajo=legajo
        self.sueldo=sueldo
    def __str__(self):
        return super().__str__()+f"Legajo: {self.legajo}\nSueldo: {self.sueldo}"

class Alumno(Persona):
    def __init__(self, dni, nombre,legajo,nota1,nota2):
        super().__init__(dni, nombre)
        self.legajo=legajo
        self.nota1=nota1
        self.nota2=nota2
    def __str__(self):
        return super().__str__() +f"Legajo: {self.legajo}\nNotas : {self.nota1}/{self.nota2}"
    def get_promedio(self):
        return (self.nota1+self.nota2)/2
        
class Curso:
    def __init__(self,nombre,docente):
        self.nombre=nombre
        self.docente=docente
        self.alumnos=[]
    def listado_alumnos(self):
        for alumno in self.alumnos:
            print(alumno.nombre)
    def cantidad_regulares(self):
        alumnos_regulares=0
        for alumno in self.alumnos:
            if alumno.nota1 >=4 and alumno.nota2>=4:
                alumnos_regulares+=1
        return alumnos_regulares
    def promedio_total(self):
        acumulador_total=0
        for alumno in self.alumnos:
            acumulador_total+=alumno.get_promedio()
        return acumulador_total/len(self.alumnos)



def main():
    profesor=Docente("1234","Hola",234,"$3500")
    fabri=Alumno("44078507","Fabrizio",1,8,9)
    julian=Alumno("334422","julian",2,3,2)
    jose=Alumno("123456","jose",3,6,8)
    pepito=Alumno("918246","pepito",4,4,4)
    roberto=Alumno("565474521","roberto",5,3,10)

    curso=Curso("Programacion",profesor)
    curso.alumnos.append(fabri)
    curso.alumnos.append(julian)
    curso.alumnos.append(jose)
    curso.alumnos.append(pepito)
    curso.alumnos.append(roberto)
    curso.listado_alumnos()
    print(curso.promedio_total())
    print(curso.cantidad_regulares())

main()

