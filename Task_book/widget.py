
from os.path import dirname, join
#from pathlib import Path
import sys
'''
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
'''
from PyQt5.Qt import *                                            # PyQt5
from PyQt5 import uic


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()

    def load_ui(self):
        '''
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

        #self.ui = QUiLoader().load("form.ui", self)
        self.loader.Create_Task_button.clicked(self.onClicked)
        '''
        current_dir = dirname(__file__)
        uic.loadUi(current_dir + "./form.ui", self)
        self.Create_Task_button.clicked.connect(self.onClicked)

    def onClicked(self):
        date_1 = self.Calendar_1.selectedDate().toString('MMMM d, yyyy')
        time_1 = self.Time_text.toPlainText()
        task_1 = self.Task_text.toPlainText()
        self.Task_Book.append(date_1 + " " + time_1 + " - " + task_1)

if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
