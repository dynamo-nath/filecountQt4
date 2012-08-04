# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filecount.ui'
#
# Created: Sat Aug  4 14:56:07 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(600, 500)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 560, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lblFileSearch = QtGui.QLabel(self.centralwidget)
        self.lblFileSearch.setGeometry(QtCore.QRect(20, 10, 250, 17))
        self.lblFileSearch.setObjectName(_fromUtf8("lblFileSearch"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 80, 560, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.lblFileCombo = QtGui.QLabel(self.centralwidget)
        self.lblFileCombo.setGeometry(QtCore.QRect(20, 60, 191, 17))
        self.lblFileCombo.setObjectName(_fromUtf8("lblFileCombo"))
        self.txtResults = QtGui.QTextEdit(self.centralwidget)
        self.txtResults.setGeometry(QtCore.QRect(20, 130, 560, 200))
        self.txtResults.setObjectName(_fromUtf8("txtResults"))
        self.lblResult = QtGui.QLabel(self.centralwidget)
        self.lblResult.setGeometry(QtCore.QRect(20, 110, 191, 17))
        self.lblResult.setObjectName(_fromUtf8("lblResult"))
        self.pbMakeList = QtGui.QPushButton(self.centralwidget)
        self.pbMakeList.setGeometry(QtCore.QRect(50, 370, 140, 27))
        self.pbMakeList.setObjectName(_fromUtf8("pbMakeList"))
        self.chkSubFolders = QtGui.QCheckBox(self.centralwidget)
        self.chkSubFolders.setGeometry(QtCore.QRect(440, 340, 140, 22))
        self.chkSubFolders.setObjectName(_fromUtf8("chkSubFolders"))
        self.pbResults = QtGui.QPushButton(self.centralwidget)
        self.pbResults.setGeometry(QtCore.QRect(440, 370, 110, 27))
        self.pbResults.setObjectName(_fromUtf8("pbResults"))
        self.pbClose = QtGui.QPushButton(self.centralwidget)
        self.pbClose.setGeometry(QtCore.QRect(440, 410, 110, 27))
        self.pbClose.setObjectName(_fromUtf8("pbClose"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pbClose, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "File type count", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFileSearch.setText(QtGui.QApplication.translate("MainWindow", "1. Enter initial filepath to search", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFileCombo.setText(QtGui.QApplication.translate("MainWindow", "2. Select filepath to search", None, QtGui.QApplication.UnicodeUTF8))
        self.lblResult.setText(QtGui.QApplication.translate("MainWindow", "3. File count output", None, QtGui.QApplication.UnicodeUTF8))
        self.pbMakeList.setText(QtGui.QApplication.translate("MainWindow", "Make directory list", None, QtGui.QApplication.UnicodeUTF8))
        self.chkSubFolders.setText(QtGui.QApplication.translate("MainWindow", "inc Sub-folders?", None, QtGui.QApplication.UnicodeUTF8))
        self.pbResults.setText(QtGui.QApplication.translate("MainWindow", "Get file count", None, QtGui.QApplication.UnicodeUTF8))
        self.pbClose.setText(QtGui.QApplication.translate("MainWindow", "Close form", None, QtGui.QApplication.UnicodeUTF8))

