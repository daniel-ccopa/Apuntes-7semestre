import time
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

def contar_repeticiones(nombres):
    return {nombre: nombres.count(nombre) for nombre in set(nombres)}

def main():
    opcion = input("1. Cargar desde archivo\n2. Ingresar manualmente\nSeleccione una opción: ").strip()
    if opcion == "1":
        strings = cargar_desde_archivo(input("Archivo: ").strip())
    elif opcion == "2":
        strings = []
        print("Ingresa las cadenas una por una. Deja en blanco para terminar.")
        while True:
            cadena = input("Cadena: ").strip()
            if not cadena:
                break
            strings.append(cadena)
    else:
        return print("Opción no válida.")
    
    if not strings: return print("No se han ingresado cadenas.")

    ascendente = input("1. Ascendente\n2. Descendente\nIngrese 1 para ascendente o 2 para descendente: ").strip() == "1"
    inicio_tiempo = time.time()
    
    strings.sort(reverse=not ascendente)

    print(f"\nCadenas ordenadas:\n" + "\n".join(strings))
    guardar_en_archivo(strings, input("Archivo de salida: ").strip())
    print(f"Tiempo de ejecución: {time.time() - inicio_tiempo:.6f} segundos")
    
    repeticiones = contar_repeticiones(strings)
    print("\nRepeticiones:\n" + "\n".join(f"{nombre}: {cantidad} veces" for nombre, cantidad in repeticiones.items() if cantidad > 1))

if __name__ == "__main__":
    main()