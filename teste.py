from PySide6.QtWidgets import QMainWindow,QApplication
import sys
from sistema_teste_python import Ui_MainWindow



class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("Teste")
        self.setupUi(self)

        print(app.style().objectName())




if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())










