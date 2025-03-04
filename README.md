# Prueba Técnica DKD Ingenierías

## Bienvenido a nuestra prueba técnica. Aquí evaluaremos tus habilidades técnicas, lógica de programación y capacidad para resolver problemas algorítmicos.

Para cada prueba, debes crear un entorno virtual e implementar las pruebas de integración junto con su respectiva documentación.

## Pongamos a prueba nuestros conocimientos en Programación Orientada a Objetos (POO) con un Sistema de Control de Usuarios 😉 

En este proyecto se definen dos constantes fundamentales para el cálculo de salarios:  

```python
# Constantes  
SALARIO_MINIMO = 84000  # Valor del salario mínimo  
AUXILIO_TRANSPORTE = 12600  # Valor del auxilio de transporte  
```

Mario necesita un sistema de control de usuarios basado en una clase principal:


```python
from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre: str, palabra_clave: str, edad: int):
        self.nombre = nombre
        self.palabra_clave = palabra_clave
        self.edad = edad

    @abstractmethod
    def calcular_salario(self) -> int:
        pass
```

## Tipos de Usuarios
Mario necesita crear tres tipos de usuarios, los cuales deben heredar de la clase `Usuario`:

- **Usuarios Administrativos**
- **Usuarios por Prestación de Servicios**
- **Usuarios de Término Directivo**

## Reglas de Negocio
Cada tipo de usuario debe cumplir con las siguientes reglas de negocio:

### 1. Usuarios Administrativos
- Reciben un salario equivalente al **sueldo mínimo** más el **auxilio de transporte**.

### 2. Usuarios por Prestación de Servicios
- Su salario depende del valor de la hora trabajada, es decir, el pago se calcula en función del número de horas laboradas y la tarifa por hora establecida.

### 3. Usuarios de Término Directivo
- Reciben un salario equivalente al **sueldo mínimo** más un **45% adicional del sueldo mínimo**.
- El porcentaje adicional depende del nivel del usuario, que puede ser uno de los siguientes:
  - **Ingeniero (ING)**
  - **Gerente**
  - **Presidente**

Para esta prueba, debes implementar los principios de Encapsulamiento, Herencia y Polimorfismo. Además, es obligatorio desarrollar pruebas de integración, en las cuales deberás crear dos usuarios por cada tipo de cargo.

### **El código será evaluado según:**
 * ✅ Uso correcto de POO (Encapsulamiento, Herencia, Polimorfismo).
 * ✅ Limpieza del código y buenas prácticas.
 * ✅ Pruebas unitarias que validen la funcionalidad.

## Veamos qué tal dominamos la programación funcional. 🚀

## Objetivo
Evaluar el conocimiento y aplicación de **Programación Funcional** en Python.

Se evaluarán los siguientes aspectos:
* ✅ **Uso de funciones puras**
* ✅ **Inmutabilidad de datos**
* ✅ **Uso de funciones de orden superior**
* ✅ **Uso de map, filter y reduce**
* ✅ **Pruebas de integración**

## Descripción

María tiene un diccionario de palabras y quiere saber cuántos **palíndromos** hay en él. Debes desarrollar un programa en Python utilizando **Programación Funcional** que le ayude a identificar la cantidad de palíndromos en el diccionario de datos.

### ¿Qué es un Palíndromo?
Un palíndromo es una palabra que se lee igual de izquierda a derecha que de derecha a izquierda.

Ejemplos de palíndromos:
- **oso**
- **radar**
- **reconocer**
- **anilina**

## Requisitos de Implementación

### 📌 **Funciones Puras**
- Implementar una función pura que reciba una lista de palabras y devuelva únicamente las palabras que sean palíndromos.

### 📌 **Funciones de Orden Superior**
- Utilizar **map(), filter() o reduce()** para procesar la lista de palabras.

### 📌 **Inmutabilidad**
- No modificar directamente la lista original de palabras.

## Archivo Principal
El archivo principal para esta prueba es `prueba_palindromo.py`. Dentro de este archivo encontrarás el diccionario de palabras.

Ejemplo de lista de palabras:

```python
palabras = ["oso", "casa", "radar", "sol", "reconocer", "luz", "anilina"]
```

## Casos de Prueba
Se deben implementar pruebas unitarias con `unittest` o `pytest` para validar el correcto funcionamiento del código.

Ejemplo de prueba esperada en `test.py`:

