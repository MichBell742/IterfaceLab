# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5 import uic
import sys, csv
 
 
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r"ui\mainwindow.ui", self)
 
        # find the widgets in the xml file
        
        self.buttProf = self.findChild(QPushButton, "pushProfs")
        self.buttProf.clicked.connect(self.chargeProfs)
        
        self.buttStudente = self.findChild(QPushButton, "pushStudents")
        self.buttStudente.clicked.connect(self.chargeStudents)
 
        self.tableProfs = self.findChild(QTableWidget, "tableProfs")
        self.tableProfs.setColumnCount(3)
        self.tableProfs.setRowCount(3)
        self.tableProfs.setHorizontalHeaderLabels(["Nome", "Cognome","Ore"])
        
        self.tableProfs = self.findChild(QTableWidget, "tableStudents")
        self.tableProfs.setColumnCount(3)
        self.tableProfs.setRowCount(3)
        self.tableProfs.setHorizontalHeaderLabels(["Nome", "Cognome","Classe"])
 
        self.show()
        
    def chargeProfs(self):
        profDictionary={}
        dati = []
        fileIn=open("input\\Docenti.csv", "r", encoding="utf-8")
        reader = csv.DictReader(fileIn)
        for prova in reader:
            #print(prova)
            dati.append(prova)
        fileIn.close()
        print("caricati i prof")
        print(dati)
        riga=0
        for element in dati:
            item_name = QTableWidgetItem(element["nome"])
            self.tableProfs.setItem(riga,0, item_name)         
            item_name2 = QTableWidgetItem(element["cognome"])
            self.tableProfs.setItem(riga,1, item_name2)
            item_name3 = QTableWidgetItem(element["ore"])
            self.tableProfs.setItem(riga,2, item_name3)
            riga+=1
        
    def chargeStudents(self):
        studentiDictionary={}
        dati = []
        fileIn=open("input\\Studenti.csv", "r", encoding="utf-8")
        reader = csv.DictReader(fileIn)
        for prova in reader:
            #print(prova)
            dati.append(prova)
        fileIn.close()
        print("caricati i studenti nel seguente modo: ")
        print(dati)
        
 
app = QApplication(sys.argv)
window = UI()
app.exec_()
