import cv2
import os

class Camera():
    def __init__(self):
        self.vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        path = "Generator/Codes/0.png"
        self.testImage = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    def __del__(self):
        self.vid.release()

    def getFrame(self):
        ret, frame = self.vid.read()
        return frame

    def getTestImage(self):
        return self.testImage

