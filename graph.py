# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'font2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('QT5Agg')




class Ui_graphWindow(object):
    def setupUi(self, graphWindow):
        graphWindow.setObjectName("graphWindow")
        graphWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(graphWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.backButton = QtWidgets.QPushButton(self.frame)
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        #pitch = pitch = [0.79, 0.5, 0.33, 0.28, 0.35]

        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        #self.graphArea = PlotWidget(self.frame_2)
        #self.graphArea.setObjectName("graphArea")
        self.graphArea = plt.figure()
        self.canvas = Canvas(self.graphArea)


        #plt.show()
        #self.canvas.draw()


        #pw = pg.Plot
        #self.graphArea.plot(pitch)
        #self.graphArea


        self.gridLayout_2.addWidget(self.canvas, 0, 0, 1, 1)

        #self.graphArea.plot(pitch)

        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        graphWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(graphWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        graphWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(graphWindow)
        self.statusbar.setObjectName("statusbar")
        graphWindow.setStatusBar(self.statusbar)

        self.retranslateUi(graphWindow)
        QtCore.QMetaObject.connectSlotsByName(graphWindow)



    def retranslateUi(self, graphWindow):
        _translate = QtCore.QCoreApplication.translate
        graphWindow.setWindowTitle(_translate("graphWindow", "Graph"))
        self.backButton.setText(_translate("graphWindow", "Back"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    graph = QtWidgets.QMainWindow()
    ui = Ui_graphWindow()
    ui.setupUi(graph)
    graph.show()
    sys.exit(app.exec_())