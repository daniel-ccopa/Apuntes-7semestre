import tkinter as tk
from tkinter import filedialog, messagebox
import time

# Función para cargar nombres desde un archivo
def cargar_desde_archivo():
    nombre_archivo = filedialog.askopenfilename(title="Seleccionar archivo de entrada", filetypes=[("Text Files", "*.txt")])
    if nombre_archivo:
        try:
            with open(nombre_archivo, 'r') as archivo:
                return [linea.strip() for linea in archivo.readlines()]
        except FileNotFoundError:
            messagebox.showerror("Error", f"El archivo '{nombre_archivo}' no existe.")
    return []

# Función para guardar nombres ordenados en un archivo
def guardar_en_archivo(nombres_ordenados):
    nombre_archivo = filedialog.asksaveasfilename(title="Guardar archivo", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if nombre_archivo:
        with open(nombre_archivo, 'w') as archivo:
            for nombre in nombres_ordenados:
                archivo.write(f'{nombre}\n')
        messagebox.showinfo("Guardado", f"Las cadenas ordenadas se han guardado en '{nombre_archivo}'")

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

# Función para agregar cadenas manualmente
def agregar_cadena_manual():
    cadena = entry.get().strip()
    if cadena:
        cadenas.append(cadena)
        actualizar_lista()
        entry.delete(0, tk.END)

# Función para actualizar la lista de cadenas en la interfaz
def actualizar_lista():
    listbox.delete(0, tk.END)
    for cadena in cadenas:
        listbox.insert(tk.END, cadena)

# Función para ordenar las cadenas
def ordenar_cadenas():
    if not cadenas:
        messagebox.showerror("Error", "No hay cadenas para ordenar.")
        return
    
    # Preguntar si se quiere ordenar en orden ascendente o descendente
    tipo_orden = messagebox.askyesno("Ordenar", "¿Deseas ordenar en orden ascendente?")
    ascendente = tipo_orden
    
    # Medir el tiempo de ejecución
    inicio_tiempo = time.time()
    burbuja(cadenas, ascendente=ascendente)
    fin_tiempo = time.time()
    
    # Actualizar la lista ordenada
    actualizar_lista()

    # Mostrar tiempo de ejecución
    tiempo_ejecucion = fin_tiempo - inicio_tiempo
    messagebox.showinfo("Tiempo de ejecución", f"Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos")

    # Mostrar repeticiones de nombres
    repeticiones = contar_repeticiones(cadenas)
    repetidos = "\n".join([f"{nombre}: {cantidad} veces" for nombre, cantidad in repeticiones.items() if cantidad > 1])
    if repetidos:
        messagebox.showinfo("Repeticiones", f"Repeticiones encontradas:\n{repetidos}")
    else:
        messagebox.showinfo("Repeticiones", "No hay repeticiones.")

# Función para cargar un archivo con cadenas
def cargar_archivo():
    global cadenas
    cadenas = cargar_desde_archivo()
    actualizar_lista()

# Función para guardar las cadenas ordenadas
def guardar_archivo():
    if not cadenas:
        messagebox.showerror("Error", "No hay cadenas para guardar.")
        return
    guardar_en_archivo(cadenas)

# Función principal de la interfaz
def main():
    global root, listbox, entry, cadenas
    cadenas = []

    # Crear ventana principal
    root = tk.Tk()
    root.title("Ordenar Cadenas")
    root.geometry("500x400")

    # Etiquetas y botones
    label = tk.Label(root, text="Selecciona una opción:")
    label.pack(pady=10)

    # Botones de carga, guardar, y ordenar
    load_button = tk.Button(root, text="Cargar cadenas desde archivo", command=cargar_archivo)
    load_button.pack(pady=5)

    manual_input_button = tk.Button(root, text="Agregar cadenas manualmente", command=agregar_cadena_manual)
    manual_input_button.pack(pady=5)

    sort_button = tk.Button(root, text="Ordenar cadenas", command=ordenar_cadenas)
    sort_button.pack(pady=5)

    save_button = tk.Button(root, text="Guardar cadenas ordenadas", command=guardar_archivo)
    save_button.pack(pady=5)

    # Lista para mostrar cadenas ingresadas
    listbox = tk.Listbox(root, height=10, width=50)
    listbox.pack(pady=10)

    # Campo de texto para ingresar manualmente
    entry = tk.Entry(root, width=40)
    entry.pack(pady=5)

    # Ejecutar la ventana
    root.mainloop()

if __name__ == "__main__":
    main()
