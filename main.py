import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_ui import *

import cv2
import numpy as np
import matplotlib.pyplot as plt

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

    # done
    def on_disparity_click(self):
    	# print('disparity_btn')
        imgL = cv2.imread('./imL.png',0)
        imgR = cv2.imread('./imR.png',0)

        stereo = cv2.StereoBM_create(numDisparities=64, blockSize=9)
        disparity = stereo.compute(imgL,imgR)
        plt.imshow(disparity,'gray')
        plt.show()

        cv2.waitKey()
        cv2.destroyAllWindows()

    # done
    def on_ncc_click(self):
    	# print('ncc_btn')
        img_rgb = cv2.imread('./ncc_img.jpg')
        img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
        img = cv2.imread('./ncc_img.jpg', 0)
        tmp = cv2.imread('./ncc_template.jpg', 0)
        w, h = tmp.shape[::-1]

        res = cv2.matchTemplate(img, tmp, cv2.TM_CCORR_NORMED)
        threshold = 0.999
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

        plt.subplot(121),plt.imshow(img_rgb)
        plt.title('ncc_img.jpg'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(res, cmap = 'gray')
        plt.title('tamplate matching feature'), plt.xticks([]), plt.yticks([])
        plt.suptitle('CCN')
        plt.show()

        cv2.waitKey()
        cv2.destroyAllWindows()

    def on_keypoints_click(self):
    	# print('keypoints_btn')
        img1 = cv2.imread('./Aerial1.jpg', 0)
        img2 = cv2.imread('./Aerial2.jpg', 0)

        sift = cv2.xfeatures2d.SIFT_create()
        kp1 = sift.detect(img1, None)
        kp2 = sift.detect(img2, None)

        kp1 = sorted(kp1, key = lambda x:x.size, reverse=True)
        kp2 = sorted(kp2, key = lambda x:x.size, reverse=True)

        img1 = cv2.drawKeypoints(img1, kp1[:7], img1)
        img2 = cv2.drawKeypoints(img2, kp2[:7], img2)

        cv2.imshow('FeatureArial1.jpg',img1)
        cv2.imshow('FeatureArial2.jpg', img2)

        cv2.waitKey()
        cv2.destroyAllWindows()

    def on_matchKeypoints_click(self):
    	# print('matchKeypoints_btn')
        img1 = cv2.imread('./Aerial1.jpg', 0)
        img2 = cv2.imread('./Aerial2.jpg', 0)

        sift = cv2.xfeatures2d.SIFT_create()
        kp1 = sift.detect(img1, None)
        kp2 = sift.detect(img2, None)

        kp1 = sorted(kp1, key = lambda x:x.size, reverse=True)
        kp2 = sorted(kp2, key = lambda x:x.size, reverse=True)

        kp1, descriptors_1 = sift.compute(img1, kp1[:7])
        kp2, descriptors_2 = sift.compute(img2, kp2[:7])
        
        bf_matcher = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
        matches = bf_matcher.match(descriptors_1, descriptors_2)

        for m in matches:
            if m.distance > 2000:  # this parameter affects the result filtering
                matches.pop(matches.index(m))
                # print(m.queryIdx)

        match_img = cv2.drawMatches(img1, kp1, img2, kp2, matches, None, (0, 255, 0), (255, 0, 0),flags=0)

        cv2.imshow('Matched keypoints',match_img)

        cv2.waitKey()
        cv2.destroyAllWindows()

    	


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())