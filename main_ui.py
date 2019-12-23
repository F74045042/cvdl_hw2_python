# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 281, 151))
        self.groupBox.setObjectName("groupBox")
        self.disparity_btn = QtWidgets.QPushButton(self.groupBox)
        self.disparity_btn.setGeometry(QtCore.QRect(20, 40, 200, 50))
        self.disparity_btn.setObjectName("disparity_btn")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 190, 281, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.ncc_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ncc_btn.setGeometry(QtCore.QRect(20, 40, 200, 50))
        self.ncc_btn.setObjectName("ncc_btn")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(340, 30, 221, 301))
        self.groupBox_3.setObjectName("groupBox_3")
        self.keypoints_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.keypoints_btn.setGeometry(QtCore.QRect(10, 30, 200, 50))
        self.keypoints_btn.setObjectName("keypoints_btn")
        self.matchKeypoints_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.matchKeypoints_btn.setGeometry(QtCore.QRect(10, 90, 200, 50))
        self.matchKeypoints_btn.setObjectName("matchKeypoints_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cv2019_Hw2"))
        self.groupBox.setTitle(_translate("MainWindow", "1. Stereo"))
        self.disparity_btn.setText(_translate("MainWindow", "1.1 Disparity"))
        self.groupBox_2.setTitle(_translate("MainWindow", "2. Normalized Cross Correlation"))
        self.ncc_btn.setText(_translate("MainWindow", "2.1 NCC"))
        self.groupBox_3.setTitle(_translate("MainWindow", "3. SIFT"))
        self.keypoints_btn.setText(_translate("MainWindow", "3.1 Keypoints"))
        self.matchKeypoints_btn.setText(_translate("MainWindow", "3.2 Matched keypoints"))

