from PyQt6 import QtCore, QtGui, QtWidgets


# Mã xác suất tính toán
def calculate_combination(n, k):
    if k > n:
        return 0
    result = 1
    for i in range(k):
        result *= (n - i) / (i + 1)
    return result


def calculate_probability(N, D, M):
    if N <= 0 or D < 0 or M <= 0 or D > N or M > N:
        return "Invalid input"

    C_D_1 = calculate_combination(D, 1)  # Chọn 1 bóng hỏng từ D bóng hỏng
    C_N_D_M_1 = calculate_combination(N - D, M - 1)  # Chọn M-1 bóng tốt từ N-D bóng tốt
    C_N_M = calculate_combination(N, M)  # Chọn M bóng từ tổng N bóng

    probability = (C_D_1 * C_N_D_M_1) / C_N_M
    return round(probability, 4)


# Lớp chính của cửa sổ ứng dụng
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(656, 544)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Tiêu đề
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 50, 421, 51))
        self.label.setObjectName("label")

        # Nhóm nhập liệu
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 110, 561, 181))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        # Các label
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 301, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 331, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 331, 31))
        self.label_4.setObjectName("label_4")

        # Các ô nhập liệu
        self.lineEditN = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditN.setGeometry(QtCore.QRect(320, 41, 171, 31))
        self.lineEditN.setObjectName("lineEditN")
        self.lineEditD = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditD.setGeometry(QtCore.QRect(360, 80, 171, 31))
        self.lineEditD.setObjectName("lineEditD")
        self.lineEditM = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditM.setGeometry(QtCore.QRect(350, 120, 171, 31))
        self.lineEditM.setObjectName("lineEditM")

        # Nút tính toán
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 300, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Calculate")

        # Nhóm kết quả
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 360, 561, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(30, 40, 211, 41))
        self.label_5.setObjectName("label_5")

        # Kết quả tính toán
        self.lineEditProfit = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditProfit.setGeometry(QtCore.QRect(260, 40, 231, 41))
        self.lineEditProfit.setObjectName("lineEditProfit")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Kết nối nút bấm với hàm tính toán
        self.pushButton.clicked.connect(self.calculate_button_clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Light Bulb Inspection Calculator"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\">Light Bulb Inspection Probability Calculator </span></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Input N,D,M:"))
        self.label_2.setText(_translate("MainWindow", "Total Number of Light Bulbs (N): "))
        self.label_3.setText(_translate("MainWindow", "Number of Damaged Light Bulbs (D):"))
        self.label_4.setText(_translate("MainWindow", "Number of Light Bulbs to Check (M):"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Result:"))
        self.label_5.setText(_translate("MainWindow", "Calculated Probability:"))

    def calculate_button_clicked(self):
        try:
            N = int(self.lineEditN.text())
            D = int(self.lineEditD.text())
            M = int(self.lineEditM.text())

            probability = calculate_probability(N, D, M)
            self.lineEditProfit.setText(str(probability))
        except ValueError:
            self.lineEditProfit.setText("Invalid input")
