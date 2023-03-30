from pregunta4 import Alumno
import unittest

class Main(unittest.TestCase):
    def test1(self):
        alumno1 = Alumno("Paco", 7)
        alumno2 = Alumno("Ruben", 10)
        alumno3 = Alumno("Claudia", 8)
        alumno4 = Alumno("Pepe", 4)
        print(alumno1)
        print(alumno2)
        print(alumno3)
        print(alumno4)
        self.assertEqual(alumno1.__str__(), "Nombre: Paco, Nota: 7")
        self.assertEqual(alumno2.__str__(), "Nombre: Ruben, Nota: 10")
        self.assertEqual(alumno3.__str__(), "Nombre: Claudia, Nota: 8")
        self.assertEqual(alumno4.__str__(), "Nombre: Pepe, Nota: 4")





if __name__ == "__main__":
    unittest.main()
