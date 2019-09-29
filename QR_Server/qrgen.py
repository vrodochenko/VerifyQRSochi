import qrcode
from configs import *

def generate_qr_code(FIO):
    qr = qrcode.QRCode(
        version=1,
        box_size=15,
        border=1
    )
    data = FIO
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(PIC_PATH)
    img.save(PIC_THUMB_PATH)
    return img


def generate_qr_code_iphone(iphone_json):
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
    img.save(PIC_PATH)
    img.save(PIC_THUMB_PATH)
    return img
