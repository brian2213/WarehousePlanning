from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QSizePolicy, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from Main import *


class Ui_MainWindow(object):

    def __init__(self):
        self.gridFile = ""
        self.orderFile = ""
        self.itemFile = ""
        self.LoadPickle = False
        self.countEffort = False

        self.modelChanged = True
        self.wareHouse = None

        self.start = "0*0"
        self.end = "0*0"
        self.startOrEndChanged = True

        self.orders = []
        self.numberOfWindows=0

        self.combinedOrder = []
        self.splitedOrder = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(756, 543)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalWidget_2 = QtWidgets.QWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget_2.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_2.setSizePolicy(sizePolicy)
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.gridFileBtn = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.gridFileBtn.setObjectName("gridFileBtn")
        self.gridLayout.addWidget(self.gridFileBtn, 0, 0, 1, 1)
        self.gridTextbox = QtWidgets.QLineEdit(self.horizontalWidget_2)
        self.gridTextbox.setObjectName("gridTextbox")
        self.gridLayout.addWidget(self.gridTextbox, 0, 1, 1, 1)
        self.itemFileBtn = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.itemFileBtn.setObjectName("itemFileBtn")
        self.gridLayout.addWidget(self.itemFileBtn, 1, 0, 1, 1)
        self.itemTextbox = QtWidgets.QLineEdit(self.horizontalWidget_2)
        self.itemTextbox.setObjectName("itemTextbox")
        self.gridLayout.addWidget(self.itemTextbox, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.LoadPicklecheckBox = QtWidgets.QCheckBox(self.horizontalWidget_2)
        self.LoadPicklecheckBox.setChecked(False)
        self.LoadPicklecheckBox.setObjectName("LoadPicklecheckBox")
        self.gridLayout_2.addWidget(self.LoadPicklecheckBox, 0, 0, 1, 1)
        self.EffortcheckBox = QtWidgets.QCheckBox(self.horizontalWidget_2)
        self.EffortcheckBox.setChecked(False)
        self.EffortcheckBox.setObjectName("EffortcheckBox")
        self.gridLayout_2.addWidget(self.EffortcheckBox, 0, 1, 1, 1)
        self.CombineOrderCheckBox = QtWidgets.QCheckBox(self.horizontalWidget_2)
        self.CombineOrderCheckBox.setObjectName("CombineOrderCheckBox")
        self.gridLayout_2.addWidget(self.CombineOrderCheckBox, 0, 2, 1, 1)
        self.maxWeightLabel = QtWidgets.QLabel(self.horizontalWidget_2)
        self.maxWeightLabel.setObjectName("maxWeightLabel")
        self.gridLayout_2.addWidget(self.maxWeightLabel, 1, 0, 1, 1)
        self.maxWeightLineEdit = QtWidgets.QLineEdit(self.horizontalWidget_2)
        self.maxWeightLineEdit.setObjectName("maxWeightLineEdit")
        self.gridLayout_2.addWidget(self.maxWeightLineEdit, 1, 1, 1, 1)
        self.WeightLimitCheckBox = QtWidgets.QCheckBox(self.horizontalWidget_2)
        self.WeightLimitCheckBox.setObjectName("WeightLimitCheckBox")
        self.gridLayout_2.addWidget(self.WeightLimitCheckBox, 1, 2, 1, 1)
        self.startNodeLabel = QtWidgets.QLabel(self.horizontalWidget_2)
        self.startNodeLabel.setObjectName("startNodeLabel")
        self.gridLayout_2.addWidget(self.startNodeLabel, 2, 0, 1, 1)
        self.startNodeLineEdit = QtWidgets.QLineEdit(self.horizontalWidget_2)
        self.startNodeLineEdit.setObjectName("startNodeLineEdit")
        self.gridLayout_2.addWidget(self.startNodeLineEdit, 2, 1, 1, 1)
        self.startNodeLineEdit_2 = QtWidgets.QLineEdit(self.horizontalWidget_2)
        self.startNodeLineEdit_2.setObjectName("startNodeLineEdit_2")
        self.gridLayout_2.addWidget(self.startNodeLineEdit_2, 2, 2, 1, 1)
        self.endNodeLabel = QtWidgets.QLabel(self.horizontalWidget_2)
        self.endNodeLabel.setObjectName("endNodeLabel")
        self.gridLayout_2.addWidget(self.endNodeLabel, 3, 0, 1, 1)
        self.endNodeLineEdit = QtWidgets.QLineEdit(self.horizontalWidget_2)
        self.endNodeLineEdit.setObjectName("endNodeLineEdit")
        self.gridLayout_2.addWidget(self.endNodeLineEdit, 3, 1, 1, 1)
        self.endNodeLineEdit_2 = QtWidgets.QLineEdit(self.horizontalWidget_2)
        self.endNodeLineEdit_2.setObjectName("endNodeLineEdit_2")
        self.gridLayout_2.addWidget(self.endNodeLineEdit_2, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.orderFileBtn = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.orderFileBtn.setObjectName("orderFileBtn")
        self.gridLayout_4.addWidget(self.orderFileBtn, 0, 0, 1, 2)
        self.orderTextbox = QtWidgets.QLineEdit(self.horizontalWidget_2)
        self.orderTextbox.setObjectName("orderTextbox")
        self.gridLayout_4.addWidget(self.orderTextbox, 0, 2, 1, 2)
        self.OrderComboBox = QtWidgets.QComboBox(self.horizontalWidget_2)
        self.OrderComboBox.setObjectName("OrderComboBox")
        self.gridLayout_4.addWidget(self.OrderComboBox, 0, 4, 1, 1)
        self.orderLabel = QtWidgets.QLabel(self.horizontalWidget_2)
        self.orderLabel.setObjectName("orderLabel")
        self.gridLayout_4.addWidget(self.orderLabel, 1, 0, 1, 1)
        self.orderLineEdit = QtWidgets.QLineEdit(self.horizontalWidget_2)
        self.orderLineEdit.setObjectName("orderLineEdit")
        self.gridLayout_4.addWidget(self.orderLineEdit, 1, 1, 1, 3)
        self.runSingle = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.runSingle.setObjectName("runSingle")
        self.gridLayout_4.addWidget(self.runSingle, 1, 4, 1, 1)
        self.WeightOrganizeButton = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.WeightOrganizeButton.setObjectName("WeightOrganizeButton")
        self.gridLayout_4.addWidget(self.WeightOrganizeButton, 2, 0, 1, 2)
        self.ModeComboBox = QtWidgets.QComboBox(self.horizontalWidget_2)
        self.ModeComboBox.setObjectName("ModeComboBox")
        self.ModeComboBox.addItem("")
        self.ModeComboBox.addItem("")
        self.ModeComboBox.addItem("")
        self.gridLayout_4.addWidget(self.ModeComboBox, 2, 2, 1, 1)
        self.runBatch = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.runBatch.setObjectName("runBatch")
        self.gridLayout_4.addWidget(self.runBatch, 2, 3, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.singleOrderLabel_2 = QtWidgets.QLabel(self.horizontalWidget_2)
        self.singleOrderLabel_2.setObjectName("singleOrderLabel_2")
        self.gridLayout_3.addWidget(self.singleOrderLabel_2, 0, 0, 1, 1)
        self.OrderSplitComboBox = QtWidgets.QComboBox(self.horizontalWidget_2)
        self.OrderSplitComboBox.setObjectName("OrderSplitComboBox")
        self.gridLayout_3.addWidget(self.OrderSplitComboBox, 0, 1, 1, 1)
        self.SingleTripButton = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.SingleTripButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.SingleTripButton, 0, 2, 1, 1)
        self.batchOrderLabel_3 = QtWidgets.QLabel(self.horizontalWidget_2)
        self.batchOrderLabel_3.setObjectName("batchOrderLabel_3")
        self.gridLayout_3.addWidget(self.batchOrderLabel_3, 1, 0, 1, 1)
        self.OrderCombineComboBox = QtWidgets.QComboBox(self.horizontalWidget_2)
        self.OrderCombineComboBox.setObjectName("OrderCombineComboBox")
        self.gridLayout_3.addWidget(self.OrderCombineComboBox, 1, 1, 1, 1)
        self.SingleTripButton_Batch = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.SingleTripButton_Batch.setObjectName("SingleTripButton_2")
        self.gridLayout_3.addWidget(self.SingleTripButton_Batch, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.horizontalWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.ResultTextEdit = QtWidgets.QTextEdit(self.horizontalWidget_2)
        self.ResultTextEdit.setReadOnly(True)
        self.ResultTextEdit.setObjectName("ResultTextEdit")
        self.verticalLayout_6.addWidget(self.ResultTextEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout_5.addWidget(self.horizontalWidget_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 756, 22))
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

        self.startNodeLineEdit.textChanged.connect(self.chageNode)
        self.startNodeLineEdit_2.textChanged.connect(self.chageNode)
        self.endNodeLineEdit.textChanged.connect(self.chageNode)
        self.endNodeLineEdit_2.textChanged.connect(self.chageNode)
        self.OrderComboBox.currentIndexChanged.connect(self.orderChanged)


        self.runSingle.clicked.connect(lambda :self.runsingle(orders=self.orderLineEdit.text(),TripReset=True))
        self.runBatch.clicked.connect(self.runbatch)
        self.SingleTripButton.clicked.connect(lambda :self.runsingle(orders=" ".join(self.splitedOrder[self.OrderSplitComboBox.currentIndex()])))
        self.SingleTripButton_Batch.clicked.connect(lambda :self.runsingle(orders=" ".join(self.combinedOrder[self.OrderCombineComboBox.currentIndex()])))

        # This small code section is for debug easier
        self.gridTextbox.setText(
            "/Users/Brian/Documents/UCI/EECS 221 Advanced Algorith Application/HW5/bin/warehouse-grid.csv")
        self.gridFile = self.gridTextbox.text()
        self.orderTextbox.setText(
            "/Users/Brian/Documents/UCI/EECS 221 Advanced Algorith Application/HW5/bin/warehouse-orders-v02-tabbed.txt")
        self.orderFile = self.orderTextbox.text()
        self.itemTextbox.setText(
            "/Users/Brian/Documents/UCI/EECS 221 Advanced Algorith Application/HW5/bin/item-dimensions-tabbed.txt")
        self.itemFile = self.itemTextbox.text()
        self.readOrder(self.orderFile)
        self.orderChanged(0)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def orderChanged(self, i):
        if i < len(self.orders):
            self.orderLineEdit.setText(" ".join(self.orders[i]))

    def readOrder(self, file):

        with open(file, 'r') as f:
            orders = []
            i = 1
            self.OrderComboBox.clear()
            for line in f:
                orders.append(line.split())
                self.OrderComboBox.addItem("#Order " + str(i))
                i += 1

            self.orders = orders

    def DrawResult(self, model=None, points=[], title="route"):
        if model == None:
            return
        self.newWindows = Matplot_Window(model=model, points=points, title=title)
        self.newWindows.show()

    def chageNode(self):
        self.startOrEndChanged = True

    def runsingle(self,orders="",TripReset=False):

        if self.ModeComboBox.currentText() == "Left":
            leftMode = True
            rightMode = False
        elif self.ModeComboBox.currentText() == "Right":
            leftMode = False
            rightMode = True
        else:
            leftMode = True
            rightMode = True

        if self.wareHouse is None or self.modelChanged or self.startOrEndChanged:
            startNode = self.startNodeLineEdit.text() + "*" + self.startNodeLineEdit_2.text()
            endNode = self.endNodeLineEdit.text() + "*" + self.endNodeLineEdit_2.text()

            self.wareHouse = mainWareHouse(warehouseGridFile=self.gridFile, itemFile=self.itemFile,
                                           LoadPickle=self.LoadPickle, startNode=startNode, endNode=endNode)
            # result=mainTSPforUi(LoadPickle=self.LoadPickle, itemFile=self.itemFile,
            #              warehouseGridFile=self.gridFile,countEffort=self.countEffort)
            self.modelChanged = False
            self.startOrEndChanged = False

        if self.maxWeightLineEdit.text().isdigit():
            maxWeight = int(self.maxWeightLineEdit.text())
        else:
            maxWeight = sys.maxsize
            self.maxWeightLineEdit.setText("System maximum value")

        content = self.wareHouse.runSolver(countEffort=self.countEffort, leftMode=leftMode, rightMode=rightMode,
                                           orders=orders, maxWeight=maxWeight,
                                           CombineOrder=self.CombineOrderCheckBox.isChecked(),
                                           WeightLimit=self.WeightLimitCheckBox.isChecked())

        self.ResultTextEdit.setText(content)

        if self.WeightLimitCheckBox.isChecked() and TripReset:
            self.splitedOrder=self.wareHouse.solver.splitedOrder
            self.OrderSplitComboBox.clear()
            for i in range(len(self.splitedOrder)):
                self.OrderSplitComboBox.addItem("#Trip " + str(i+1))

        i=1
        for point in self.wareHouse.solver.originRoutePoints:
            exec("self.newWindows"+str(i)+" = Matplot_Window(model=self.wareHouse.model, points=point,title='Original Route Trip"+str(i)+"')")
            exec("self.newWindows"+str(i)+".show()")
            i+=1
        j=i
        i=1
        for point in self.wareHouse.solver.routePoints:
            exec("self.newWindows"+str(i+j)+" = Matplot_Window(model=self.wareHouse.model, points=point,title='Optimized Route Trip"+str(i)+"')")
            exec("self.newWindows"+str(i+j)+".show()")
            i+=1
        # setattr(self, "original", newWindows)
        # self.newWindows2 = Matplot_Window(model=self.wareHouse.model, points=self.wareHouse.solver.routePoints,
        #                                   title="Optimized Route")
        # self.newWindows2.show()

    def runbatch(self):

        if self.ModeComboBox.currentText() == "Left":
            leftMode = True
            rightMode = False
        elif self.ModeComboBox.currentText() == "Right":
            leftMode = False
            rightMode = True
        else:
            leftMode = True
            rightMode = True

        if self.wareHouse is None or self.modelChanged or self.startOrEndChanged:
            startNode = self.startNodeLineEdit.text() + "*" + self.startNodeLineEdit_2.text()
            endNode = self.endNodeLineEdit.text() + "*" + self.endNodeLineEdit_2.text()

            self.wareHouse = mainWareHouse(warehouseGridFile=self.gridFile, itemFile=self.itemFile,
                                           LoadPickle=self.LoadPickle, startNode=startNode, endNode=endNode)
            # result=mainTSPforUi(LoadPickle=self.LoadPickle, itemFile=self.itemFile,
            #              warehouseGridFile=self.gridFile,countEffort=self.countEffort)
            self.modelChanged = False
            self.startOrEndChanged = False

        if self.maxWeightLineEdit.text().isdigit():
            maxWeight = int(self.maxWeightLineEdit.text())
        else:
            maxWeight = sys.maxsize
            self.maxWeightLineEdit.setText("System maximum value")

        content = self.wareHouse.runSolver(countEffort=self.countEffort, leftMode=leftMode, rightMode=rightMode,
                                           orders=self.orderLineEdit.text(), maxWeight=maxWeight,
                                           CombineOrder=self.CombineOrderCheckBox.isChecked(),
                                           WeightLimit=self.WeightLimitCheckBox.isChecked(),
                                           orderlist=self.orderTextbox.text())

        self.ResultTextEdit.setText(content)

        if self.CombineOrderCheckBox.isChecked():
            self.combinedOrder=self.wareHouse.solver.combinedOrder
            self.OrderCombineComboBox.clear()
            for i in range(len(self.combinedOrder)):
                self.OrderCombineComboBox.addItem("#Trip " + str(i+1))



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EECS 221"))
        self.gridFileBtn.setText(_translate("MainWindow", "Select grid file"))
        self.itemFileBtn.setText(_translate("MainWindow", "Select item file"))
        self.LoadPicklecheckBox.setText(_translate("MainWindow", "Load Pickle"))
        self.EffortcheckBox.setText(_translate("MainWindow", "Effort"))
        self.CombineOrderCheckBox.setText(_translate("MainWindow", "combine order"))
        self.maxWeightLabel.setText(_translate("MainWindow", "max weight"))
        self.WeightLimitCheckBox.setText(_translate("MainWindow", "weight limit"))
        self.startNodeLabel.setText(_translate("MainWindow", "startNode"))
        self.startNodeLineEdit.setText(_translate("MainWindow", "0"))
        self.startNodeLineEdit_2.setText(_translate("MainWindow", "0"))
        self.endNodeLabel.setText(_translate("MainWindow", "endNode"))
        self.endNodeLineEdit.setText(_translate("MainWindow", "0"))
        self.endNodeLineEdit_2.setText(_translate("MainWindow", "0"))
        self.orderFileBtn.setText(_translate("MainWindow", "Select oder file"))
        self.orderLabel.setText(_translate("MainWindow", "Order"))
        self.runSingle.setText(_translate("MainWindow", "Run Order"))
        self.WeightOrganizeButton.setText(_translate("MainWindow", "OrganizeWeight"))
        self.ModeComboBox.setItemText(0, _translate("MainWindow", "Left"))
        self.ModeComboBox.setItemText(1, _translate("MainWindow", "Right"))
        self.ModeComboBox.setItemText(2, _translate("MainWindow", "Both"))
        self.runBatch.setText(_translate("MainWindow", "Run Batch Order"))
        self.singleOrderLabel_2.setText(_translate("MainWindow", "Order Split"))
        self.SingleTripButton.setText(_translate("MainWindow", "Show Trip"))
        self.batchOrderLabel_3.setText(_translate("MainWindow", "Order Combine"))
        self.SingleTripButton_Batch.setText(_translate("MainWindow", "Show Trip"))
        self.label_2.setText(_translate("MainWindow", "Result"))

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
                self.countEffort = True
            else:
                print(b.text() + " is deselected")
                self.countEffort = False

    def openFileDialog(self, fileVar):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName()

        if fileName:
            if fileVar == "gridFile":
                self.gridFile = fileName
                self.gridTextbox.setText(fileName)
                self.modelChanged = True
                print(self.gridFile)
            elif fileVar == "orderFile":
                self.orderFile = fileName
                self.orderTextbox.setText(fileName)
                self.readOrder(fileName)
                self.orderChanged(0)
            elif fileVar == "itemFile":
                self.itemFile = fileName
                self.itemTextbox.setText(fileName)


class plotTour(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100, model=None, points=[], title="route"):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        if model == None:
            raise Exception("No data model to draw the plot")

        minmax = model.minmax
        self.axes = fig.add_subplot(111)
        self.axes.axis(minmax)
        self.axes.grid(True)
        self.axes.set_title(title)
        self.axes.set_xticks(range(minmax[0], minmax[1], 1))
        self.axes.set_yticks(range(minmax[2], minmax[3], 1))
        for i in range(1, len(points), 1):
            x1 = [points[i - 1][0], points[i][0]]
            y1 = [points[i - 1][1], points[i][1]]
            self.axes.plot(x1, y1, marker='o')
        # self.axes.plot()


class Matplot_Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None, model=None, points=[], title="route"):
        super(Matplot_Window, self).__init__(parent)

        self.main_widget = QtWidgets.QWidget(self)
        l = QtWidgets.QVBoxLayout(self.main_widget)
        sc = plotTour(self.main_widget, width=5, height=4, dpi=100, model=model, points=points, title=title)
        # dc = plotTour(self.main_widget, width=5, height=4, dpi=100,model=model,points=points)
        l.addWidget(sc)
        # l.addWidget(dc)
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
