import time

# Función para cargar nombres desde un archivo
def cargar_desde_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            return [linea.strip() for linea in archivo.readlines()]
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
        return []

# Función para guardar nombres ordenados en un archivo
def guardar_en_archivo(nombres_ordenados, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for nombre in nombres_ordenados:
            archivo.write(f'{nombre}\n')
    print(f"Las cadenas ordenadas se han guardado en '{nombre_archivo}'")

# Función de ordenamiento burbuja
def burbuja(arr, ascendente=True):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if (ascendente and arr[j] > arr[j+1]) or (not ascendente and arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Función para contar cuántas veces se repite cada nombre
def contar_repeticiones(nombres):
    repeticiones = {}
    for nombre in nombres:
        if nombre in repeticiones:
            repeticiones[nombre] += 1
        else:
            repeticiones[nombre] = 1
    return repeticiones

# Función principal
def main():
    print("1. Cargar cadenas desde un archivo")
    print("2. Ingresar cadenas manualmente")
    opcion = input("Seleccione una opción: ").strip()

    # Lista para almacenar las cadenas
    strings = []

    if opcion == "1":
        archivo_entrada = input("Ingrese el nombre del archivo desde el cual cargar las cadenas: ").strip()
        strings = cargar_desde_archivo(archivo_entrada)
        if not strings:
            return  # Termina el programa si no se pueden cargar cadenas
    elif opcion == "2":
        print("Ingresa las cadenas una por una. Deja en blanco para terminar.")
        while True:
            cadena = input("Cadena: ").strip()
            if cadena == "":
                break
            strings.append(cadena)
    else:
        print("Opción no válida.")
        return

    if not strings:
        print("No se han ingresado cadenas.")
        return

    print("\nSeleccione el tipo de orden:")
    print("1. Ascendente")
    print("2. Descendente")
    tipo_orden = input("Ingrese 1 para ascendente o 2 para descendente: ").strip()

    if tipo_orden == "1":
        ascendente = True
    elif tipo_orden == "2":
        ascendente = False
    else:
        print("Opción no válida.")
        return

    # Medir el tiempo de ejecución del ordenamiento
    inicio_tiempo = time.time()
    burbuja(strings, ascendente=ascendente)
    fin_tiempo = time.time()

    # Mostrar cadenas ordenadas
    print("\nCadenas ordenadas:")
    for string in strings:
        print(f'ORDEN: {string}')

    # Guardar cadenas en archivo
    archivo_salida = input("Ingrese el nombre del archivo donde guardar las cadenas ordenadas: ").strip()
    guardar_en_archivo(strings, archivo_salida)

    # Mostrar tiempo de ejecución
    tiempo_ejecucion = fin_tiempo - inicio_tiempo
    print(f"\nTiempo de ejecución del ordenamiento: {tiempo_ejecucion:.6f} segundos")

    # Mostrar cuántas veces se repite cada cadena
    repeticiones = contar_repeticiones(strings)
    print("\nRepeticiones de nombres:")
    for nombre, cantidad in repeticiones.items():
        if cantidad > 1:
            print(f"{nombre}: {cantidad} veces")

if __name__ == "__main__":
    main()
