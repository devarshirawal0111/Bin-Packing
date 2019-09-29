# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.frame = QtWidgets.QFrame(self.splitter_2)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.binPackingLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("xos4 Terminus")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.binPackingLabel.setFont(font)
        self.binPackingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.binPackingLabel.setObjectName("binPackingLabel")
        self.gridLayout.addWidget(self.binPackingLabel, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.splitter_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.itemInput = QtWidgets.QLineEdit(self.frame_2)
        self.itemInput.setObjectName("itemInput")
        self.verticalLayout.addWidget(self.itemInput)
        self.maxInput = QtWidgets.QLineEdit(self.frame_2)
        self.maxInput.setObjectName("maxInput")
        self.verticalLayout.addWidget(self.maxInput)
        self.lengthInput = QtWidgets.QLineEdit(self.frame_2)
        self.lengthInput.setObjectName("lengthInput")
        self.verticalLayout.addWidget(self.lengthInput)
        self.widthInput = QtWidgets.QLineEdit(self.frame_2)
        self.widthInput.setObjectName("widthInput")
        self.verticalLayout.addWidget(self.widthInput)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.runButton = QtWidgets.QPushButton(self.frame_2)
        self.runButton.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.runButton.setFont(font)
        self.runButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.runButton.setObjectName("runButton")
        self.horizontalLayout.addWidget(self.runButton)

        '''
        self.autoButton = QtWidgets.QPushButton(self.frame_2)
        self.autoButton.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.autoButton.setFont(font)
        self.autoButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.autoButton.setObjectName("autoButton")
        self.horizontalLayout.addWidget(self.autoButton)
        '''

        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.splitter_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #self.runButton.clicked.connect(self.change)

    #def change:


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.binPackingLabel.setText(_translate("MainWindow", "2D Bin Packing"))
        self.itemInput.setPlaceholderText(_translate("MainWindow", "Input number of items here"))
        self.maxInput.setPlaceholderText(_translate("MainWindow", "Input maximum size of bin"))
        self.lengthInput.setPlaceholderText(_translate("MainWindow", "Input length of all items"))
        self.widthInput.setPlaceholderText(_translate("MainWindow", "Input width of all items"))
        self.runButton.setText(_translate("MainWindow", "Run"))
        #self.autoButton.setText(_translate("MainWindow","Auto"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

