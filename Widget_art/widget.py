
from os.path import dirname, join    
from pathlib import Path
import sys

from PyQt5.Qt import *                                            # PyQt5
from PyQt5 import uic, QtWidgets, QtGui, QtCore



class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()
        
    def load_ui(self):
        current_dir = dirname(__file__)
        uic.loadUi(current_dir + "./Form_1.ui", self)
        self.Create_matrix.clicked.connect(self.onClicked)

    
    def onClicked(self):
        h = int(self.Height.toPlainText())
        w = int(self.Weight.toPlainText())
        #print(1)
        self.w2 = Window2(h,w)
        #print(1)
        self.w2.show()

class Button(QPushButton):
   def __init__(self, num, text, size, color):                 # !!!
        super().__init__()  

        self.setText(" ")                          # 
        self.setFixedSize(*size)                               # !!! (*size)         

class Window2(QWidget):
    def __init__(self,h,w):
        
        super().__init__()

        
        
        many_buttons = h*w                    # хотим создать h*w кнопок
        column = w                          # хотим разместить эти кнопки в w колонки
        size = (40, 40)                    # размер кнопки
        color = '#000000'                    # цвет текста 
        
        layout = QGridLayout(self)
        
        for step in range(many_buttons):
            btn = Button(step+1, '*', size, color)               # !!!
            btn.clicked.connect(lambda ch, b=btn : self.onClicked(b))
            layout.addWidget(btn, step // column, step % column)  
        
    def onClicked(self, btn):
        # действия по нажатию на кнопку
        if btn.text() ==" ":
            btn.setText("*")
        else:
            btn.setText(" ")
        

if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())


