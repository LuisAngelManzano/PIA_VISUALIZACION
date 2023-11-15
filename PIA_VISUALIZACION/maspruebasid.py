import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QTextEdit, QVBoxLayout, QPushButton
from PyQt5.uic import loadUi
import sqlite3

class MiVentana(QMainWindow):
    def __init__(self):
        super(MiVentana, self).__init__()
        loadUi('interfaz.ui', self)  # Asegúrate de cambiar 'interfaz.ui' al nombre de tu archivo UI.

        # Cargar todas las páginas de antemano
        self.stackedWidget = QVBoxLayout(self)
        self.setCentralWidget(self.stackedWidget)

        self.paginas = {
            "Siniestro": "PaginaFenomenoSiniestro.ui",
            "Saw": "PaginaSawX.ui",
            "Guerra Mundial Z": "PaginaGuerraMundialZ.ui",
            # Agrega el resto de las páginas según tu interfaz y nombres de los botones
        }

        self.botones = []
        for nombre, pagina in self.paginas.items():
            boton = QRadioButton(nombre)
            boton.clicked.connect(lambda _, p=pagina: self.mostrar_pagina(p))
            self.botones.append(boton)
            self.stackedWidget.addWidget(boton)

        self.conexion_db = sqlite3.connect('informacion_datos.db')  # Conectar con la base de datos
        self.cursor = self.conexion_db.cursor()

    def mostrar_pagina(self, pagina):
        loadUi(pagina, self)
        
        # Realiza aquí las operaciones necesarias relacionadas con la página o su carga desde la base de datos
        # Por ejemplo, ejecutar consultas en la base de datos para llenar la página con información.

    def closeEvent(self, event):
        self.conexion_db.close()  # Cierra la conexión con la base de datos al cerrar la ventana

def ejecutar_aplicacion():
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    ejecutar_aplicacion()
