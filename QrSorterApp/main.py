from gpiozero import LightSensor
from sorter import *
import stepper as Step
import RPi.GPIO as GPIO
from multiprocessing import Process, Lock

beltDelay = 0.003

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    sensor = LightSensor(23)
    sorter = Sorter()
    result = False

    stepper = Step.Stepper(Step.halfStepSequence)
    beltLock = Lock()
    beltProcess = Process(target=stepper.moveAsync, args=(beltDelay, beltLock))

    try:
        beltProcess.start()
        while True:
            print("waiting for dark")
            sensor.wait_for_dark() 
            print("stopping the belt")
            beltLock.acquire() 
            result = sorter.sort()
            if result != False:
                print("QR Detected")
                print("Starting manual move")
                stepper.move(beltDelay, 6000)
                print("Opening servo")
                sorter.close()
            print("Releasing the belt")
            beltLock.release()

    finally:
        if beltProcess.is_alive():
            beltProcess.terminate()
            beltProcess.close()
        GPIO.cleanup()
        cv2.destroyAllWindows()
