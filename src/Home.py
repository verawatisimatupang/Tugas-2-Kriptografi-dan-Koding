from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as Tk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class HomePage(Tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.Home()

    def Home(self):
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
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("base_button_1.png"))
        self.base_button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("base_button_1 clicked"),
            relief="flat"
        )
        self.base_button_1.place(
            x=462.0,
            y=437.0,
            width=356.0,
            height=76.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("string_button_2.png"))
        self.string_button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("string_button_2 clicked"),
            relief="flat"
        )
        self.string_button_2.place(
            x=462.0,
            y=319.0,
            width=356.0,
            height=76.0
        )

        self.canvas.create_text(
            410.0,
            158.0,
            anchor="nw",
            text="by : Verawati Esteria S. Simatupang & Agnes Tamara",
            fill="#000000",
            font=("OpenSansItalic Regular", 20 * -1)
        )

        self.canvas.create_text(
            430.0,
            55.0,
            anchor="nw",
            text="Ranes Cipher",
            fill="#000000",
            font=("OpenSansRoman Bold", 64 * -1)
        )

    def startPage(self):
        self.mainloop()
    
    def click_inputstring(self):
        self.origin.InputString()

    def click_inputbase64(self):
        self.origin.InputBase64()
