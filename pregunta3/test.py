from pregunta3 import Alumno
import unittest

class Main(unittest.TestCase):
    def test1(self):
        alumno1 = Alumno("Paco", 7)
        alumno2 = Alumno("Ruben", 10)
        alumno3 = Alumno("Claudia", 8)
        alumno4 = Alumno("Pepe", 4)
        self.assertIsInstance(alumno1, Alumno)
        self.assertIsInstance(alumno2, Alumno)
        self.assertIsInstance(alumno3, Alumno)        
        self.assertIsInstance(alumno4, Alumno)
    def test2(self):
        alumno1 = Alumno("Paco", 7)
        alumno2 = Alumno("Ruben", 10)
        alumno3 = Alumno("Claudia", 8)
        alumno4 = Alumno("Pepe", 4)        
        self.assertEqual(alumno1.calificacion(), "aprobado")
        self.assertEqual(alumno2.calificacion(), "aprobado")
        self.assertEqual(alumno3.calificacion(), "aprobado")
        self.assertEqual(alumno4.calificacion(), "suspenso")





if __name__ == "__main__":
    unittest.main()
