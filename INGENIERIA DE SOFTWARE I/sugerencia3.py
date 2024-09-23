import os
import time

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def cargar_desde_archivo(nombre_archivo):
    try:
        return [linea.strip() for linea in open(nombre_archivo, 'r').readlines()]
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
        return []

def guardar_en_archivo(nombres_ordenados, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        archivo.writelines(f'{nombre}\n' for nombre in nombres_ordenados)
    print(f"Cadenas guardadas en '{nombre_archivo}'")

def burbuja(arr, ascendente=True):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if (ascendente and arr[j] > arr[j+1]) or (not ascendente and arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

def contar_repeticiones(nombres):
    return {nombre: nombres.count(nombre) for nombre in set(nombres)}

def main():
    limpiar_pantalla()
    opcion = input("1. Cargar desde archivo\n2. Ingresar manualmente\nSeleccione una opción: ").strip()
    strings = cargar_desde_archivo(input("Archivo: ").strip()) if opcion == "1" else [cadena for cadena in iter(lambda: input("Cadena: ").strip(), "")] if opcion == "2" else print("Opción no válida.") or exit()
    
    if not strings: return print("No se han ingresado cadenas.")

    ascendente = input("1. Ascendente\n2. Descendente\nIngrese 1 para ascendente o 2 para descendente: ").strip() == "1"
    inicio_tiempo = time.time()
    burbuja(strings, ascendente)
    
    limpiar_pantalla()
    print(f"\nCadenas ordenadas:\n" + "\n".join(strings))
    
    guardar_en_archivo(strings, input("Archivo de salida: ").strip())
    print(f"Tiempo de ejecución: {time.time() - inicio_tiempo:.6f} segundos")
    
    repeticiones = contar_repeticiones(strings)
    print("\nRepeticiones:\n" + "\n".join(f"{nombre}: {cantidad} veces" for nombre, cantidad in repeticiones.items() if cantidad > 1))

if __name__ == "__main__":
    main()
