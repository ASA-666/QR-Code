import qrcode

# Data to be encoded in the qrcode

data = input(str("Enter the data to be encoded in the QR code: "))

# Create a QR Code instance
qr= qrcode.QRCode(
    version=1, #controls the size of qr code
    error_correction=qrcode.constants.ERROR_CORRECT_L, #corrects error correction level
    box_size=10,
    border=4,
)
# Add data to the qr code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the qr code
img= qr.make_image(fill='black', black_color='white')

# Save the image
img.save("qrcode_example.png")

# Display the image
img.show()