import sys
from PyQt5 import QtWidgets, uic
from messagebox import msg_about, msg_error
import sqlite3 
from ventanas import MiVentana
from pruebasid import MisVentana
from paginaBarbie import Barbie
from paginabluee import Bluee
from paginajhon import jhon
from paginaspider import spider

#iniciar la aplicacion
app = QtWidgets.QApplication([])


#cargar achivos. ui,

login = uic.loadUi("entrada.ui")
registro = uic.loadUi("registro.ui")
interfaz = uic.loadUi("interfaz.ui")

reseña = uic.loadUi("reseña.ui")
ventana_personalizada = MiVentana() 
ventana2 = MisVentana()
ventana3 = Barbie()
ventana4 = Bluee()
ventana5 = jhon()
ventana6 = spider()
try:
    con = sqlite3.connect("informacion_datos.db")
    con.commit()
    con.close()
except:
    print("Error en la bade de datos...")


    
def gui_login():
    name = login.lineEdit.text()
    password = login.lineEdit_2.text()

    if len(name)==0 or len(password)==0:
        login.label_2.setText("Ingrese todos los datos")
    else: 
        con = sqlite3.connect("informacion_datos.db")
        cursor = con.cursor()
        cursor.execute("SELECT nombre, contraseña FROM user WHERE nombre= ? AND  contraseña = ?",(name, password))
        if cursor.fetchall():
            gui_interfaz()
        else:
            msg_error("Error","El usuario o contraseña no son correctos")
def crear_tabla():
    con = sqlite3.connect("informacion_datos.db")
    cursor = con.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS user(
        nombre text,
        apellido_paterno text,
        apellido_materno text,
        edad integer,
        sexo text,
        celular integer,
        correo text,
        contraseña text 
        )"""

    ) 
    con.commit()
    con.close()
    

def registrar(nombre, ap, am, edad, sex, cel, mail, contraseña):
    con = sqlite3.connect("informacion_datos.db")
    cursor = con.cursor()
    instruccion = f"INSERT INTO user VALUES ('{nombre}', '{ap}', '{am}'," \
                  f"'{edad}', '{sex}', '{cel}', '{mail}', '{contraseña}')"
    cursor.execute(instruccion)
    con.commit()
    con.close()
def reseña_ingreso (id,nombre,puntuacion,comentario):
    con = sqlite3.connect("informacion_datos.db")
    cursor = con.cursor()
    instruccion = f"INSERT INTO reseña VALUES ('{id}','{nombre}', '{puntuacion}', '{comentario}')"
    cursor.execute(instruccion)
    con.commit()
    con.close()

    
def datos():
    nombre = registro.lineEdit.text()
    apellido_p = registro.lineEdit_2.text()
    apellido_m = registro.lineEdit_3.text()
    edad = int(registro.lineEdit_4.text())
    box = str(registro.comboBox.currentText())
    celular = int(registro.lineEdit_5.text())
    correo = registro.lineEdit_6.text()
    contraseña = registro.lineEdit_7.text()
    contraseña_2 = registro.lineEdit_8.text()
    if contraseña != contraseña_2:
        msg_error("Error", "Las contraseñas no son iguales...")
    elif len(str(celular)) != 10:
        msg_error("Error", "El número de celular debe contener 10 dígitos")
    elif contraseña == contraseña_2:
        registrar(nombre, apellido_p, apellido_m, edad, box, celular, correo, contraseña)
        msg_about("Éxito!", "Se ha registrado exitosamente! \n Tu nombre es tu usuario")
        registro.lineEdit.setText("") #nombre
        registro.lineEdit_2.setText("") # app
        registro.lineEdit_3.setText("") #apm
        registro.lineEdit_4.setText("") #edad
        registro.lineEdit_5.setText("") #cel
        registro.lineEdit_6.setText("") #email
        registro.lineEdit_7.setText("") #contraseña
        registro.lineEdit_8.setText("") #contraseña2
def mostrar_reseña():
    id = reseña.id.text()
    nombre = reseña.nombre_resea.text()
    puntuacion = int(reseña.puntuacion_resena.text())
    comentario = reseña.comentario_resena.text()

    if nombre.strip()== " ":
        msg_error("Error","No se ingreseo ningun usuario")
    elif comentario.strip() == "":
        msg_error("Error","No se ingreseo ningun comentario")
    else:
        reseña_ingreso(id,nombre,puntuacion,comentario)
        msg_about("Éxito!", "Se ha registrado exitosamente! \n Tu reseña")
        reseña.id.setText("")
        reseña.nombre_resea.setText("")
        reseña.puntuacion_resena.setText("")
        reseña.comentario_resena.setText("")
       
       
#interfaz de la aplicacion
def gui_resena():
    ventana_personalizada.hide()
    ventana2.hide()
    ventana3.hide()
    ventana4.hide()
    ventana5.hide()
    reseña.show()
def gui_interfaz():
    login.hide()
    registro.hide()
    ventana_personalizada.hide()
    ventana2.hide()
    ventana3.hide()
    ventana4.hide()
    ventana5.hide()
    reseña.hide()
    interfaz.show()

#interfaz de registro en la app
def gui_registro():
    login.hide()
    registro.show()
    crear_tabla()

#salir de la apps
def salir():
    login.hide()
    registro.hide()
    interfaz.hide()
    app.exec()

def regresar_forma():
    registro.hide()
    interfaz.hide()
    login.show()

def siniestro1():
    interfaz.hide()
    ventana_personalizada.show() 

def peliculasaw():
    interfaz.hide()
    ventana2.show()    
def peliculabarbie():
    interfaz.hide()
    ventana3.show()
def paginabluee():
    interfaz.hide()
    ventana4.show()

def paginajhonw():
    interfaz.hide()
    ventana5.show()
def paginaspider():
    interfaz.hide()
    ventana6.show()

#
def actualizar_resena(id, nombre, puntuacion, comentario):
    con = sqlite3.connect("informacion_datos.db")
    cursor = con.cursor()
    # Verificar si la reseña ya existe en la base de datos
    cursor.execute("SELECT * FROM reseña WHERE nombre = ?", (id,))
    existing_resena = cursor.fetchone()

    if existing_resena:
        # La reseña existe, por lo que la actualizamos
        instruccion = "UPDATE reseña SET nombre = ?, puntuacion = ?, comentario = ? WHERE id = ?"
        cursor.execute(instruccion, (nombre, puntuacion, comentario, id))
        msg_about("Éxito!", "Reseña actualizada exitosamente!")
    else:
        # La reseña no existe, mostramos un mensaje de error
        msg_error("Error", "No se encontró la reseña para actualizar.")

    con.commit()
    con.close()

# Modifica la función mostrar_reseña para utilizar la función de actualización
"""
def mostrar_reseña():
    id = reseña.id.text()
    nombre = reseña.nombre_resea.text()
    puntuacion = int(reseña.puntuacion_resena.text())
    comentario = reseña.comentario_resena.text()

    if nombre.strip() == " ":
        msg_error("Error", "No se ingresó ningún usuario")
    elif comentario.strip() == "":
        msg_error("Error", "No se ingresó ningún comentario")
    else:
        actualizar_resena(id, nombre, puntuacion, comentario)
        reseña.id.setText("")
        reseña.nombre_resea.setText("")
        reseña.puntuacion_resena.setText("")
        reseña.comentario_resena.setText("")
