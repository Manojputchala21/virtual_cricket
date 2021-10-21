# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets
from create import Ui_createteam as createTeam
from open import Ui_Form as openTeam



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 6, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 6, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 4, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 6, 2, 1, 1)
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setAutoFillBackground(False)
        self.label1.setTextFormat(QtCore.Qt.AutoText)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpenTeam = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setBold(True)
        font.setWeight(75)
        self.actionOpenTeam.setFont(font)
        self.actionOpenTeam.setObjectName("actionOpenTeam")
        self.actionCreate_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setBold(True)
        font.setWeight(75)
        self.actionCreate_Team.setFont(font)
        self.actionCreate_Team.setObjectName("actionCreate_Team")
        self.menuManage_Teams.addAction(self.actionOpenTeam)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionCreate_Team)
        self.menuManage_Teams.addSeparator()
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Click On Manage Teams and Create new team..."))
        self.label1.setText(_translate("MainWindow", "W E L C O M E"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#00aa00;\">Fantasy Cricket Game!!</span></p></body></html>"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionOpenTeam.setText(_translate("MainWindow", "OpenTeam"))
        self.actionCreate_Team.setText(_translate("MainWindow", "Create Team"))
        self.actionCreate_Team.triggered.connect(self.create_teams)
        self.actionOpenTeam.triggered.connect(self.open_teams)

    def create_teams(self):
        self.create_team = QtWidgets.QWidget()
        self.create_screen = createTeam()
        self.create_screen.setupUi(self.create_team)
        self.create_team.show()
    def open_teams(self):
        self.open_team=QtWidgets.QWidget()
        self.open_screen=openTeam()
        self.open_screen.setupUi(self.open_team)
        self.open_team.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
