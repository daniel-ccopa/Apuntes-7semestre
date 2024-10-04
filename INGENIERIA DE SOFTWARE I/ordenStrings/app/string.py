def cargar_cadenas_desde_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return [linea.strip() for linea in archivo.readlines()]
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no existe.")
        return []

def guardar_cadenas_en_archivo(cadenas, ruta_archivo):
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        for cadena in cadenas:
            archivo.write(f'{cadena}\n')
    print(f"Cadenas guardadas en '{ruta_archivo}'.")

def ordenar_cadenas(cadenas, ascendente=True):
    return sorted(cadenas, reverse=not ascendente)

def visualizar_cadenas(cadenas):
    for cadena in cadenas:
        print(cadena)

def main():
    print("=== Programa para Ordenar Cadenas ===\n")
    ruta_archivo = input("Ingresa la ruta del archivo a cargar: ")
    cadenas = cargar_cadenas_desde_archivo(ruta_archivo)
    
    if not cadenas:
        print("No se cargaron cadenas. Finalizando el programa.")
        return
    
    print("\nCadenas cargadas:")
    visualizar_cadenas(cadenas)
    
    orden = input("\n¿Deseas ordenar en forma ascendente (A) o descendente (D)? [A/D]: ").strip().upper()
    ascendente = True if orden == 'A' else False
    cadenas_ordenadas = ordenar_cadenas(cadenas, ascendente=ascendente)
    
    print("\nCadenas ordenadas:")
    visualizar_cadenas(cadenas_ordenadas)
    
    ruta_archivo_salida = input("\nIngresa la ruta del archivo para guardar las cadenas ordenadas: ")
    guardar_cadenas_en_archivo(cadenas_ordenadas, ruta_archivo_salida)
    
    print("\nProceso completado.")

if __name__ == "__main__":
    main()
