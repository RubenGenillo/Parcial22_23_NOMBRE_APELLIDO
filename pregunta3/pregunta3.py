class Alumno:
    def __init__(self, nombre, nota) -> None:
        self.nombre = nombre
        self.nota = nota
        print("se ha creado con exito")

    def calificacion(self):
        if self.nota < 5:
            return "suspenso"
        else:
            return "aprobado"