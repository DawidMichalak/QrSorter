import RPi.GPIO as GPIO
import time
import numpy

#Servo(19, ..., True, 2) - left servo
#Servo(20, ..., False, 3) - right servo
class Servo:    
    def __init__(self, servoPin, boxId, flip=False, addition=3):
        self.servoPin = servoPin
        self.openPosition = 82
        self.closePosition = 1
        self.rezolution = 50
        self.boxId = boxId
        self.addition = addition
        GPIO.setup(self.servoPin, GPIO.OUT)
   
        if flip:
            self.openPosition = 0
            self.closePosition = 90
        
        self.position = self.openPosition
        self.open() 
        
    def close(self):
        self.move(self.closePosition)
        
    def open(self):
        self.move(self.openPosition)
        
    def move(self, newPosition):
        pwm = GPIO.PWM(self.servoPin, self.rezolution)   
        pwm.start(self.position)
        angle = numpy.linspace(self.position, newPosition, self.rezolution)
        
        for a in angle:
            duty = a / 18 + self.addition
            pwm.ChangeDutyCycle(duty)
            time.sleep(1/self.rezolution)
            
        self.position = newPosition
        pwm.stop(newPosition)
        
if __name__ == "__main__":
    servoRight = Servo(20, 2, False)
    servoRight.close()
    time.sleep(1)
    servoRight.open()
    
    time.sleep(1)
    servoLeft = Servo(19, 1, True, 2)
    servoLeft.close()
    time.sleep(1)
    servoLeft.open()
    
    GPIO.cleanup()
