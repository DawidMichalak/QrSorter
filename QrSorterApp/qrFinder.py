import numpy as np
import cv2
from pyzbar.pyzbar import decode, ZBarSymbol

def findQRData(image) :
    #return first found qr code
    try:
        decodedObjects = decode(image, symbols=[ZBarSymbol.QRCODE])
        decoded = decodedObjects[0].data.decode('utf-8')
        return decoded
    except:
        return ''

def drawQR(image):
    decodedObjects = decode(image, symbols=[ZBarSymbol.QRCODE])
    for decoded in decodedObjects:
        points = decoded.polygon
        if len(points) > 4 :
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else :
            hull = points

        n = len(hull)

        for j in range(0, n):
            cv2.line(image, hull[j], hull[ (j+1) % n], (255,0,0), 3)

    return image
