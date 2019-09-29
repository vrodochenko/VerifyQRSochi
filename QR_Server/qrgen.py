import qrcode


def genqr(FIO):
    qr = qrcode.QRCode(
        version=1,
        box_size=15,
        border=1
    )
    data = FIO
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')   
    size = (512, 512)
    img.thumbnail(size)
    img.save('FIO.png')
    return img
