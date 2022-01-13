from dataAccess import Database  
from qrFinder import *
from servo import *

class Sorter:
    def __init__(self, cam):
        servoLeft = Servo(19, 1, True, 2)
        servoRight = Servo(20, 2, False)
        self.servos = [servoLeft, servoRight]
        self.cam = cam
        self.db = Database()
        self.db.resetCategoriesCounters()
        self.categories = self.db.getCategories()
        self.closed = False
        self.servoToOpen = None

    def open(self):
        if self.closed:
            self.servoToOpen.open()
            self.closed = False
            self.servoToOpen = None

    def sort(self):
        self.closed = False
        self.servoToOpen = None
        frame = self.cam.getFrame()
        qrData = findQRData(frame)
        
        if qrData != '':
            for c in self.categories:
                if c[1] == qrData:
                    for servo in self.servos:
                        if servo.boxId == c[3]:
                            servo.close()
                            self.closed = True
                            self.servoToOpen = servo
                            self.db.updateCategory(c[0], c[1], c[2] + 1, c[3])
                            self.categories = self.db.getCategories()
                            break

                    if self.closed:
                        break
            return True
        else:
            return False
