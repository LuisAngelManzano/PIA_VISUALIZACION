import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.uic import loadUi
import sqlite3


class jhon(QMainWindow):
  
    def __init__(self):
        super(jhon, self).__init__()
        loadUi('PaginaJhonWick.ui', self)
        self.mostrar_mensajes_desde_bd()

    def obtener_mensajes_desde_bd(self):
        conexion = sqlite3.connect('informacion_datos.db')
        cursor = conexion.cursor()

        cursor.execute("SELECT nombre, comentario FROM reseña WHERE id = 11")
        resultados = cursor.fetchall()
        conexion.commit()
        conexion.close()

        if resultados:
            mensajes = [f"{resultado[0]}: {resultado[1]}" for resultado in resultados]
            return mensajes
        else:
            print("No se encontraron mensajes en la base de datos.")
            return []

    def mostrar_mensajes_desde_bd(self):
        mensajes = self.obtener_mensajes_desde_bd()

        if mensajes:
            textEdit = self.findChild(QTextEdit, 'agregaUnComentario')
            if textEdit is not None:
                text = "\n".join(mensajes)
                textEdit.setText(text)
            else:
                print("No se encontró el QTextEdit en la interfaz.")

 



def ejecutar_aplicacion():
    app = QApplication(sys.argv)
    ventana = jhon()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
  
  ejecutar_aplicacion()
