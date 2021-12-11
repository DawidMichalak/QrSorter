import cv2
from pyzbar.pyzbar import decode, ZBarSymbol
import camera  


def findQR(im) :
  decodedObjects = decode(im, symbols=[ZBarSymbol.QRCODE])

  for obj in decodedObjects:
    print('Data : ', obj.data,'\n')

  return decodedObjects


cam = camera.Camera()

while(True):
    frame = cam.getFrame()
    qrFrame = cam.display(frame, findQR(frame))


    cv2.imshow('frame', qrFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  

cv2.destroyAllWindows()