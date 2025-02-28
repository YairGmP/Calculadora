#Definicion de la clase calculadora que proporciona operaciones matematicas 
class calculadora:
    #Metodo para sumar dos numeros
    def suma(self, a, b):
        return a + b 
    
    def resta(self, a, b):
        return a - b
    
    def multiplicacion(self, a, b):
        return a * b
    
    def division(self, a, b):
        if b==0:
            raise ValueError("No se puede dividir por 0")
        return a / b
    