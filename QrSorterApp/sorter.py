import cv2
import camera
import RPi.GPIO as GPIO
from dataAccess import Database  
from qrFinder import *
from servo import *

class Sorter:
    def __init__(self):
        servoLeft = Servo(19, 1, True)
        servoRight = Servo(26, 2, False)
        self.servos = [servoLeft, servoRight]
        self.cam = camera.Camera()
        self.db = Database()
        self.categories = self.db.getCategories()
        self.closed = False
        self.servoToOpen = None

    def close(self):
        if self.closed:
            self.servoToOpen.open()
            self.closed = False
            self.servoToOpen = None

    def sort(self):
        self.closed = False
        self.servoToOpen = None
        frame = self.cam.getFrame()
        qrData = findQRData(frame)
        print(qrData)
        
        if qrData != '':
            for c in self.categories:
                if c[1] == qrData:
                    for servo in self.servos:
                        if servo.boxId == c[3]:
                            print(c[3])
                            servo.close()
                            self.closed = True
                            self.servoToOpen = servo
                            break
                    if self.closed:
                        break
            return True
        else:
            return False        