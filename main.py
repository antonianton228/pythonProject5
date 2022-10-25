import sqlite3
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QApplication
from PyQt5.QtGui import QPixmap


class Ui_Form(object):
    def __init__(self, a):
        super().__init__()
        self.id = a

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 592)



        self.pixmap = QPixmap(self.id[5]).scaled(121, 181)
        self.image = QLabel(Form)
        self.image.move(150, 20)
        self.image.resize(121, 181)
        self.image.setPixmap(self.pixmap)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 230, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 280, 281, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(160, 300, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 340, 351, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(140, 360, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(-20, 400, 431, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(170, 420, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(-40, 480, 491, 16))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        self.con = sqlite3.connect("bd.bd.db")
        self.cur = self.con.cursor()
        aut = self.cur.execute(f"""SELECT name FROM authors WHERE id = {self.id[2]}""").fetchall()[0][0]
        gen = self.cur.execute(f"""SELECT title FROM genres WHERE id = {self.id[4]}""").fetchall()[0][0]


        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Название"))
        self.label_2.setText(_translate("Form", self.id[1]))
        self.label_3.setText(_translate("Form", "Автор"))
        self.label_4.setText(_translate("Form", aut))
        self.label_5.setText(_translate("Form", "Год выпуска"))
        self.label_6.setText(_translate("Form", str(self.id[3])))
        self.label_7.setText(_translate("Form", "Жанр"))
        self.label_8.setText(_translate("Form", gen))




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.list_of_buts = []
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(90, 60, 171, 22))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 90, 171, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText('  ')

        self.comboBox.addItems(['Автор', 'Название'])

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 40, 191, 81))
        self.pushButton.setObjectName("pushButton")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(130, 150, 551, 351))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.con = sqlite3.connect("bd.bd.db")
        self.cur = self.con.cursor()



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "find"))

        self.pushButton.clicked.connect(self.a)

    def pick(self, id):
        button = QApplication.instance().sender().inf
        dialog = QDialog()
        dialog.ui = Ui_Form(button)
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()

    def a(self):
        result = []
        if self.comboBox.currentIndex() == 0:
            result = self.cur.execute(f"""SELECT * FROM books
                        WHERE author = (SELECT id FROM authors 
    WHERE name like '%{str(self.lineEdit.text()).lower()}%')""").fetchall()
        elif self.comboBox.currentIndex() == 1:
            result = self.cur.execute(f"""SELECT * FROM books
                                WHERE title like '%{self.lineEdit.text().lower()}%'""").fetchall()




        for i in self.list_of_buts:
            i.setVisible(False)
        self.list_of_buts = []
        for i in range(len(result)):
            QtWidgets.QPushButton()
            self.list_of_buts.append(Push(result[i], self.centralwidget))
            self.list_of_buts[i].setGeometry(QtCore.QRect(140, 160 + 40 * i, 531, 31))
            self.list_of_buts[i].setVisible(True)
            self.list_of_buts[i].setText(result[i][1])
            self.list_of_buts[i].clicked.connect(lambda x: self.pick(result[i]))



class Push(QPushButton):
    def __init__(self, a, QWidget = None):
        super().__init__(QWidget)
        self.inf = a


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())