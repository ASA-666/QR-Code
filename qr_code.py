import qrcode

#data to be encoded in the qrcode

data = "https://www.youtube.com/watch?v=xvFZjo5PgG0"

#ceeate a qrcode instance
qr= qrcode.QRCode(
    version=1, #controls the size of qr code
    error_correction=qrcode.constants.ERROR_CORRECT_L, #corrects error correction level
    box_size=10,
    border=4,
)
#add data to the qr code
qr.add_data(data)
qr.make(fit=True)

#create an image from the qr code
img= qr.make_image(fill='black', black_color='white')

#save the image
img.save("qrcode_example.png")

#display the image
img.show()