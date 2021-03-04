# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginBanco.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(828, 789)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Images/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color: rgb(200, 200, 200);\n"
"background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.top_bar.setStyleSheet("")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frameError = QtWidgets.QFrame(self.top_bar)
        self.frameError.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frameError.setStyleSheet("background-color: rgb(255, 85, 127);\n"
"border-radius: 5px")
        self.frameError.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameError.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameError.setObjectName("frameError")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frameError)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.obj_popUpError = QtWidgets.QLabel(self.frameError)
        self.obj_popUpError.setStyleSheet("color: rgb(35, 35, 35);")
        self.obj_popUpError.setAlignment(QtCore.Qt.AlignCenter)
        self.obj_popUpError.setObjectName("obj_popUpError")
        self.horizontalLayout_3.addWidget(self.obj_popUpError)
        self.btn_ErrorX = QtWidgets.QPushButton(self.frameError)
        self.btn_ErrorX.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_ErrorX.setStyleSheet("QPushButton {\n"
"\n"
"    border-radius: 5px;\n"
"    background-image: url(:/close_img/Images/cil-x.png);\n"
"    background-position: center;\n"
"    background-color: rgb(60, 60, 60);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(50, 50, 50);\n"
"    color: rgb(170, 0, 0)\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(170, 0, 0)\n"
"    \n"
"}\n"
"")
        self.btn_ErrorX.setText("")
        self.btn_ErrorX.setObjectName("btn_ErrorX")
        self.horizontalLayout_3.addWidget(self.btn_ErrorX)
        self.horizontalLayout_2.addWidget(self.frameError)
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_area = QtWidgets.QFrame(self.content)
        self.login_area.setMaximumSize(QtCore.QSize(450, 550))
        self.login_area.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_area.setObjectName("login_area")
        self.logo = QtWidgets.QFrame(self.login_area)
        self.logo.setGeometry(QtCore.QRect(165, 20, 120, 120))
        self.logo.setStyleSheet("image: url(:/BankLogo/Images/bankLogo.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.avatar = QtWidgets.QFrame(self.login_area)
        self.avatar.setGeometry(QtCore.QRect(180, 160, 100, 100))
        self.avatar.setStyleSheet("QFrame {\n"
"\n"
"    background-image: url(:/avatarIcon/Images/avatar.png);\n"
"    border-radius: 50px;\n"
"    border: 7px solid rgb(125, 203, 255);\n"
"    background-position: center;\n"
"\n"
"}\n"
"QFrame:hover {\n"
"\n"
"    border: 7px solid rgb(125, 193, 255);\n"
"\n"
"}")
        self.avatar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.avatar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.avatar.setObjectName("avatar")
        self.conta = QtWidgets.QLineEdit(self.login_area)
        self.conta.setGeometry(QtCore.QRect(85, 280, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.conta.setFont(font)
        self.conta.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.conta.setStyleSheet("QLineEdit {\n"
"\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgb(110, 110, 110);\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"\n"
"    border: 2px solid rgb(65, 65, 65);\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"\n"
"    border: 2px solid rgb(125, 203, 205);\n"
"    color: rgb(200, 200, 200);\n"
"\n"
"}")
        self.conta.setMaxLength(7)
        self.conta.setObjectName("conta")
        self.senha = QtWidgets.QLineEdit(self.login_area)
        self.senha.setGeometry(QtCore.QRect(85, 335, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.senha.setFont(font)
        self.senha.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.senha.setStyleSheet("QLineEdit {\n"
"\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgb(110, 110, 110);\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"\n"
"    border: 2px solid rgb(65, 65, 65);\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"\n"
"    border: 2px solid rgb(125, 203, 205);\n"
"    color: rgb(200, 200, 200);\n"
"\n"
"}")
        self.senha.setMaxLength(16)
        self.senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senha.setObjectName("senha")
        self.checkBox = QtWidgets.QCheckBox(self.login_area)
        self.checkBox.setGeometry(QtCore.QRect(85, 390, 285, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("QCheckBox:indicator {\n"
"\n"
"    border: 3px solid rgb(100, 100, 100);\n"
"    border-radius: 5px;\n"
"    background-color: rgb(135, 135, 135);\n"
"\n"
"}\n"
"QCheckBox:indicator:checked {\n"
"\n"
"    border: 3px solid rgb(170, 255, 255);\n"
"    background-color: rgb(125, 203, 205);\n"
"\n"
"}")
        self.checkBox.setObjectName("checkBox")
        self.entrar = QtWidgets.QPushButton(self.login_area)
        self.entrar.setGeometry(QtCore.QRect(85, 425, 280, 50))
        self.entrar.setStyleSheet("QPushButton {\n"
"\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70, 70, 70);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(125, 203, 205);\n"
"    border: 2px solid rgb(170, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}")
        self.entrar.setObjectName("entrar")
        self.horizontalLayout.addWidget(self.login_area)
        self.verticalLayout.addWidget(self.content)
        self.bottom = QtWidgets.QFrame(self.centralwidget)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bottom.setStyleSheet("background-color: rgb(15, 15, 15);")
        self.bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bottom)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.bottom)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(75, 75, 75);")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.bottom)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.obj_popUpError.setText(_translate("MainWindow", "Error"))
        self.conta.setPlaceholderText(_translate("MainWindow", "CONTA"))
        self.senha.setPlaceholderText(_translate("MainWindow", "SENHA"))
        self.checkBox.setText(_translate("MainWindow", "LEMBRAR USUÁRIO"))
        self.entrar.setText(_translate("MainWindow", "ENTRAR"))
        self.label.setText(_translate("MainWindow", "CREATED BY: ALEXANDRE TAVARES"))
import file_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
