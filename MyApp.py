from PyQt6.QtWidgets import QApplication, QMainWindow
from baitap22Ext import Ui_MainWindow  # Nhập lớp giao diện từ file baitap22Ext.py

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
