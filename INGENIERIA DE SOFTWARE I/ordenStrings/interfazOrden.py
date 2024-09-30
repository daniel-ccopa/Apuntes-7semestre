import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget

class OrdenarCadenasApp(QWidget):
    def __init__(self):
        super().__init__()

        # Inicializar los componentes de la interfaz
        self.initUI()

    def initUI(self):
        # Configuración de la ventana
        self.setWindowTitle("Ordenar Cadenas")
        self.setGeometry(100, 100, 400, 300)

        # Crear un layout vertical
        layout = QVBoxLayout()

        # Etiqueta para las instrucciones
        self.label = QLabel("Ingresa una cadena y presiona Enter:")
        layout.addWidget(self.label)

        # Campo de texto para ingresar cadenas
        self.text_input = QLineEdit(self)
        layout.addWidget(self.text_input)

        # Botón para agregar la cadena a la lista
        self.add_button = QPushButton("Agregar cadena", self)
        layout.addWidget(self.add_button)

        # Botón para ordenar las cadenas
        self.sort_button = QPushButton("Ordenar cadenas", self)
        layout.addWidget(self.sort_button)

        # Lista para mostrar las cadenas ingresadas
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        # Etiqueta para mostrar el resultado de las cadenas ordenadas
        self.result_label = QLabel("Cadenas ordenadas:")
        layout.addWidget(self.result_label)

        # Conectar el botón de agregar al método que maneja el evento
        self.add_button.clicked.connect(self.agregar_cadena)
        # Conectar el botón de ordenar al método que maneja la ordenación
        self.sort_button.clicked.connect(self.ordenar_cadenas)

        # Conectar el evento "Enter" del campo de texto para agregar la cadena
        self.text_input.returnPressed.connect(self.agregar_cadena)

        # Establecer el layout en la ventana principal
        self.setLayout(layout)

        # Lista para almacenar las cadenas ingresadas
        self.cadenas = []

    def agregar_cadena(self):
        # Obtener la cadena ingresada
        cadena = self.text_input.text().strip()

        if cadena != "":
            # Agregar la cadena a la lista interna y al widget de la lista
            self.cadenas.append(cadena)
            self.list_widget.addItem(cadena)
            self.text_input.clear()

    def ordenar_cadenas(self):
        # Implementar el algoritmo de burbuja para ordenar las cadenas
        def burbuja(arr):
            n = len(arr)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]

        # Ordenar las cadenas
        burbuja(self.cadenas)

        # Limpiar la lista visible en la interfaz
        self.list_widget.clear()

        # Mostrar las cadenas ordenadas en la lista visible
        for cadena in self.cadenas:
            self.list_widget.addItem(f'ORDEN: {cadena}')


if __name__ == '__main__':
    # Crear la aplicación PyQt
    app = QApplication(sys.argv)
    
    # Crear la ventana principal
    ventana = OrdenarCadenasApp()
    
    # Mostrar la ventana
    ventana.show()

    # Ejecutar el ciclo de eventos
    sys.exit(app.exec_())
