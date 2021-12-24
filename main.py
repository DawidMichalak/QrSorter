import cv2
import camera  
from qrFinder import *

cam = camera.Camera()

while(True):
    frame = cam.getTestImage()
    qrFrame = drawQR(frame, findQR(frame))

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  

cv2.destroyAllWindows()