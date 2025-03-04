from abc import ABC, abstractmethod

# Constantes  
SALARIO_MINIMO = 84000  # Valor del salario mínimo  
AUXILIO_TRANSPORTE = 12600  # Valor del auxilio de transporte 

class Usuario(ABC):
    def __init__(self, nombre: str, palabra_clave: str, edad: int):
        self.nombre = nombre
        self.palabra_clave = palabra_clave
        self.edad = edad

    @abstractmethod
    def calcular_salario(self) -> int:
        pass
