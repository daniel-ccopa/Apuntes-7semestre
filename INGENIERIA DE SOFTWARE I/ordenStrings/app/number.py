def cargar_numeros_desde_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            numeros = []
            for linea in archivo:
                try:
                    numero = float(linea.strip())
                    numeros.append(numero)
                except ValueError:
                    print(f"Advertencia: '{linea.strip()}' no es un número válido y será ignorado.")
            return numeros
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no existe.")
        return []

def guardar_numeros_en_archivo(numeros, ruta_archivo):
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        for numero in numeros:
            archivo.write(f'{numero}\n')
    print(f"Números guardados en '{ruta_archivo}'.")

def ordenar_numeros(numeros, ascendente=True):
    return sorted(numeros, reverse=not ascendente)

def visualizar_numeros(numeros):
    for numero in numeros:
        print(numero)

def main():
    print("=== Programa para Ordenar Números ===\n")
    ruta_archivo = input("Ingresa la ruta del archivo a cargar: ")
    numeros = cargar_numeros_desde_archivo(ruta_archivo)
    
    if not numeros:
        print("No se cargaron números. Finalizando el programa.")
        return
    
    print("\nNúmeros cargados:")
    visualizar_numeros(numeros)
    
    orden = input("\n¿Deseas ordenar en forma ascendente (A) o descendente (D)? [A/D]: ").strip().upper()
    ascendente = True if orden == 'A' else False
    numeros_ordenados = ordenar_numeros(numeros, ascendente=ascendente)
    
    print("\nNúmeros ordenados:")
    visualizar_numeros(numeros_ordenados)
    
    ruta_archivo_salida = input("\nIngresa la ruta del archivo para guardar los números ordenados: ")
    guardar_numeros_en_archivo(numeros_ordenados, ruta_archivo_salida)
    
    print("\nProceso completado.")

if __name__ == "__main__":
    main()
