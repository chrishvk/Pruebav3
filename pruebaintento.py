import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
#from conexion_sqlite import Comunicacion



class Prueba(QMainWindow):
    def __init__(self):
        super(Prueba, self).__init__()
        loadUi('interfaces/prueba.ui', self)




#Correr programa
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = Prueba()
    #Mostrar ventana
    mi_app.show()
    sys.exit(app.exec_())