```python
import unittest
from prueba_palindromo import obtener_palindromos

class TestPalindromos(unittest.TestCase):
    def test_palindromos(self):
        palabras = ["oso", "casa", "radar", "sol", "reconocer", "luz", "anilina"]
        self.assertEqual(obtener_palindromos(palabras), ["oso", "radar", "reconocer", "anilina"])

if __name__ == '__main__':
    unittest.main()
```

## Evaluación
El código será evaluado en base a:
* ✅ **Uso correcto de Programación Funcional.**
* ✅ **Uso de funciones puras y de orden superior.**
* ✅ **Código limpio y buenas prácticas.**
* ✅ **Pruebas unitarias que validen la funcionalidad.**

# Veamos qué tal dominamos la Programación Asíncrona🕐

## Objetivo
Evaluar el conocimiento y aplicación de **Programación Asíncrona** en Python.

Se evaluarán los siguientes aspectos:
* ✅ **Uso de `async` y `await`**
* ✅ **Manejo de `asyncio`**
* ✅ **Uso de tareas concurrentes (`asyncio.gather` o `asyncio.create_task`)**
* ✅ **Pruebas de integración**

## Descripción

Mario necesita un sistema que realice múltiples consultas a una API de manera eficiente sin bloquear la ejecución del programa. Debes desarrollar un programa en Python utilizando **Programación Asíncrona** que realice varias solicitudes a una API ficticia y procese los resultados de forma concurrente.

### 📌 **Requisitos de Implementación**
1. Implementar una función **asíncrona** que realice una solicitud HTTP a una API simulada.
2. Ejecutar múltiples solicitudes de forma **concurrente**.
3. Procesar y mostrar los resultados de las solicitudes.
4. Implementar pruebas de integración para validar la ejecución.

## Archivo Principal
El archivo principal para esta prueba es `prueba_asincronica.py`. Dentro de este archivo encontrarás una lista de URLs de ejemplo.

Ejemplo de URLs:

```python
urls = [
    "https://api.ejemplo.com/datos/1",
    "https://api.ejemplo.com/datos/2",
    "https://api.ejemplo.com/datos/3"
]
```

## Casos de Prueba
Se deben implementar pruebas unitarias con `pytest` o `unittest` para validar el correcto funcionamiento del código.

## Evaluación
El código será evaluado en base a:
* ✅ **Uso correcto de programación asíncrona (`async/await`).**
* ✅ **Uso de `asyncio` para ejecutar tareas concurrentes.**
* ✅ **Código limpio y buenas prácticas.**
* ✅ **Pruebas unitarias que validen la funcionalidad.**

# Veamos qué tal dominamos el Manejo de Archivos 🗂️

## Objetivo
Evaluar la capacidad de manipulación de archivos en Python, específicamente la lectura de archivos CSV y la conversión de datos a formato JSON.

Se evaluarán los siguientes aspectos:
* ✅ **Lectura y procesamiento de archivos CSV**
* ✅ **Conversión de datos a formato JSON**
* ✅ **Escritura de datos en un nuevo archivo**
* ✅ **Pruebas de integración**

## Descripción
Mario tiene un archivo de datos en formato CSV con información de usuarios y necesita transformarlo a un formato JSON para integrarlo con otro sistema. Tu tarea es desarrollar un programa en Python que realice esta conversión de manera eficiente.

El archivo CSV de entrada (`usuarios.csv`) tiene el siguiente formato:

```csv
id,nombre,edad,email
1,Mario,30,mario@example.com
2,Ana,25,ana@example.com
3,Luis,40,luis@example.com
```

### 📌 **Requisitos de Implementación**
1. Implementar una función que lea los datos de un archivo CSV.
2. Convertir los datos en una lista de diccionarios.
3. Guardar los datos convertidos en un archivo JSON (`usuarios.json`).
4. Implementar pruebas de integración para validar la conversión.

## 📂 Archivo Principal
El archivo principal para esta prueba es `convertir_csv_json.py`.

### 📌 **Ejemplo de Implementación**

```python
import csv
import json

def convertir_csv_a_json(archivo_csv, archivo_json):
    # ...

# Llamada a la función
convertir_csv_a_json("usuarios.csv", "usuarios.json")
```

## 🔍 Casos de Prueba
Se deben implementar pruebas unitarias para validar que:
- El archivo JSON se crea correctamente.
- Los datos en JSON son equivalentes a los del archivo CSV original.

Ejemplo de prueba esperada en `test.py`:

```python
import json
import unittest
from convertir_csv_json import convertir_csv_a_json

def test_conversion():
    convertir_csv_a_json("usuarios.csv", "usuarios.json")
        # ...
```

## 📌 Evaluación
El código será evaluado en base a:
* ✅ **Correcta manipulación de archivos**
* ✅ **Conversión adecuada de formatos**
* ✅ **Código limpio y buenas prácticas**
* ✅ **Pruebas unitarias funcionales**

# Probemos qué tan bien nos va optimizando el código 📈

## 🎯 Objetivo
Evaluar la capacidad de optimización y mejora del código en términos de rendimiento y buenas prácticas.

Se evaluarán los siguientes aspectos:
* ✅ **Optimización del rendimiento**
* ✅ **Uso adecuado de estructuras de datos**
* ✅ **Limpieza y mantenibilidad del código**
* ✅ **Pruebas unitarias para validar mejoras**

## 🔍 Descripción
Mario tiene una función en Python que procesa una lista de números y devuelve los valores únicos ordenados de menor a mayor. Sin embargo, el código actual es ineficiente y necesita ser optimizado.

Tu tarea es **mejorar el código** sin cambiar su funcionalidad.

El código original es el siguiente:

```python
def procesar_lista(numeros):
    lista_unicos = []
    for num in numeros:
        if num not in lista_unicos:
            lista_unicos.append(num)
    lista_unicos.sort()
    return lista_unicos

numeros = [5, 3, 8, 3, 1, 5, 2, 8, 1]
resultado = procesar_lista(numeros)
print(resultado)
```

## 📌 Tareas a realizar
1. **Optimizar el código** para que sea más eficiente en términos de tiempo de ejecución.
2. **Explicar** las mejoras aplicadas y el porqué de cada optimización.
3. **Implementar pruebas unitarias** para validar la funcionalidad del código optimizado.

## 📂 Archivo Principal
El código debe estar en un archivo llamado `optimizar_codigo.py`.

## 🔍 Casos de Prueba
Se deben implementar pruebas unitarias en `test.py` para validar:
- Que la función optimizada devuelve el mismo resultado que la original.
- Que el rendimiento ha mejorado.

Ejemplo de prueba esperada:

```python
import unittest
from optimizar_codigo import procesar_lista_optimizada

def test_procesar_lista():
    numeros = [5, 3, 8, 3, 1, 5, 2, 8, 1]
    assert procesar_lista_optimizada(numeros) == [1, 2, 3, 5, 8]
```

## 📌 Evaluación
El código será evaluado en base a:
* ✅ **Mejoras en eficiencia y rendimiento**
* ✅ **Explicación clara de las optimizaciones**
* ✅ **Pruebas unitarias correctamente implementadas**
* ✅ **Código limpio y modular**

# Ahora vamos con Estructuras de Datos 🏢

## 🎯 Objetivo
Evaluar el conocimiento en el uso de estructuras de datos y su correcta aplicación en escenarios prácticos.

Se evaluarán los siguientes aspectos:
* ✅ **Uso adecuado de estructuras de datos** (listas, diccionarios, conjuntos, colas, pilas, etc.)
* ✅ **Eficiencia en el manejo de datos**
* ✅ **Correcta implementación de algoritmos**
* ✅ **Pruebas unitarias para validar la solución**

## 🔍 Descripción
Mario necesita gestionar un sistema de pedidos en un restaurante, donde cada pedido tiene:
- **Número de orden**
- **Nombre del cliente**
- **Lista de productos pedidos**
- **Estado del pedido** (Pendiente, En preparación, Listo, Entregado)

Tu tarea es diseñar una estructura de datos eficiente para manejar estos pedidos y permitir las siguientes operaciones:

1. **Agregar un nuevo pedido**.
2. **Actualizar el estado de un pedido**.
3. **Listar todos los pedidos en orden de llegada**.
4. **Listar solo los pedidos pendientes**.
5. **Buscar un pedido por número de orden**.

## 📂 Archivo Principal
El código debe estar en un archivo llamado `gestionar_pedidos.py`.

### 📌 Requerimientos
- Utilizar una **estructura de datos adecuada** para almacenar y manejar los pedidos.
- Implementar las funciones necesarias para las operaciones mencionadas.
- Aplicar **buenas prácticas de programación**.
- Incluir pruebas unitarias en `test_pedidos.py`.

### 📌 Evaluación
El código será evaluado en base a:
* ✅ **Uso correcto de estructuras de datos**
* ✅ **Eficiencia en las operaciones**
* ✅ **Código limpio y modular**
* ✅ **Pruebas unitarias correctamente implementadas**

