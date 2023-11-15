# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\angel\Desktop\PIA_VISUALIZACION\reseña.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(986, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 991, 631))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(190, 10, 141, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("c:\\Users\\angel\\Desktop\\PIA_VISUALIZACION\\imagenes/netflix-logo-51.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(80, 110, 81, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(80, 180, 121, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(80, 250, 121, 41))
        self.label_8.setObjectName("label_8")
        self.nombre_resea = QtWidgets.QLineEdit(self.frame)
        self.nombre_resea.setGeometry(QtCore.QRect(220, 110, 341, 51))
        self.nombre_resea.setStyleSheet("background-color: rgb(153, 153, 153);\n"
"font: 13pt \".AppleSystemUIFont\";\n"
"font: 13pt \".AppleSystemUIFont\";\n"
"font: 13pt \".AppleSystemUIFont\";\n"
"border-radius:5px;")
        self.nombre_resea.setText("")
        self.nombre_resea.setMaxLength(32768)
        self.nombre_resea.setPlaceholderText("")
        self.nombre_resea.setObjectName("nombre_resea")
        self.puntuacion_resena = QtWidgets.QLineEdit(self.frame)
        self.puntuacion_resena.setGeometry(QtCore.QRect(220, 180, 341, 51))
        self.puntuacion_resena.setStyleSheet("background-color: rgb(153, 153, 153);\n"
"font: 13pt \".AppleSystemUIFont\";\n"
"font: 13pt \".AppleSystemUIFont\";\n"
"font: 13pt \".AppleSystemUIFont\";\n"
"border-radius:5px;")
        self.puntuacion_resena.setText("")
        self.puntuacion_resena.setMaxLength(32768)
        self.puntuacion_resena.setPlaceholderText("")
        self.puntuacion_resena.setObjectName("puntuacion_resena")
        self.bot_agregar = QtWidgets.QPushButton(self.frame)
        self.bot_agregar.setGeometry(QtCore.QRect(220, 450, 121, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.bot_agregar.setFont(font)
        self.bot_agregar.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(240, 0, 27);\n"
"Color: white;")
        self.bot_agregar.setObjectName("bot_agregar")
        self.bot_act = QtWidgets.QPushButton(self.frame)
        self.bot_act.setGeometry(QtCore.QRect(370, 450, 121, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.bot_act.setFont(font)
        self.bot_act.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(240, 0, 27);\n"
"Color: white;")
        self.bot_act.setObjectName("bot_act")
        self.bot_eliminar = QtWidgets.QPushButton(self.frame)
        self.bot_eliminar.setGeometry(QtCore.QRect(510, 450, 121, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.bot_eliminar.setFont(font)
        self.bot_eliminar.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(240, 0, 27);\n"
"Color: white;")
        self.bot_eliminar.setObjectName("bot_eliminar")
        self.bot_salir = QtWidgets.QPushButton(self.frame)
        self.bot_salir.setGeometry(QtCore.QRect(650, 450, 121, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.bot_salir.setFont(font)
        self.bot_salir.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(240, 0, 27);\n"
"Color: white;")
        self.bot_salir.setObjectName("bot_salir")
        self.comentario_resena = QtWidgets.QLineEdit(self.frame)
        self.comentario_resena.setGeometry(QtCore.QRect(220, 260, 341, 51))
        self.comentario_resena.setStyleSheet("background-color: rgb(153, 153, 153);\n"
"font: 13pt \".AppleSystemUIFont\";\n"
"font: 13pt \".AppleSystemUIFont\";\n"
"font: 13pt \".AppleSystemUIFont\";\n"
"border-radius:5px;")
        self.comentario_resena.setText("")
        self.comentario_resena.setMaxLength(32768)
        self.comentario_resena.setPlaceholderText("")
        self.comentario_resena.setObjectName("comentario_resena")
        self.nombre_resea_2 = QtWidgets.QLineEdit(self.frame)
        self.nombre_resea_2.setGeometry(QtCore.QRect(220, 70, 81, 21))
        self.nombre_resea_2.setStyleSheet("background-color: rgb(153, 153, 153);\n"
"font: 13pt \".AppleSystemUIFont\";\n"
"font: 13pt \".AppleSystemUIFont\";\n"
"font: 13pt \".AppleSystemUIFont\";\n"
"border-radius:5px;")
        self.nombre_resea_2.setText("")
        self.nombre_resea_2.setMaxLength(32768)
        self.nombre_resea_2.setPlaceholderText("")
        self.nombre_resea_2.setObjectName("nombre_resea_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">NOMBRE</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">PUNTUACION</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">COMENTARIO</span></p></body></html>"))
        self.bot_agregar.setText(_translate("MainWindow", "Agregar"))
        self.bot_act.setText(_translate("MainWindow", "Actualizar"))
        self.bot_eliminar.setText(_translate("MainWindow", "Eliminar"))
        self.bot_salir.setText(_translate("MainWindow", "Salir"))
