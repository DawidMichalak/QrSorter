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

    def __enter__(self):
        for p in pins:
            p.direction = digitalio.Direction.OUTPUT
        return self
    
    def __exit__(self ,type, value, traceback):
        print("deinit")
        for p in pins:
            p.value = 0
            p.deinit()
        
    def __init__(self, seq):
        self.sequence = seq

    def forward(self, delay, steps):
        for i in range(0, steps):
            self.setStep(i % len(self.sequence))
            time.sleep(delay)
        
    def backward(self, delay, steps):
        for i in range(0, steps):
            self.setStep(( - i % len(self.sequence)))
            time.sleep(delay)
        
    def setStep(self, seq):
        for i, p in enumerate(pins):
            p.value = self.sequence[seq][i]

if __name__ == "__main__":
     
    with Stepper(halfStepSequence) as step:
        while True:
            delay = input("Delay(milliseconds): ")
            steps = input("Steps: ")
            if steps == '0' or delay == '0':
                break
            step.forward(int(delay) / 1000.0, int(steps))
            