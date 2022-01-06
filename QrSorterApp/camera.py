import cv2

class Camera():
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.video.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        path = 'Generator/Codes/0.png'
        self.testImage = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    def __del__(self):
        self.video.release()

    def getFrame(self):
        _, frame = self.video.read()
        return frame

    def getTestImage(self):
        return self.testImage
