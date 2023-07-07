import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import *

  
class Button(QPushButton):
   def __init__(self, num, text, size, color):                 # !!!
        super().__init__()  

        self.setText(f'{text} {num}')                          # !!! {text} {num}
        self.setFixedSize(*size)                               # !!! (*size) 


class Example(QWidget): 
    def __init__(self):
        super().__init__()
        
        many_buttons = 16                    # хотим создать 16 кнопок
        column = 4                           # хотим разместить эти кнопки в 4 колонки
        size = (150, 150)                    # размер кнопки, например 150х150 
        color = '#ffffff'                    # пускай цвет текста будет такой
        
        layout = QGridLayout(self)
        
        for step in range(many_buttons):
            btn = Button(step+1, '*', size, color)               # !!!
            btn.clicked.connect(lambda ch, b=btn : self.onClicked(b))
            layout.addWidget(btn, step // column, step % column)        
        
    def onClicked(self, btn):
        # тут выполняются какие-то действия по нажатию на кнопку
        # допустим мы хотим скрыть кнопку, на которуй нажали
        btn.setText("1") 
        

if __name__ == '__main__':        
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
