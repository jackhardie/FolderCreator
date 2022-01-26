# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'foldercreator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import sys
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from PyQt5 import QtCore, QtGui, QtWidgets
from FolderList import Art, Characters, Core, Effects, Maps, MaterialLibrary, Placeables, Weapons


class Ui_Dialog(object):

    def __init__(self):
        self.folderselection = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 120)
        Dialog.setMinimumSize(QtCore.QSize(400, 120))
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(False)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 260, 22))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(280, 20, 93, 28))
        self.pushButton.clicked.connect(self.getfolder)
        self.pushButton.setObjectName("pushButton")

        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 40, 295, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.createfolder)
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.openfolder)
        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.Close)
        self.horizontalLayout.addWidget(self.pushButton_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def getfolder(self):
        print("get folder")
        root = tk.Tk()
        root.withdraw()
        self.folderselection = filedialog.askdirectory()
        self.lineEdit.setText(self.folderselection)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Folder Structure Creator"))
        self.pushButton.setText(_translate("Dialog", "Get Folder"))
        self.pushButton_2.setText(_translate("Dialog", "Create Folders"))
        self.pushButton_4.setText(_translate("Dialog", "Open"))
        self.pushButton_3.setText(_translate("Dialog", "Close"))

    def createfolder(self):
        print("create folder")
        mainsructure = ["Art", "Characters", "Core", "Effects", "Maps", "MaterialLibrary", "Placeables", "Weapons"]
        gamefolder = "GenericGameFolderRename"
        folderstruc = [Art, Characters, Core, Effects, Maps, MaterialLibrary, Placeables, Weapons]
        for i in range(0, len(folderstruc)):
            for j in range(0, len(folderstruc[i])):
                Path(self.folderselection, gamefolder, mainsructure[i], folderstruc[i][j]).mkdir(parents=True,
                                                                                                 exist_ok=True)

    def openfolder(self):
        print("open")
        folder = self.folderselection
        if folder:
            os.startfile(folder)
        else:
            return

    def Close(self):
        print("close")
        sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
