import qrcode

theData =  input('Message or the link that you want to place in the QR: ').strip()
qrcodeimage_name = input('Name you prefer to be the name of the qrcode image + image format(.png, .jpeg, .jpg): ').strip()

theQR = qrcode.QRCode(box_size=7, border=3)
theQR.add_data(theQR)
theqrcodeimage = theQR.make_image(fill_color="blue", back_color="white")
theqrcodeimage.save(qrcodeimage_name)
print(f'Your QRcode  is ready to GO!!')