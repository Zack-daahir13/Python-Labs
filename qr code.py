import qrcode
import tkinter as tk
from PIL import ImageTk, Image

# Generate QR code
data = "Hello, world!"  # The data you want to encode in the QR code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white")

# Display QR code using Tkinter
root = tk.Tk()
root.title("QR Code Scanner")
qr_image_tk = ImageTk.PhotoImage(qr_img.resize((300, 300)))
label = tk.Label(root, image=qr_image_tk)
label.pack()
root.mainloop()
