# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit
from PyQt5 import uic
import sys
 
 
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r"C:\Users\giacomolillacci\Desktop\mainwindow.ui", self)
 
        # find the widgets in the xml file
        
        #self.textedit = self.findChild(QLineEdit, "line1")
        #self.button = self.findChild(QPushButton, "button")
        #self.button.clicked.connect(self.clickedBtn)
 
        self.show()
 
 
 
    def clickedBtn(self):
        atext = self.textedit.text()
        print(atext)

app = QApplication(sys.argv)
window = UI()
app.exec_()