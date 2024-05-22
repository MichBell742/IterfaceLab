# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5 import uic
import sys
 
 
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r"mainwindow.ui", self)
 
        # find the widgets in the xml file
        
        lista=[
                {"nome":"Andrea","professore":"Marco","ore":"24"},
                {"nome":"Marco","professore":"Andreoli","ore":"24"},
                {"nome":"Ruspi","professore":"Luca","ore":"24"}
            ]
        
        self.buttonRimuovi = self.findChild(QPushButton, "bRimuovi")
        self.buttonRimuovi.clicked.connect(self.clickedBtn)
        
        self.tabella = self.findChild(QTableWidget, "tabellaAssociazione")
        self.tabella.setColumnCount(3)
        self.tabella.setRowCount(4)
        self.tabella.setHorizontalHeaderLabels(["nome","cognome","ore"])
        
        self.tabella.setItem(0,0,QTableWidgetItem(lista[0]["nome"]))  
        
        self.show()
        
    def clickedBtn(self):
        
        atext = self.textedit.text()
        print(atext)

app = QApplication(sys.argv)
window = UI()
app.exec_()