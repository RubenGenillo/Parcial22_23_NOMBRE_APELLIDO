class Alumno:
    def __init__(self, nombre, nota) -> None:
        self.nombre = nombre
        self.nota = nota
        print("se ha creado con exito")

    def __str__(self):
        return "Nombre: {}, Nota: {}". format(self.nombre, self.nota)
    

    def calificacion(self):
        if self.nota < 5:
            return "suspenso"
        else:
            return "aprobado"