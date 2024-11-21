

"""
import qrcode
import image 
qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data="https://github.com/anurag815311"

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("test.png")"""

import qrcode
from PIL import Image  # Using Pillow for image processing

# Function to generate QR code from user input
def generate_qrcode():
    # Get user input for the data to encode
    data = input("Enter the data to encode in QR Code (e.g., URL, text): ")

    # Get user input for the file name to save the image
    filename = input("Enter the filename to save the QR Code (e.g., myqrcode.png): ")

    # Create a QR code object with customization
    qr = qrcode.QRCode(
        version=15,  # QR Code size
        box_size=10,  # Size of each box
        border=5  # Border size
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)  # Fit the data within the QR code

    # Create the image from the QR code object
    img = qr.make_image(fill="black", back_color="white")

    # Save the image to the specified filename
    img.save(filename)

    # Notify the user of the successful generation and save
    print(f"QR Code generated and saved as {filename}")

# Run the QR code generator function
generate_qrcode()


