import time
import threading
import multiprocessing

def descargar_datos():
    print("Descargando datos...")
    time.sleep(2)  # Simula una espera por I/O
    print("Descarga completada")

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def calcular_primos(limite):
    print(f"Calculando primos hasta {limite}...")
    primos = [n for n in range(limite) if es_primo(n)]
    print(f"Cálculo completado. Se encontraron {len(primos)} primos.")

def ejecutar_con_threads():
    inicio = time.time()
    hilo1 = threading.Thread(target=descargar_datos)
    hilo2 = threading.Thread(target=calcular_primos, args=(50000,))
    
    hilo1.start()
    hilo2.start()
    
    hilo1.join()
    hilo2.join()
    fin = time.time()
    print(f"Tiempo con threading: {fin - inicio:.2f} segundos")

def ejecutar_con_procesos():
    inicio = time.time()
    proceso1 = multiprocessing.Process(target=descargar_datos)
    proceso2 = multiprocessing.Process(target=calcular_primos, args=(50000,))
    
    proceso1.start()
    proceso2.start()
    
    proceso1.join()
    proceso2.join()
    fin = time.time()
    print(f"Tiempo con multiprocessing: {fin - inicio:.2f} segundos")

if __name__ == "__main__":
    ejecutar_con_threads()
    ejecutar_con_procesos()