# Multi-threading vs. Multi-processing

## 🎯 Objetivo
Evaluar la comprensión y aplicación de concurrencia en Python, diferenciando entre **multi-threading** y **multi-processing**.

Se evaluarán los siguientes aspectos:
* ✅ **Uso correcto de hilos (threads) y procesos**
* ✅ **Diferencias entre `threading` y `multiprocessing`**
* ✅ **Implementación eficiente de tareas concurrentes**
* ✅ **Medición y comparación del rendimiento entre ambos enfoques**

## 🔍 Descripción
Mario está desarrollando un sistema que requiere ejecutar tareas concurrentes. Algunas tareas son **ligeras** y requieren compartir memoria, mientras que otras son **pesadas** y se benefician de múltiples núcleos de CPU.

Debes implementar un programa que realice las siguientes tareas en paralelo:

1. **Descarga de datos simulada** (I/O-bound) → Ideal para multi-threading
2. **Cálculo intensivo de números primos** (CPU-bound) → Ideal para multi-processing

El código debe demostrar el uso adecuado de `threading` y `multiprocessing`, comparando los tiempos de ejecución de ambas estrategias.

## 📂 Archivo Principal
El código debe estar en un archivo llamado `concurrencia.py`.

### 📌 Requerimientos
- Implementar dos funciones:
  1. `descargar_datos()`: Simular una descarga de datos con `time.sleep()`.
  2. `calcular_primos(n)`: Encontrar todos los números primos hasta `n`.
- Crear versiones de cada tarea utilizando `threading` y `multiprocessing`.
- Comparar el rendimiento y mostrar los tiempos de ejecución.
- Explicar en `README.md` cuándo usar `threading` vs. `multiprocessing`.

### 🔍 Ejemplo de Uso
```python
if __name__ == "__main__":
    ejecutar_con_threads()
    ejecutar_con_procesos()
```

### 📌 Evaluación
El código será evaluado en base a:
* ✅ **Uso correcto de `threading` y `multiprocessing`**
* ✅ **Estructura clara y modular**
* ✅ **Comparación del rendimiento de ambas técnicas**
* ✅ **Explicación en `README.md`**

# Desarrollando una API REST 🚀

## 🎯 Objetivo
Evaluar la capacidad de diseñar e implementar una API REST utilizando Python y un framework web.

Se evaluarán los siguientes aspectos:
* ✅ **Estructura y modularidad del código**
* ✅ **Uso de un framework web FastAPI**
* ✅ **Implementación de endpoints CRUD**
* ✅ **Uso de validaciones y manejo de errores**
* ✅ **Documentación de la API**

## 🔍 Descripción
Mario necesita una API para gestionar usuarios. Tu tarea es desarrollar una API RESTful que permita realizar operaciones CRUD sobre usuarios.

## 📂 Archivo Principal
El código debe estar en un archivo llamado `api.py`.

### 📌 Requerimientos
- Usar **FastAPI** para la implementación.
- Crear un modelo `Usuario` con los atributos:
  - `id`: Identificador único (autoincremental)
  - `nombre`: Nombre del usuario
  - `email`: Correo electrónico
  - `edad`: Edad del usuario
- Implementar los siguientes endpoints:
  1. `GET /usuarios` → Obtener la lista de usuarios.
  2. `POST /usuarios` → Crear un nuevo usuario.
  3. `GET /usuarios/{id}` → Obtener un usuario por ID.
  4. `PUT /usuarios/{id}` → Actualizar un usuario por ID.
  5. `DELETE /usuarios/{id}` → Eliminar un usuario por ID.
- Validar los datos de entrada (por ejemplo, que el email tenga formato válido y que la edad sea un número positivo).
- Manejo de errores y respuestas con códigos HTTP adecuados.
- Documentar la API con Swagger

### 🔍 Ejemplo de Uso
#### Crear un usuario
```json
POST /usuarios
{
  "nombre": "Mario",
  "email": "mario@email.com",
  "edad": 30
}
```

#### Respuesta esperada:
```json
{
  "id": 1,
  "nombre": "Mario",
  "email": "mario@email.com",
  "edad": 30
}
```

### 📌 Evaluación
El código será evaluado en base a:
* ✅ **Correcta implementación de endpoints RESTful**
* ✅ **Validaciones y manejo de errores**
* ✅ **Documentación de la API**
* ✅ **Código limpio y estructurado**