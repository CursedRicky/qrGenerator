import sys, os, customtkinter, qrcode
from PIL import Image

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def qrCode():
    global firstTime
    img = qrcode.make(textBox.get("0.0", 'end'))
    img.save(resource_path("code.png"))
    qrImage.configure(dark_image=Image.open(resource_path("code.png")))

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("400x400")
root.title("QR Generator")
root.resizable(False, False)

titolo = customtkinter.CTkLabel(master=root, text="Generatore di QR", font=("Verdana", 20))
titolo.pack(pady=10)

textBox = customtkinter.CTkTextbox(master=root, width=260, height=50)
textBox.pack(pady=20)

btnGen = customtkinter.CTkButton(master=root, text="Genera QR", command=qrCode)
btnGen.pack(pady=5)

qrImage = customtkinter.CTkImage(dark_image=Image.open(resource_path("blank.png")), size=(160, 160))
label = customtkinter.CTkLabel(master=root, text="", image=qrImage)
label.pack(pady=20)

root.mainloop()