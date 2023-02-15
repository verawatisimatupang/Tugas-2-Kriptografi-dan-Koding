from pathlib import Path
from tkinter import StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox
import tkinter as Tk
import base64

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class RanesCipherBasePage(Tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.RanesCipherBase()

    def RanesCipherBase(self):
        self.canvas = Canvas(
            self.master,
            bg = "#F4F3F9",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)

        self.key = StringVar()
        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            381.0,
            589.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.key
        )
        self.entry_1.place(
            x=158.0,
            y=537.0,
            width=446.0,
            height=103.0
        )

        self.plain = StringVar()
        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            381.0,
            412.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.plain
        )
        self.entry_2.place(
            x=158.0,
            y=360.0,
            width=446.0,
            height=103.0
        )

        self.cipher_base = StringVar()
        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            983.0,
            589.5,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable= self.cipher_base
        )
        self.entry_3.place(
            x=760.0,
            y=537.0,
            width=446.0,
            height=103.0
        )

        self.cipher_string = StringVar()
        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            983.0,
            412.5,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.cipher_string
        )
        self.entry_4.place(
            x=760.0,
            y=360.0,
            width=446.0,
            height=103.0
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("encrypt_button.png"))
        self.encrypt_button = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.encrypt(),
            relief="flat"
        )
        self.encrypt_button.place(
            x=68.0,
            y=682.0,
            width=250.58251953125,
            height=55.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("reset_button.png"))
        self.reset_button = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.reset(),
            relief="flat"
        )
        self.reset_button.place(
            x=682.0,
            y=682.0,
            width=524.0,
            height=55.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("back_button.png"))
        self.back_button = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.click_backHome(),
            relief="flat"
        )
        self.back_button.place(
            x=88.0,
            y=104.0,
            width=97.0,
            height=55.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("decrypt_button.png"))
        self.decrypt_button = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.decrypt(),
            relief="flat"
        )
        self.decrypt_button.place(
            x=340.41748046875,
            y=682.0,
            width=250.58250427246094,
            height=55.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("downloadbiner_no_space_button.png"))
        self.downloadbiner_no_space_button = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.downloadfilebiner_nospace(),
            relief="flat"
        )
        self.downloadbiner_no_space_button.place(
            x=669.0,
            y=417.0,
            width=75.0,
            height=48.0
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("downloadbiner_with_space_button.png"))
        self.downloadbiner_with_space_button = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.downloadfilebiner_withspace(),
            relief="flat"
        )
        self.downloadbiner_with_space_button.place(
            x=670.0,
            y=594.0,
            width=75.0,
            height=48.0
        )

        self.button_image_7 = PhotoImage(
            file=relative_to_assets("uploadbiner_plaintext_button.png"))
        self.uploadbiner_plaintext_button = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.uploadfilebiner_plaintext(),
            relief="flat"
        )
        self.uploadbiner_plaintext_button.place(
            x=68.0,
            y=417.0,
            width=75.0,
            height=48.0
        )

        self.button_image_8 = PhotoImage(
            file=relative_to_assets("uploadbiner_key_button.png"))
        self.uploadbiner_key_button = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.uploadfilebiner_key(),
            relief="flat"
        )
        self.uploadbiner_key_button.place(
            x=68.0,
            y=594.0,
            width=75.0,
            height=48.0
        )

        self.button_image_9 = PhotoImage(
            file=relative_to_assets("uploadtxt_plaintext_button.png"))
        self.uploadtxt_plaintext_button = Button(
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.uploadfiletxt_plaintext(),
            relief="flat"
        )
        self.uploadtxt_plaintext_button.place(
            x=68.0,
            y=360.0,
            width=75.0,
            height=48.0
        )

        self.button_image_10 = PhotoImage(
            file=relative_to_assets("uploadtxt_key_button.png"))
        self.uploadtxt_key_button = Button(
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.uploadfiletxt_key(),
            relief="flat"
        )
        self.uploadtxt_key_button.place(
            x=68.0,
            y=537.0,
            width=75.0,
            height=48.0
        )

        self.button_image_11 = PhotoImage(
            file=relative_to_assets("downloadtxt_no_space_button.png"))
        self.downloadtxt_no_space_button = Button(
            image=self.button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.downloadfiletxt_nospace(),
            relief="flat"
        )
        self.downloadtxt_no_space_button.place(
            x=669.0,
            y=360.0,
            width=75.0,
            height=48.0
        )

        self.button_image_12 = PhotoImage(
            file=relative_to_assets("downloadtxt_with_space_button.png"))
        self.downloadtxt_with_space_button = Button(
            image=self.button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.downloadfiletxt_withspace(),
            relief="flat"
        )
        self.downloadtxt_with_space_button.place(
            x=670.0,
            y=537.0,
            width=75.0,
            height=48.0
        )

        self.canvas.create_text(
            773.0,
            505.0,
            anchor="nw",
            text="Ciphertext (base64):",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            773.0,
            331.0,
            anchor="nw",
            text="Ciphertext (string):",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            158.0,
            505.0,
            anchor="nw",
            text="Enter secret key for encryption and decryption:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            158.0,
            331.0,
            anchor="nw",
            text="Enter text for encryption and decryption:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            224.0,
            97.0,
            anchor="nw",
            text="Ranes Cipher Standard",
            fill="#000000",
            font=("Inter Bold", 64 * -1)
        )
    
    def startPage(self):
        self.mainloop()
    
    def click_backHome(self):
        self.origin.Home()
    
    # Reset
    def reset(self):
        self.plain.set("")
        self.key.set("")
        self.cipher_string.set("")
        self.cipher_base.set("")
    
    def text_to_ascii(self, text):
        ascii_list = [ord(char) for char in text]
        return ascii_list
    
    def ascii_to_text(self, number):
        text = []
        for i in range (len(number)):
            text.append(chr(number[i]))
            result  = "".join(text)
        return result

    def text_to_base64(self, text):
        text_bytes = text.encode("utf-8")
        base64_bytes = base64.b64encode(text_bytes)
        base64_str = base64_bytes.decode("ascii")
        return base64_str

    def base64_to_text(self, base64_str):
        base64_bytes = base64_str.encode("ascii")
        text_bytes = base64.b64decode(base64_bytes)
        text_str = text_bytes.decode("utf-8")
        return text_str
    
    def ascii_to_base64(self, number):
        convert_to_string = self.ascii_to_text(number)
        convert_to_base64 = self.text_to_base64(convert_to_string)
        return convert_to_base64

    def base64_to_ascii(self, base64_str):
        convert_to_string = self.base64_to_text(base64_str)
        convert_to_ascii = self.text_to_ascii(convert_to_string)
        return convert_to_ascii
    
    def KSA(self, key):
        S = []
        K = []

        for i in range(0,256):
            S.append(i)
            K.append(ord(key[i % len(key)]))

        j = 0
        for i in range(0,256):
            j = (j + S[i] + K[i]) % 256
            S[i], S[j] = S[j], S[i]
        
        return S
    
    def PRGA(self, S, plaintext):
        j = 0
        K = []
        for i in range (len(plaintext)):
            i = (i+1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            K.append(S[(S[i] + S[j]) % 256])
        return K
    
    def XOR(self, plaintext, key):
        ciphertext = []
        for i in range(len(plaintext)):
            formula = ord(plaintext[i]) ^ key[i]
            ciphertext.append(formula)
        return ciphertext
    
    # Encyrpt
    def decrypt(self):
        plaintext = self.plain.get()
        key = self.key.get()

        if len(plaintext) == 0:
            messagebox.showerror("Error", "Please input plaintext / file")
        elif len(key) == 0:
            messagebox.showerror("Error", "Please input key / file")
        else :  
            convert_to_string = self.base64_to_text(plaintext)
            ksa_key = self.KSA(key)
            prga_ksakey_plaintext = self.PRGA(ksa_key, convert_to_string)
            xor_plaintext_prgaksakey = self.XOR(convert_to_string, prga_ksakey_plaintext)
            result_string = self.ascii_to_text(xor_plaintext_prgaksakey)
            result_base64 = self.text_to_base64(result_string)
        self.cipher_string.set(result_string)
        self.cipher_base.set(result_base64)
