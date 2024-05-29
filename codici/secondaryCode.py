# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5 import uic
import sys
 
 
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r"P:\Iterface\IterfaceLab\interfacciaGrafica\form.ui", self)
        
        self.buttonInterfaccia1 = self.findChild(QPushButton, "cambiaInterfaccia")
        self.buttonInterfaccia1.clicked.connect(self.changeInterface)
        
        self.show()
        
    def changeInterface(self):
        execfile(r"helphour.py")
    
app = QApplication(sys.argv)
window = UI()
app.exec_()
