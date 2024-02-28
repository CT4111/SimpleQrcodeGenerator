import qrcode
import customtkinter as ctk
from customtkinter import CTk
from PIL import Image,ImageTk
def GenerateCode(data,name,color1,color2,QRCodeImageDisplay):
    a = data.get()
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=20,
                       border=1)
    qr.add_data(a)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color1, back_color=color2)
    img.save(name)
    my_image = ctk.CTkImage(light_image=Image.open("D://pythonStufffffffff//"+name),
                                      dark_image=Image.open("D://pythonStufffffffff//"+name),
                                      size=(200, 200))
    QRCodeImageDisplay.configure(image=my_image,text = "")
def QRCodeGUI(root):
    ctk.set_appearance_mode("dark")
    #window = CTk()
    window = ctk.CTkToplevel(root)
    window.iconbitmap(r"D:\pythonStufffffffff\Icon.ico")
    lable = ctk.CTkLabel(window, text="QR Code Generator", font=("Helvetica", 30))
    lable.pack(pady= 10)
    frame = ctk.CTkFrame(window)
    frame.pack(expand=True, fill="both", padx=20, pady=10)

    QRCodeImageDisplay = ctk.CTkLabel(frame,text="QR Code")


    btn_1 = ctk.CTkButton(frame, text="Generate QR Code", fg_color='blue',
                      command= lambda:GenerateCode(txtfld,"QRCode.png","black","white",QRCodeImageDisplay))
    btn_1.pack(pady = 10)
    txtfld = ctk.CTkEntry(frame, placeholder_text="Input link or text")
    txtfld.pack(pady=10)
    QRCodeImageDisplay.pack()
    window.title('QR_Code_Generator')
    window.configure(background='black')
    window.geometry("600x400")
    window.mainloop()
