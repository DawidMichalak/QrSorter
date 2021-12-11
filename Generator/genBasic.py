import qrcode
  
for i in range(4):
    data = i
    qr = qrcode.QRCode(version = 1,
                    box_size = 10,
                    border = 5,
                    error_correction = qrcode.constants.ERROR_CORRECT_Q)

    qr.add_data(data)
    
    qr.make(fit = True)
    img = qr.make_image()
    
    img.save( str(i) + '.png')