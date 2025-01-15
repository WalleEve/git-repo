import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window_1_2 import ImageApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageApp()
    window.show()
    sys.exit(app.exec_())
