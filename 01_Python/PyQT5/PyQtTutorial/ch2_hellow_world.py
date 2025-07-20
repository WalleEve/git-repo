from PyQt5.QtWidgets import * 
import sys 

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(700, 200, 400, 300)
        self.setWindowTitle("Hello")

        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel ("Hellow, World!")
        layout.addWidget(label, 0, 0) # this indicated grids position

    
app = QApplication(sys.argv)
screen = Window()
screen.show()

sys.exit(app.exec_())