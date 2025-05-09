import qrcode
import os
from PIL import Image

# Create data_files directory if it doesn't exist
data_dir = 'data_files'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Create QR code
data = 'Don\'t forget to subscribe'
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# Create and save the QR code image
img = qr.make_image(fill_color='red', back_color='white')
qr_path = os.path.join(data_dir, 'myqr_code.png')
img.save(qr_path)
print(f"QR code has been created and saved to: {qr_path}")
print(f"The QR code contains the text: {data}")