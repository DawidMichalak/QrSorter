import cv2
import camera
import RPi.GPIO as GPIO
from dataAccess import Database  
from qrFinder import *
from servo import *

if __name__ == "__main__":
    cam = camera.Camera()
    servoLeft = Servo(19, 1, True)
    servoRight = Servo(26, 2, False)
    servos = [servoLeft, servoRight]
    db = Database()
    categories = db.getCategories()

    try:
        while(True):
            closed = False
            servoToOpen = None
            cam.getFrame()
            frame = cam.getFrame()
            cv2.imshow('frame', frame)
            qrData = findQRData(frame)
            print(qrData)
            for c in categories:
                if c[1] == qrData:
                    for servo in servos:
                        if servo.boxId == c[3]:
                            print(c[3])
                            servo.close()
                            closed = True
                            servoToOpen = servo
                            break
                    if closed:
                        break
            if closed:
                servoToOpen.open()
                closed = False
                servoToOpen = None
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        GPIO.cleanup()
        cv2.destroyAllWindows()
        