import random

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QSizePolicy, QWidget, \
    QPushButton, QFileDialog, QLineEdit, QCheckBox, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from Main import *


class App(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()
        self.title = 'EECS 221 Adv Alg App'
        self.left = 10
        self.top = 10
        self.width = 820
        self.height = 480
        self.initUI()

        self.gridFile = ""
        self.orderFile = ""
        self.itemFile = ""

        self.LoadPickle = False
        self.countEffort=False

    def initUI(self):

        gridFileBtn = QPushButton('Select grid file', self)
        gridFileBtn.setToolTip('Select grid file')
        gridFileBtn.move(0, 30)
        gridFileBtn.clicked.connect(lambda: self.openFileDialog("gridFile"))

        orderFileBtn = QPushButton('Select order file', self)
        orderFileBtn.setToolTip('Select order file')
        orderFileBtn.move(0, 110)
        orderFileBtn.clicked.connect(lambda: self.openFileDialog("orderFile"))

        itemFileBtn = QPushButton('Select item file', self)
        itemFileBtn.setToolTip('Select item file')
        itemFileBtn.move(0, 200)
        itemFileBtn.clicked.connect(lambda: self.openFileDialog("itemFile"))


        runSingleBtn = QPushButton('Run Single Order', self)
        runSingleBtn.setToolTip('Run Single Order')
        runSingleBtn.move(0, 400)
        # runSingleBtn.clicked.connect(lambda: self.openFileDialog("itemFile"))

        runBatchBtn = QPushButton('Run Batch Order', self)
        runBatchBtn.setToolTip('Run Batch Order')
        runBatchBtn.move(0, 430)
        # runBatchBtn.clicked.connect(lambda: self.openFileDialog("itemFile"))

        self.gridTextbox = QLineEdit(self)
        self.gridTextbox.move(10, 60)
        self.gridTextbox.resize(150, 20)

        self.orderTextbox = QLineEdit(self)
        self.orderTextbox.move(10, 150)
        self.orderTextbox.resize(150, 20)

        self.itemTextbox = QLineEdit(self)
        self.itemTextbox.move(10, 230)
        self.itemTextbox.resize(150, 40)

        self.CostLabel = QLabel(self)
        self.CostLabel.setText('Cost')
        self.CostLabel.move(10, 530)
        # self.CostLabel.resize(150, 20)

        self.CostTextbox = QLineEdit(self)
        self.CostTextbox.move(10, 550)
        self.CostTextbox.resize(150, 20)

        self.LoadPicklecheckBox = QCheckBox('LoadPickle', self)
        self.LoadPicklecheckBox.move(10, 300)
        self.LoadPicklecheckBox.stateChanged.connect(lambda :self.btnstate(self.LoadPicklecheckBox))
        self.LoadPicklecheckBox.toggle()

        self.EffortcheckBox = QCheckBox('Effort', self)
        self.EffortcheckBox.move(10, 350)
        self.EffortcheckBox.stateChanged.connect(lambda :self.btnstate(self.EffortcheckBox))
        self.EffortcheckBox.toggle()

        # self.orderFileBtn.clicked.connect(lambda: self.openFileDialog("orderFile"))
        # self.gridFileBtn.clicked.connect(lambda: self.openFileDialog("gridFile"))
        # self.itemFileBtn.clicked.connect(lambda: self.openFileDialog("itemFile"))
        # self.LoadPicklecheckBox.stateChanged.connect(lambda: self.btnstate(self.LoadPicklecheckBox))
        # self.EffortcheckBox.stateChanged.connect(lambda: self.btnstate(self.EffortcheckBox))

        m = PlotCanvas(self)
        m.move(200, 30)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def btnstate(self,b):
        if b.text() == "LoadPickle":
            if b.isChecked() == True:
                print(b.text() + " is selected")
            else:
                print(b.text() + " is deselected")

        elif b.text() == "Effort":
            if b.isChecked() == True:
                print(b.text() + " is selected")
            else:
                print(b.text() + " is deselected")

    def openFileDialog(self, fileVar):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
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

    def on_click(self):
        print("hello")


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

        # m = PlotCanvas(MainWindow)
        # m.move(300, 30)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def runsingle(self):
        self.ResultTextEdit.setText(mainTSPforUi(LoadPickle=self.LoadPickle, itemFile=self.itemFile,
                     warehouseGridFile=self.gridFile,countEffort=self.countEffort))

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
if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # ex = App()
    # sys.exit(app.exec_())

    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())