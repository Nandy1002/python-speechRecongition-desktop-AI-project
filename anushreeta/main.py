
from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("/home/anushreeta/pyProject/jarvisUi.ui", self)
        self.show()

        

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec()

if __name__=='__main__':
    main()


