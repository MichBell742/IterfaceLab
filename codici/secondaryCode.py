# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5 import uic
import sys
 
 
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r"P:\Iterface\IterfaceLab\interfacciaGrafica\forum.ui", self)
 
        # find the widgets in the xml file
        
        self.lista=[
                {"studente":"Andrea","professore":"Marco","ore":"24"},
                {"studente":"Marco","professore":"Andreoli","ore":"24"},
                {"studente":"Ruspi","professore":"Luca","ore":"24"}
            ]
        
        self.buttonRimuovi = self.findChild(QPushButton, "bRimuovi")
        self.buttonRimuovi.clicked.connect(self.clickedRimuovi)
        
        self.tabella = self.findChild(QTableWidget, "tabellaAssociazione")
        self.tabella.setColumnCount(3)
        self.tabella.setRowCount(3)
        self.tabella.setHorizontalHeaderLabels(["nome","cognome","ore"])
        
        cont=0
        for i in self.lista:
            self.tabella.setItem(cont,0,QTableWidgetItem(i["studente"]))
            self.tabella.setItem(cont,1,QTableWidgetItem(i["professore"]))
            self.tabella.setItem(cont,2,QTableWidgetItem(i["ore"])) 
            cont+=1
        
        self.show()
        
    def clickedRimuovi(self):
        #rimuovere la riga delle informazioni dalla tabella e dal dizionario
        indice = self.tabella.currentRow()
        print(indice)
        self.lista.remove(self.lista[indice])
        self.tabella.removeRow(indice);
        print(self.lista)
        

app = QApplication(sys.argv)
window = UI()
app.exec_()
