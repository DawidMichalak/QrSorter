from time import sleep
import stepper as Step
import RPi.GPIO as GPIO
import threading
from gpiozero import LightSensor, exc
from sorter import Sorter
from camera import Camera
from multiprocessing import Process, Lock, Pipe

if __name__ == '__main__': 
    GPIO.setmode(GPIO.BCM)
    beltDelay = 0.003
    sensor = LightSensor(23, threshold=0.1)
    camera = Camera()
    sorter = Sorter(camera)
    stepper = Step.Stepper(Step.halfStepSequence)
    result = True
    stopCameraThread = False

    beltLock = Lock()
    cameraLock = threading.Lock()

    beltProcess = Process(target=stepper.moveAsync, args=(beltDelay, beltLock))
    flushCameraThread = threading.Thread(target=camera.flushCamera, args=(cameraLock, lambda: stopCameraThread))
    
    beltProcess.start()
    flushCameraThread.start()

    while True:
        try:
            print('Waiting for dark')
            sensor.wait_for_dark() 
            print('It is dark')
            if result == True:
                print('Acquiring camera')
                cameraLock.acquire()
            print('Stopping the belt')
            beltLock.acquire()

            result = sorter.sort()
            if result != False:
                print('QR Detected')
                print('Starting manual move')
                stepper.move(beltDelay, 6500)
                print('Opening servo')
                sorter.open()
                print('Releasing camera')
                cameraLock.release()

            print('Releasing the belt')
            beltLock.release()
        except:
            print('Preparing to close...')
            break

    print('Closing processes...')
    if beltProcess.is_alive():
        beltProcess.terminate()
        beltProcess.join()
        beltProcess.close()

    try:
        cameraLock.release()
    except:
        pass

    stopCameraThread = True
    flushCameraThread.join()

    print('All processes and threads closed')
