import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from sort import sort


class window(QWidget):
    def __init__(self, parent = None):
        super(window, self).__init__(parent)
        self.resize(400,150)
        self.setWindowTitle("ImgSizeSort")
        self.label = QLabel(self)
        self.label.setText("Image Size Sorter")
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        fontSmall = QFont()
        fontSmall.setFamily("Arial")
        fontSmall.setPointSize(14)
        
        self.label.setFont(font)
        self.label.move(50,20)
        
        self.label2 = QLabel(self)
        self.label2.setText("path: ")
        self.label2.move(20, 60)
        self.label2.setFont(fontSmall)
        
        self.textbox = QLineEdit(self)
        self.textbox.move(80, 60)
        self.textbox.resize(280, 30)
        
        self.button = QPushButton('Sort', self)
        self.button.move(20, 110)
        self.button.clicked.connect(self.Button1)
        self.show()
      
    def Button1(self):
        path = self.textbox.text()
        
        exception = sort(path)
        
        msg = QMessageBox()
        msg.setWindowTitle("ImgCloneFinderInfo")
        if exception == 1:
            msg.setText("Finished.")
        elif exception == 2:
            msg.setText("Remove folders named lands cape portrait or square.")
        else: 
            msg.setText("Something went wrong.")
        
        x = msg.exec_()
      
def main():
   app = QApplication(sys.argv)
   ex = window()
   ex.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
   main()