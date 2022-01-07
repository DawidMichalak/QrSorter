import time
import RPi.GPIO as GPIO

pins = [4, 17, 27, 22]

halfStepSequence = [
    (GPIO.HIGH,  GPIO.LOW,  GPIO.LOW,  GPIO.LOW),
    (GPIO.HIGH, GPIO.HIGH,  GPIO.LOW,  GPIO.LOW),
    ( GPIO.LOW, GPIO.HIGH,  GPIO.LOW,  GPIO.LOW),
    ( GPIO.LOW, GPIO.HIGH, GPIO.HIGH,  GPIO.LOW),
    ( GPIO.LOW,  GPIO.LOW, GPIO.HIGH,  GPIO.LOW),
    ( GPIO.LOW,  GPIO.LOW, GPIO.HIGH, GPIO.HIGH),
    ( GPIO.LOW,  GPIO.LOW,  GPIO.LOW, GPIO.HIGH),
    (GPIO.HIGH,  GPIO.LOW,  GPIO.LOW, GPIO.HIGH)]

torqueSequence = [
    ( GPIO.LOW,  GPIO.LOW, GPIO.HIGH, GPIO.HIGH),
    (GPIO.HIGH,  GPIO.LOW,  GPIO.LOW, GPIO.HIGH),
    (GPIO.HIGH, GPIO.HIGH,  GPIO.LOW,  GPIO.LOW),
    ( GPIO.LOW, GPIO.HIGH, GPIO.HIGH,  GPIO.LOW)]

class Stepper():
    
    sequence = []

    def __init__(self, seq):
        if GPIO.getmode() == None:
            GPIO.setmode(GPIO.BCM)
        GPIO.setup(pins, GPIO.OUT)
        self.sequence = seq


    def move(self, delay, steps, backward=False):
        for i in range(0, steps):
            if backward:
                GPIO.output(pins, self.sequence[(- i % len(self.sequence))])
            else:
                GPIO.output(pins, self.sequence[i % len(self.sequence)])
            time.sleep(delay)
        GPIO.output(pins, GPIO.LOW)


if __name__ == "__main__":
    step = Stepper(halfStepSequence)
    while True:
        delay = input("Delay(milliseconds): ")
        steps = input("Steps: ")
        if steps == '0' or delay == '0':
            break
        step.move(int(delay) / 1000.0, int(steps))
    GPIO.cleanup()