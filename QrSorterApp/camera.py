from time import sleep
import cv2
from qrFinder import drawQR

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

    def flushCamera(self, lock, stop):
        while True:
            with lock:
                _, frame = self.video.read()
            sleep(0.5)
            if stop():
                break

if __name__ == '__main__':
    cam = Camera()
    while(True):
        frame = cam.getFrame()
        toDraw = drawQR(frame)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