"""



#Conexion con botones----------------------------
#inicio
login.pushButton.clicked.connect(gui_login)
login.pushButton_2.clicked.connect(gui_registro)
login.pushButton_3.clicked.connect(salir)
#registro
registro.pushButton_registro.clicked.connect(datos)
registro.pushButton_registro_2.clicked.connect(regresar_forma)

#interfaz
interfaz.bot_salir.clicked.connect(salir)
interfaz.bot_cerrarsesion.clicked.connect(regresar_forma)
interfaz.bot_siniestro.clicked.connect(siniestro1)
interfaz.bot_saw.clicked.connect(peliculasaw)
interfaz.bot_guerramundz.clicked.connect(regresar_forma)
interfaz.bot_pawpatrol.clicked.connect(regresar_forma)
interfaz.bot_joker.clicked.connect(regresar_forma)
interfaz.bot_godzilla.clicked.connect(regresar_forma)
interfaz.bot_spiderman.clicked.connect(regresar_forma)
interfaz.bot_barbie.clicked.connect(peliculabarbie)
interfaz.bot_bluebettle.clicked.connect(paginabluee)
interfaz.bot_mortalkombat.clicked.connect(regresar_forma)
interfaz.bot_jhonwwick.clicked.connect(paginajhonw)
interfaz.bot_rojo.clicked.connect(regresar_forma)

#reseña
reseña.bot_agregar.clicked.connect(mostrar_reseña)
reseña.bot_act.clicked.connect(actualizar_resena)
reseña.bot_eliminar.clicked.connect(gui_interfaz)
reseña.bot_salir.clicked.connect(gui_interfaz)

#botones de peliculas
ventana_personalizada.bot_resena.clicked.connect(gui_resena)
ventana_personalizada.BotonInicio.clicked.connect(gui_interfaz)

ventana2.bot_resena.clicked.connect(gui_resena)
ventana2.BotonInicio.clicked.connect(gui_interfaz)

ventana3.bot_resena.clicked.connect(gui_resena)
ventana3.BotonInicio.clicked.connect(gui_interfaz)

ventana4.bot_resena.clicked.connect(gui_resena)
ventana4.BotonInicio.clicked.connect(gui_interfaz)

ventana5.bot_resena.clicked.connect(gui_resena)
ventana5.BotonInicio.clicked.connect(gui_interfaz)
ventana6.bot_resena.clicked.connect(gui_resena)
ventana6.BotonInicio.clicked.connect(gui_interfaz)


#Ejecucion de app
login.show()
app.exec()


