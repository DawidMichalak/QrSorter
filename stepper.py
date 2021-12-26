import time
import board
import digitalio

pins = [
    digitalio.DigitalInOut(board.D4),
    digitalio.DigitalInOut(board.D17),
    digitalio.DigitalInOut(board.D27),
    digitalio.DigitalInOut(board.D22)
]

halfStepSequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]]

torqueSequence = [
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 0]]


class Stepper():
    
    sequence = []
    
    def __init__(self, seq):
        self.sequence = seq
        for p in pins:
            p.direction = digitalio.Direction.OUTPUT
            
    def forward(self, delay, steps):
        for i in range(0, steps):
            self.setStep(i % len(self.sequence))
            time.sleep(delay)
        
    def setStep(self, seq):
        for i, p in enumerate(pins):
            p.value = self.sequence[seq][i]


if __name__ == "__main__":
    step = Stepper(halfStepSequence)
    while True:
        user_delay = input("Delay(milliseconds): ")
        user_steps = input("Steps: ")
        step.forward(int(user_delay) / 1000.0, int(user_steps))


