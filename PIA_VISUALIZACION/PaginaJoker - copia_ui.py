# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\angel\Desktop\PIA_VISUALIZACION\PaginaJoker - copia.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 678)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelLogoNetflix = QtWidgets.QLabel(self.centralwidget)
        self.labelLogoNetflix.setGeometry(QtCore.QRect(20, 20, 151, 41))
        self.labelLogoNetflix.setText("")
        self.labelLogoNetflix.setPixmap(QtGui.QPixmap("c:\\Users\\angel\\Desktop\\PIA_VISUALIZACION\\imagenes/netflix-logo-51.png"))
        self.labelLogoNetflix.setScaledContents(True)
        self.labelLogoNetflix.setObjectName("labelLogoNetflix")
        self.BotonInicio = QtWidgets.QPushButton(self.centralwidget)
        self.BotonInicio.setGeometry(QtCore.QRect(200, 30, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BotonInicio.setFont(font)
        self.BotonInicio.setStyleSheet("color: white;\n"
"")
        self.BotonInicio.setFlat(True)
        self.BotonInicio.setObjectName("BotonInicio")
        self.BotonPeliculas = QtWidgets.QPushButton(self.centralwidget)
        self.BotonPeliculas.setGeometry(QtCore.QRect(310, 30, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BotonPeliculas.setFont(font)
        self.BotonPeliculas.setStyleSheet("color: white;\n"
"")
        self.BotonPeliculas.setFlat(True)
        self.BotonPeliculas.setObjectName("BotonPeliculas")
        self.labelLogoUsuario = QtWidgets.QLabel(self.centralwidget)
        self.labelLogoUsuario.setGeometry(QtCore.QRect(1180, 20, 41, 41))
        self.labelLogoUsuario.setText("")
        self.labelLogoUsuario.setPixmap(QtGui.QPixmap("c:\\Users\\angel\\Desktop\\PIA_VISUALIZACION\\imagenes/33db09513083d86358fe59ad8f888de0.png"))
        self.labelLogoUsuario.setScaledContents(True)
        self.labelLogoUsuario.setObjectName("labelLogoUsuario")
        self.labelUsuario = QtWidgets.QLabel(self.centralwidget)
        self.labelUsuario.setGeometry(QtCore.QRect(1110, 40, 60, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.labelUsuario.setFont(font)
        self.labelUsuario.setStyleSheet("COLOR: WHITE;")
        self.labelUsuario.setObjectName("labelUsuario")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1260, 10, 16, 160))
        self.verticalScrollBar.setStyleSheet("QScrollBar:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #E0E0E0, stop:1 #FFFFFF);\n"
"    width: 12px; /* Ancho del scrollbar */\n"
"    margin: 0px 0px 0px 0px;\n"
" border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #B0B0B0; /* Color del handle o thumb del scrollbar */\n"
"    min-height: 20px; /* Altura mínima del handle */\n"
"    border-radius: 6px; /* Bordes redondeados */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.ImagenFenomenoSiniestroFondo = QtWidgets.QLabel(self.centralwidget)
        self.ImagenFenomenoSiniestroFondo.setGeometry(QtCore.QRect(0, 0, 1281, 711))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.ImagenFenomenoSiniestroFondo.setFont(font)
        self.ImagenFenomenoSiniestroFondo.setText("")
        self.ImagenFenomenoSiniestroFondo.setPixmap(QtGui.QPixmap("c:\\Users\\angel\\Desktop\\PIA_VISUALIZACION\\imagenes/joker historia real goetz ny.jpeg.png"))
        self.ImagenFenomenoSiniestroFondo.setScaledContents(True)
        self.ImagenFenomenoSiniestroFondo.setObjectName("ImagenFenomenoSiniestroFondo")
        self.labelTituloFenomenoSiniestro = QtWidgets.QLabel(self.centralwidget)
        self.labelTituloFenomenoSiniestro.setGeometry(QtCore.QRect(40, 70, 1141, 81))
        self.labelTituloFenomenoSiniestro.setStyleSheet("QLabel {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgba(0, 0, 0, 0); /* Cambia el color de texto a transparente */\n"
"}\n"
"\n"
"color: white;")
        self.labelTituloFenomenoSiniestro.setObjectName("labelTituloFenomenoSiniestro")
        self.labelSinpsisFenomenOSiniestro = QtWidgets.QLabel(self.centralwidget)
        self.labelSinpsisFenomenOSiniestro.setGeometry(QtCore.QRect(30, 140, 1191, 251))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelSinpsisFenomenOSiniestro.setFont(font)
        self.labelSinpsisFenomenOSiniestro.setStyleSheet("QLabel {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgba(0, 0, 0, 0); /* Cambia el color de texto a transparente */\n"
"}\n"
"\n"
"color: white;\n"
"\n"
"QLabel {\n"
"    padding: 10px; /* Establece un margen de 10px alrededor del QLabel */\n"
"    line-height: 1.5; /* Establece un espaciado entre líneas del 1.5 (ajusta según tus preferencias) */\n"
"}\n"
"")
        self.labelSinpsisFenomenOSiniestro.setObjectName("labelSinpsisFenomenOSiniestro")
        self.labelDuracion = QtWidgets.QLabel(self.centralwidget)
        self.labelDuracion.setGeometry(QtCore.QRect(180, 160, 51, 21))
        self.labelDuracion.setStyleSheet("QLabel {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgba(0, 0, 0, 0); /* Cambia el color de texto a transparente */\n"
"}\n"
"\n"
"color: white;")
        self.labelDuracion.setObjectName("labelDuracion")
        self.labelGenero = QtWidgets.QLabel(self.centralwidget)
        self.labelGenero.setGeometry(QtCore.QRect(280, 160, 201, 21))
        self.labelGenero.setStyleSheet("QLabel {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgba(0, 0, 0, 0); /* Cambia el color de texto a transparente */\n"
"}\n"
"\n"
"color: white;")
        self.labelGenero.setObjectName("labelGenero")
        self.botonEstrella1 = QtWidgets.QPushButton(self.centralwidget)
        self.botonEstrella1.setGeometry(QtCore.QRect(50, 320, 31, 31))
        self.botonEstrella1.setText("")
        self.botonEstrella1.setCheckable(True)
        self.botonEstrella1.setFlat(True)
        self.botonEstrella1.setObjectName("botonEstrella1")
        self.labelEstrella1 = QtWidgets.QLabel(self.centralwidget)
        self.labelEstrella1.setGeometry(QtCore.QRect(50, 320, 31, 31))
        self.labelEstrella1.setStyleSheet("QLabel {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgba(0, 0, 0, 0); /* Cambia el color de texto a transparente */\n"
"}")
        self.labelEstrella1.setText("")
        self.labelEstrella1.setPixmap(QtGui.QPixmap("c:\\Users\\angel\\Desktop\\PIA_VISUALIZACION\\estrella.png"))
        self.labelEstrella1.setScaledContents(True)
        self.labelEstrella1.setObjectName("labelEstrella1")
        self.labelEstrella2 = QtWidgets.QLabel(self.centralwidget)
        self.labelEstrella2.setGeometry(QtCore.QRect(90, 320, 31, 31))
        self.labelEstrella2.setStyleSheet("QLabel {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgba(0, 0, 0, 0); /* Cambia el color de texto a transparente */\n"
"}")
        self.labelEstrella2.setText("")
        self.labelEstrella2.setPixmap(QtGui.QPixmap("c:\\Users\\angel\\Desktop\\PIA_VISUALIZACION\\estrella.png"))
        self.labelEstrella2.setScaledContents(True)
        self.labelEstrella2.setObjectName("labelEstrella2")
        self.labelEstrella4 = QtWidgets.QLabel(self.centralwidget)
        self.labelEstrella4.setGeometry(QtCore.QRect(170, 320, 31, 31))
        self.labelEstrella4.setStyleSheet("QLabel {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgba(0, 0, 0, 0); /* Cambia el color de texto a transparente */\n"
"}")
        self.labelEstrella4.setText("")
        self.labelEstrella4.setPixmap(QtGui.QPixmap("c:\\Users\\angel\\Desktop\\PIA_VISUALIZACION\\estrella.png"))
        self.labelEstrella4.setScaledContents(True)
        self.labelEstrella4.setObjectName("labelEstrella4")
        self.labelEstrella3 = QtWidgets.QLabel(self.centralwidget)
        self.labelEstrella3.setGeometry(QtCore.QRect(130, 320, 31, 31))
        self.labelEstrella3.setStyleSheet("QLabel {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgba(0, 0, 0, 0); /* Cambia el color de texto a transparente */\n"
"}")
        self.labelEstrella3.setText("")
        self.labelEstrella3.setPixmap(QtGui.QPixmap("c:\\Users\\angel\\Desktop\\PIA_VISUALIZACION\\estrella.png"))
        self.labelEstrella3.setScaledContents(True)
        self.labelEstrella3.setObjectName("labelEstrella3")
        self.labelEstrella5 = QtWidgets.QLabel(self.centralwidget)
        self.labelEstrella5.setGeometry(QtCore.QRect(210, 320, 31, 31))
        self.labelEstrella5.setStyleSheet("QLabel {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgba(0, 0, 0, 0); /* Cambia el color de texto a transparente */\n"
"}")
        self.labelEstrella5.setText("")
        self.labelEstrella5.setPixmap(QtGui.QPixmap("c:\\Users\\angel\\Desktop\\PIA_VISUALIZACION\\estrella.png"))
        self.labelEstrella5.setScaledContents(True)
        self.labelEstrella5.setObjectName("labelEstrella5")
        self.botonEstrella2 = QtWidgets.QPushButton(self.centralwidget)
        self.botonEstrella2.setGeometry(QtCore.QRect(90, 320, 31, 31))
        self.botonEstrella2.setText("")
        self.botonEstrella2.setCheckable(True)
        self.botonEstrella2.setFlat(True)
        self.botonEstrella2.setObjectName("botonEstrella2")
        self.botonEstrella3 = QtWidgets.QPushButton(self.centralwidget)
        self.botonEstrella3.setGeometry(QtCore.QRect(130, 320, 31, 31))
        self.botonEstrella3.setText("")
        self.botonEstrella3.setCheckable(True)
        self.botonEstrella3.setFlat(True)
        self.botonEstrella3.setObjectName("botonEstrella3")
        self.botonEstrella4 = QtWidgets.QPushButton(self.centralwidget)
        self.botonEstrella4.setGeometry(QtCore.QRect(170, 320, 31, 31))
        self.botonEstrella4.setText("")
        self.botonEstrella4.setCheckable(True)
        self.botonEstrella4.setFlat(True)
        self.botonEstrella4.setObjectName("botonEstrella4")
        self.botonEstrella5 = QtWidgets.QPushButton(self.centralwidget)
        self.botonEstrella5.setGeometry(QtCore.QRect(210, 320, 31, 31))
        self.botonEstrella5.setText("")
        self.botonEstrella5.setCheckable(True)
        self.botonEstrella5.setFlat(True)
        self.botonEstrella5.setObjectName("botonEstrella5")
        self.BotonPeliculas_2 = QtWidgets.QPushButton(self.centralwidget)
        self.BotonPeliculas_2.setGeometry(QtCore.QRect(210, 330, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.BotonPeliculas_2.setFont(font)
        self.BotonPeliculas_2.setStyleSheet("color: white;\n"
"")
        self.BotonPeliculas_2.setFlat(True)
        self.BotonPeliculas_2.setObjectName("BotonPeliculas_2")
        self.agregaUnComentario = QtWidgets.QTextEdit(self.centralwidget)
        self.agregaUnComentario.setGeometry(QtCore.QRect(40, 460, 441, 141))
        self.agregaUnComentario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"")
        self.agregaUnComentario.setObjectName("agregaUnComentario")
        self.bot_resena = QtWidgets.QPushButton(self.centralwidget)
        self.bot_resena.setGeometry(QtCore.QRect(90, 410, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.bot_resena.setFont(font)
        self.bot_resena.setStyleSheet("color: white;\n"
"")
        self.bot_resena.setFlat(True)
        self.bot_resena.setObjectName("bot_resena")
        self.ImagenFenomenoSiniestroFondo.raise_()
        self.labelLogoNetflix.raise_()
        self.BotonInicio.raise_()
        self.BotonPeliculas.raise_()
        self.labelLogoUsuario.raise_()
        self.labelUsuario.raise_()
        self.verticalScrollBar.raise_()
        self.labelTituloFenomenoSiniestro.raise_()
        self.labelSinpsisFenomenOSiniestro.raise_()
        self.labelDuracion.raise_()
        self.labelGenero.raise_()
        self.labelEstrella1.raise_()
        self.labelEstrella2.raise_()
        self.labelEstrella4.raise_()
        self.labelEstrella3.raise_()
        self.labelEstrella5.raise_()
        self.botonEstrella2.raise_()
        self.botonEstrella3.raise_()
        self.botonEstrella4.raise_()
        self.botonEstrella5.raise_()
        self.BotonPeliculas_2.raise_()
        self.botonEstrella1.raise_()
        self.agregaUnComentario.raise_()
        self.bot_resena.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionCerrar_Sesion = QtWidgets.QAction(MainWindow)
        self.actionCerrar_Sesion.setObjectName("actionCerrar_Sesion")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BotonInicio.setText(_translate("MainWindow", "Inicio"))
        self.BotonPeliculas.setText(_translate("MainWindow", "Peliculas"))
        self.labelUsuario.setText(_translate("MainWindow", "USUARIO"))
        self.labelTituloFenomenoSiniestro.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt; font-weight:600; color:#ffffff;\">GUASON</span></p><p><br/></p><p><br/></p><p><br/></p></body></html>"))
        self.labelSinpsisFenomenOSiniestro.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" color:#e1e1e1;\">La pasión de Arthur Fleck, un hombre ignorado por la sociedad, es hacer reír a la gente. </span></p><p align=\"justify\"><span style=\" color:#e1e1e1;\">Sin embargo, una serie de trágicos sucesos harán que su visión del mundo se distorsione</span></p><p align=\"justify\"><span style=\" color:#e1e1e1;\">considerablemente convirtiéndolo en un brillante criminal.</span></p></body></html>"))
        self.labelDuracion.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">1h 40m </span></p></body></html>"))
        self.labelGenero.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Terror sobrenatural</span></p></body></html>"))
        self.BotonPeliculas_2.setText(_translate("MainWindow", "Reseñas"))
        self.bot_resena.setText(_translate("MainWindow", "Agrega un comentario"))
        self.actionCerrar_Sesion.setText(_translate("MainWindow", "Cerrar Sesion"))