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

class Administrativo(Usuario):
    def __init__(self, nombre: str, palabra_clave: str, edad: int):
        super().__init__(nombre, palabra_clave, edad)

    def calcular_salario(self) -> int:
        print(SALARIO_MINIMO + AUXILIO_TRANSPORTE)
        return SALARIO_MINIMO + AUXILIO_TRANSPORTE


class PrestacionServicios(Usuario):
    def __init__(self, nombre: str, palabra_clave: str, edad: int, horas_trabajadas: int, tarifa_hora: int):
        super().__init__(nombre, palabra_clave, edad)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora

    def calcular_salario(self) -> int:
        print(self.horas_trabajadas * self.tarifa_hora)
        return self.horas_trabajadas * self.tarifa_hora


class TerminoDirectivo(Usuario):
    def __init__(self, nombre: str, palabra_clave: str, edad: int, nivel: str):
        super().__init__(nombre, palabra_clave, edad)
        self.nivel = nivel

    def calcular_salario(self) -> int:
        if self.nivel == "ING":
            print(SALARIO_MINIMO + int(0.45 * SALARIO_MINIMO))
            return SALARIO_MINIMO + int(0.45 * SALARIO_MINIMO)
        elif self.nivel == "Gerente":
            print(SALARIO_MINIMO + int(0.45 * SALARIO_MINIMO))
            return SALARIO_MINIMO + int(0.45 * SALARIO_MINIMO)
        elif self.nivel == "Presidente":
            print(SALARIO_MINIMO + int(0.45 * SALARIO_MINIMO))
            return SALARIO_MINIMO + int(0.45 * SALARIO_MINIMO)
        else:
            raise ValueError("Nivel desconocido")
