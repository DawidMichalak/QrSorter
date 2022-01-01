import qrcode
import os
  
class QrCodeGenerator:
    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__)) 
        self.path += '\\Generator\\Codes\\'

    def addQrCode(self, data):
        qr = qrcode.QRCode(version = 1,
                box_size = 10,
                border = 5,
                error_correction = qrcode.constants.ERROR_CORRECT_Q)

        qr.add_data(data)
        qr.make(fit = True)
        img = qr.make_image()
        img.save(self.path + str(i) + '.png')
