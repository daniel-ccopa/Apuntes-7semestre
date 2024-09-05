import tkinter as tk
from tkinter import messagebox


class OrdenarCadenasApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.title("Ordenar Cadenas")
        self.geometry("400x300")

        # Lista para almacenar las cadenas
        self.cadenas = []

        # Crear widgets de la interfaz
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta para instrucciones
        self.label = tk.Label(self, text="Ingresa una cadena y presiona Enter:")
        self.label.pack(pady=10)

        # Campo de texto para ingresar cadenas
        self.text_input = tk.Entry(self)
        self.text_input.pack(pady=5)
        self.text_input.bind("<Return>", self.agregar_cadena)  # Conectar el "Enter" a la función

        # Botón para agregar la cadena
        self.add_button = tk.Button(self, text="Agregar cadena", command=self.agregar_cadena)
        self.add_button.pack(pady=5)

        # Botón para ordenar las cadenas
        self.sort_button = tk.Button(self, text="Ordenar cadenas", command=self.ordenar_cadenas)
        self.sort_button.pack(pady=5)

        # Lista para mostrar las cadenas ingresadas
        self.listbox = tk.Listbox(self)
        self.listbox.pack(pady=10, fill=tk.BOTH, expand=True)

    def agregar_cadena(self, event=None):
        # Obtener la cadena ingresada
        cadena = self.text_input.get().strip()

        if cadena:
            # Agregar la cadena a la lista y al Listbox
            self.cadenas.append(cadena)
            self.listbox.insert(tk.END, cadena)
            self.text_input.delete(0, tk.END)  # Limpiar el campo de texto
        else:
            messagebox.showwarning("Advertencia", "No se puede agregar una cadena vacía")

    def ordenar_cadenas(self):
        # Implementar el algoritmo de burbuja para ordenar las cadenas
        def burbuja(arr):
            n = len(arr)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]

        # Ordenar las cadenas usando el algoritmo de burbuja
        burbuja(self.cadenas)

        # Limpiar el Listbox y mostrar las cadenas ordenadas
        self.listbox.delete(0, tk.END)
        for cadena in self.cadenas:
            self.listbox.insert(tk.END, f"ORDEN: {cadena}")


if __name__ == "__main__":
    # Crear y ejecutar la aplicación
    app = OrdenarCadenasApp()
    app.mainloop()