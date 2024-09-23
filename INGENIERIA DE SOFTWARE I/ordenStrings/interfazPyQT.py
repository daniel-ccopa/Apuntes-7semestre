import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QFileDialog, QLineEdit, QMessageBox

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

# Clase principal de la interfaz
class OrdenarCadenasApp(QWidget):
    def __init__(self):
        super().__init__()
        self.cadenas = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Ordenar Cadenas")
        self.setGeometry(100, 100, 500, 400)

        # Layout
        layout = QVBoxLayout()

        # Etiqueta de instrucciones
        self.label = QLabel("Selecciona una opción:")
        layout.addWidget(self.label)

        # Botones de cargar, guardar y ordenar
        self.load_button = QPushButton("Cargar cadenas desde archivo", self)
        self.load_button.clicked.connect(self.cargar_archivo)
        layout.addWidget(self.load_button)

        self.manual_input_button = QPushButton("Agregar cadenas manualmente", self)
        self.manual_input_button.clicked.connect(self.agregar_cadena_manual)
        layout.addWidget(self.manual_input_button)

        self.sort_button = QPushButton("Ordenar cadenas", self)
        self.sort_button.clicked.connect(self.ordenar_cadenas)
        layout.addWidget(self.sort_button)

        self.save_button = QPushButton("Guardar cadenas ordenadas", self)
        self.save_button.clicked.connect(self.guardar_archivo)
        layout.addWidget(self.save_button)

        # Lista para mostrar cadenas
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        # Campo de texto para ingresar manualmente
        self.text_input = QLineEdit(self)
        layout.addWidget(self.text_input)

        # Configurar el layout
        self.setLayout(layout)

    def cargar_archivo(self):
        archivo_entrada, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo de entrada", "", "Text Files (*.txt);;All Files (*)")
        if archivo_entrada:
            self.cadenas = cargar_desde_archivo(archivo_entrada)
            self.actualizar_lista()

    def agregar_cadena_manual(self):
        cadena = self.text_input.text().strip()
        if cadena:
            self.cadenas.append(cadena)
            self.actualizar_lista()
            self.text_input.clear()

    def actualizar_lista(self):
        self.list_widget.clear()
        for cadena in self.cadenas:
            self.list_widget.addItem(cadena)

    def ordenar_cadenas(self):
        if not self.cadenas:
            QMessageBox.warning(self, "Error", "No hay cadenas para ordenar.")
            return

        # Preguntar si se quiere ordenar en orden ascendente o descendente
        tipo_orden = QMessageBox.question(self, "Ordenar", "¿Deseas ordenar en orden ascendente?",
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        ascendente = True if tipo_orden == QMessageBox.Yes else False

        # Medir el tiempo de ejecución
        inicio_tiempo = time.time()
        burbuja(self.cadenas, ascendente=ascendente)
        fin_tiempo = time.time()

        # Actualizar la lista ordenada
        self.actualizar_lista()

        # Mostrar tiempo de ejecución
        tiempo_ejecucion = fin_tiempo - inicio_tiempo
        QMessageBox.information(self, "Tiempo de ejecución", f"Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos")

        # Mostrar repeticiones de nombres
        repeticiones = contar_repeticiones(self.cadenas)
        repetidos = "\n".join([f"{nombre}: {cantidad} veces" for nombre, cantidad in repeticiones.items() if cantidad > 1])
        if repetidos:
            QMessageBox.information(self, "Repeticiones", f"Repeticiones encontradas:\n{repetidos}")
        else:
            QMessageBox.information(self, "Repeticiones", "No hay repeticiones.")

    def guardar_archivo(self):
        if not self.cadenas:
            QMessageBox.warning(self, "Error", "No hay cadenas para guardar.")
            return
        archivo_salida, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Text Files (*.txt);;All Files (*)")
        if archivo_salida:
            guardar_en_archivo(self.cadenas, archivo_salida)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = OrdenarCadenasApp()
    ventana.show()
    sys.exit(app.exec_())
