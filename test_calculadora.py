#Importacion del modulo unittest para poder realizar pruebas unitarias 
import unittest 

#importacion de la clase calculadorea desde el archivo calculadora.py
from Calculadora import calculadora

#Definicion de la clase de pruebas que hereda de unitest.testcase
class TestCalculadora(unittest.TestCase):
    #Metodo que se ejecuta antes de cada prueba
    def setUp(self):
        #creamos una instancia para usar en las prubas
        self.calc = calculadora()
        
    #prueba del metodo suma
    def test_suma(self):
     #prueba la suma de dos numero positivos 
        self.assertEqual(self.calc.suma(5,4),9) 
    #     #prueba la suma de un numer0 negativo y uno positivo
        self.assertEqual(self.calc.suma(-1,1),0)
    #     #prueba de suma de 2 0
        self.assertEqual(self.calc.suma(0,0),0)
        
    def test_resta(self):
      # prueba la resta de dos números positivos
        self.assertEqual(self.calc.resta(10, 4), 6)
     # prueba la resta de dos números iguales
        self.assertEqual(self.calc.resta(7, 7), 0)
     # prueba la resta de dos números negativos
        self.assertEqual(self.calc.resta(-6, -3), -3)

    def test_multiplicacion(self):
    #     # prueba la multiplicación de dos números positivos
        self.assertEqual(self.calc.multiplicacion(4, 2), 8)
    #     # prueba la multiplicación de un número por 0 (debe dar 0)
        self.assertEqual(self.calc.multiplicacion(7, 0), 0)
    #     # prueba la multiplicación de un número negativo por uno positivo
        self.assertEqual(self.calc.multiplicacion(-3, 3), -9)

    #prueba del metodo division
    def test_division(self):
        #prueba de division exacta 
        self.assertEqual(self.calc.division(12,2),6)
        #prueba la division con resultado decimal 
        self.assertAlmostEqual(self.calc.division(5, 2), 2.50, places=2)
    #     #prueba con division periodica usando asserAlmostEqual para comparar con precision limitada 
        self.assertAlmostEqual(self.calc.division(10, 3), 3.33, places=2)
    #  # Prueba específica para verificar el manejo de la división por cero
        with self.assertRaises(ZeroDivisionError):
            self.calc.division(6, 0)

     
#Bloque condicional que permite ejecutar las pruebas directamente             
if __name__ == '__main__':
    #inicializar la ejecucion de todas las pruebas definidas en la clase
    unittest.main()