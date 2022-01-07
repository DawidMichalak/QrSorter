import qrcode
import os
  
class QrCodeGenerator:
    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__)) 
        self.path += '\\Codes\\'

    def addQrCode(self, data):
        qr = qrcode.QRCode(version = 1,
                box_size = 10,
                border = 5,
                error_correction = qrcode.constants.ERROR_CORRECT_Q)

        qr.add_data(data)
        qr.make(fit = True)
        img = qr.make_image()
        img.save(self.path + str(data) + '.png')
    
if __name__ == "__main__":
    generator = QrCodeGenerator()
    generator.addQrCode('tools')
    generator.addQrCode('clothes')
    generator.addQrCode('games')
