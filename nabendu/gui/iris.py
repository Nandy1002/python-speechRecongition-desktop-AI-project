pyqt tutorialpyqt tutorial# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvisUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JarvisUi(object):
    def setupUi(self, JarvisUi):
        JarvisUi.setObjectName("JarvisUi")
        JarvisUi.resize(1372, 720)
        self.centralwidget = QtWidgets.QWidget(JarvisUi)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(-70, 10, 1451, 741))
        self.label_1.setText("")
        self.label_1.setPixmap(QtGui.QPixmap("../Downloads/Black_Template.jpg"))
        self.label_1.setScaledContents(True)
        self.label_1.setObjectName("label_1")
        self.gif_1 = QtWidgets.QLabel(self.centralwidget)
        self.gif_1.setGeometry(QtCore.QRect(10, 60, 241, 171))
        self.gif_1.setText("")
        self.gif_1.setPixmap(QtGui.QPixmap("../Downloads/Earth.gif"))
        self.gif_1.setScaledContents(True)
        self.gif_1.setObjectName("gif_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(266, 66, 1061, 171))
        self.label_2.setStyleSheet("background-color: rgb(26, 95, 180);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Downloads/2DY9ob.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.textBox_1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBox_1.setGeometry(QtCore.QRect(375, 81, 931, 131))
        self.textBox_1.setStyleSheet("font: 57 11pt \"Ubuntu\";\n"
"background-color: rgb(222, 221, 218);")
        self.textBox_1.setObjectName("textBox_1")
        self.line_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_1.setGeometry(QtCore.QRect(0, 250, 1331, 16))
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.text_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(273, 80, 91, 51))
        self.text_1.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.text_1.setObjectName("text_1")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(36, 306, 1291, 221))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../Downloads/2DY9ob.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(55, 320, 1241, 181))
        self.textBrowser.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.textBrowser.setObjectName("textBrowser")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 559, 1331, 41))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 620, 31, 31))
        self.pushButton.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Downloads/mic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(76, 606, 1081, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../Downloads/2DY9ob.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.text_edit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_edit.setGeometry(QtCore.QRect(93, 619, 1041, 41))
        self.text_edit.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.text_edit.setObjectName("text_edit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1178, 610, 151, 61))
        self.pushButton_2.setStyleSheet("background-color: rgb(41, 146, 179);\n"
"font: 75 20pt \"Ubuntu Mono\";")
        self.pushButton_2.setObjectName("pushButton_2")
        JarvisUi.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(JarvisUi)
        self.statusbar.setObjectName("statusbar")
        JarvisUi.setStatusBar(self.statusbar)

        self.retranslateUi(JarvisUi)
        QtCore.QMetaObject.connectSlotsByName(JarvisUi)

    def retranslateUi(self, JarvisUi):
        _translate = QtCore.QCoreApplication.translate
        JarvisUi.setWindowTitle(_translate("JarvisUi", "MainWindow"))
        self.text_1.setHtml(_translate("JarvisUi", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#3d3846;\">Did You Mean...</span></p></body></html>"))
        self.pushButton_2.setText(_translate("JarvisUi", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JarvisUi = QtWidgets.QMainWindow()
    ui = Ui_JarvisUi()
    ui.setupUi(JarvisUi)
    JarvisUi.show()
    sys.exit(app.exec_())
