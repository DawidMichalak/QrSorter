from gpiozero import LightSensor
from sorter import *
import RPi.GPIO as GPIO

if __name__ == "__main__":
    sensor = LightSensor(23)
    sorter = Sorter()
    result = False

    try:
        while True:
            if result != False:
                sensor.wait_for_light()
                sorter.close()
            sensor.wait_for_dark()
            result = sorter.sort()
    finally:
        GPIO.cleanup()
        cv2.destroyAllWindows()
