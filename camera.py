import cv2
import numpy as np

class Camera():
    def __init__(self):
        self.vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    def __del__(self):
        self.vid.release()

    def getFrame(self):
        ret, frame = self.vid.read()
        return frame

    def display(self, image, decodedObjects):
        for decodedObject in decodedObjects:
            points = decodedObject.polygon
            if len(points) > 4 :
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                hull = list(map(tuple, np.squeeze(hull)))
            else :
                hull = points

            n = len(hull)

            for j in range(0, n):
                cv2.line(image, hull[j], hull[ (j+1) % n], (255,0,0), 3)

        return image

