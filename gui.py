import random

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QSizePolicy, QWidget, \
    QPushButton, QFileDialog, QLineEdit, QCheckBox, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from Main import *


class Ui_MainWindow(object):

    def __init__(self):
        self.gridFile = ""
        self.orderFile = ""
        self.itemFile = ""
        self.LoadPickle = False
        self.countEffort=False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 397)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(290, 0, 341, 321))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.ResultTextEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget_6)
        self.ResultTextEdit.setObjectName("ResultTextEdit")
        self.verticalLayout_6.addWidget(self.ResultTextEdit)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 0, 245, 269))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.orderFileBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.orderFileBtn.setObjectName("orderFileBtn")
        self.verticalLayout_2.addWidget(self.orderFileBtn)
        self.orderTextbox = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.orderTextbox.setObjectName("orderTextbox")
        self.verticalLayout_2.addWidget(self.orderTextbox)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridFileBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.gridFileBtn.setObjectName("gridFileBtn")
        self.verticalLayout.addWidget(self.gridFileBtn)
        self.gridTextbox = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.gridTextbox.setObjectName("gridTextbox")
        self.verticalLayout.addWidget(self.gridTextbox)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.itemFileBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.itemFileBtn.setObjectName("itemFileBtn")
        self.verticalLayout_3.addWidget(self.itemFileBtn)
        self.itemTextbox = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.itemTextbox.setObjectName("itemTextbox")
        self.verticalLayout_3.addWidget(self.itemTextbox)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.EffortcheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_5)
        self.EffortcheckBox.setChecked(False)
        self.EffortcheckBox.setObjectName("EffortcheckBox")
        self.horizontalLayout.addWidget(self.EffortcheckBox)
        self.LoadPicklecheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_5)
        self.LoadPicklecheckBox.setChecked(False)
        self.LoadPicklecheckBox.setObjectName("LoadPicklecheckBox")
        self.horizontalLayout.addWidget(self.LoadPicklecheckBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 280, 276, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.runSingle = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.runSingle.setObjectName("runSingle")
        self.horizontalLayout_2.addWidget(self.runSingle)
        self.runBatch = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.runBatch.setObjectName("runBatch")
        self.horizontalLayout_2.addWidget(self.runBatch)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)


        self.orderFileBtn.clicked.connect(lambda: self.openFileDialog("orderFile"))
        self.gridFileBtn.clicked.connect(lambda: self.openFileDialog("gridFile"))
        self.itemFileBtn.clicked.connect(lambda: self.openFileDialog("itemFile"))
        self.LoadPicklecheckBox.stateChanged.connect(lambda: self.btnstate(self.LoadPicklecheckBox))
        self.EffortcheckBox.stateChanged.connect(lambda: self.btnstate(self.EffortcheckBox))
        self.runSingle.clicked.connect(self.runsingle)
        self.runBatch.clicked.connect(self.runbatch)
        # self.runBatch.clicked.connect(self.testOpenWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def testOpenWindow(self):
        self.newWindows=Matplot_Window()
        self.newWindows.show()

    def runsingle(self):
        result=mainTSPforUi(LoadPickle=self.LoadPickle, itemFile=self.itemFile,
                     warehouseGridFile=self.gridFile,countEffort=self.countEffort)
        self.ResultTextEdit.setText(result)

    def runbatch(self):
        self.ResultTextEdit.setText(mainTSPforUi(LoadPickle=self.LoadPickle, itemFile=self.itemFile,
                                                 warehouseGridFile=self.gridFile, orderlist=self.orderFile,
                                                 countEffort=self.countEffort))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EECS 221"))
        self.label_2.setText(_translate("MainWindow", "Result"))
        self.orderFileBtn.setText(_translate("MainWindow", "Select oder file"))
        self.gridFileBtn.setText(_translate("MainWindow", "Select grid file"))
        self.itemFileBtn.setText(_translate("MainWindow", "Select item file"))
        self.EffortcheckBox.setText(_translate("MainWindow", "Effort"))
        self.LoadPicklecheckBox.setText(_translate("MainWindow", "Load Pickle"))
        self.runSingle.setText(_translate("MainWindow", "Run Single Order"))
        self.runBatch.setText(_translate("MainWindow", "Run Batch Order"))

    def btnstate(self, b):
        if b.text() == "Load Pickle":
            if b.isChecked() == True:
                print(b.text() + " is selected")
                self.LoadPickle = True
            else:
                print(b.text() + " is deselected")
                self.LoadPickle = False

        elif b.text() == "Effort":
            if b.isChecked() == True:
                print(b.text() + " is selected")
                self.countEffort=True
            else:
                print(b.text() + " is deselected")
                self.countEffort=False

    def openFileDialog(self, fileVar):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName()

        if fileName:
            if fileVar == "gridFile":
                self.gridFile = fileName
                self.gridTextbox.setText(fileName)
                print(self.gridFile)
            elif fileVar == "orderFile":
                self.orderFile = fileName
                self.orderTextbox.setText(fileName)
            elif fileVar == "itemFile":
                self.itemFile = fileName
                self.itemTextbox.setText(fileName)


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()


class Matplot_Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Matplot_Window, self).__init__(parent)

        self.main_widget = QtWidgets.QWidget(self)
        l = QtWidgets.QVBoxLayout(self.main_widget)
        sc = PlotCanvas(self.main_widget, width=5, height=4, dpi=100)
        dc = PlotCanvas(self.main_widget, width=5, height=4, dpi=100)
        l.addWidget(sc)
        l.addWidget(dc)
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())