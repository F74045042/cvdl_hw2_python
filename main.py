import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_ui import *
import cv2

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.onBindingUI()

    def onBindingUI(self):
    	self.disparity_btn.clicked.connect(self.on_disparity_click)
    	self.ncc_btn.clicked.connect(self.on_ncc_click)
    	self.keypoints_btn.clicked.connect(self.on_keypoints_click)
    	self.matchKeypoints_btn.clicked.connect(self.on_matchKeypoints_click)

    def on_disparity_click(self):
    	# print('disparity_btn')
        imgL = cv2.imread('./imL.png')
        imgR = cv2.imread('./imR.png')

        cv2.imshow('imgL', imgL)
        cv2.imshow('imgR', imgR)
        
        cv2.waitKey()
        cv2.destroyAllWindows()

    def on_ncc_click(self):
    	print('ncc_btn')

    def on_keypoints_click(self):
    	print('keypoints_btn')

    def on_matchKeypoints_click(self):
    	print('matchKeypoints_btn')
    	


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())