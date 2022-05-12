import datetime
import math
import re
from tkinter import *

# About the program
"""
This program calculates from personal identification number (PIN) the age,
date of birth, and sex.
    
The program is written in Python 3.7.
Made by Vojtěch Adam alias HelloItsMeAdm
"""


class Udaje():
    def __init__(self, rodne_cislo):
        self.rodne_cislo = rodne_cislo

    # check if rodne cislo is ok
    def jeSpravne(self):
        if re.match(r'^\d{6}[/]\d{4}$', self.rodne_cislo):
            if not int(self.rodne_cislo.replace("/", "")) % 11 == 0:
                print('[\u2717] Rodne cislo neni delitelne 11')
                return False
            else:
                print("[\u2713] Rodne cislo je spravne")
                return True
        else:
            print('[\u2717] Nespravny format rodneho cisla')
            return False

    # get pohlavi from rodne cislo
    def pohlavi(self):
        self.rodne_cislo = self.rodne_cislo.replace('/', '')
        kontrola = self.rodne_cislo[2] + "" + self.rodne_cislo[3]
        if not int(kontrola) <= 50:
            return 'žena'
        else:
            return 'muž'

    # get datum narozeni from rodne cislo
    def datumNarozeni(self):
        self.rodne_cislo = self.rodne_cislo.replace('/', '')
        datum = self.rodne_cislo[0:6]

        den = datum[4:6]
        mesic = datum[2:4]
        rok = datum[0:2]
        if int(rok) > 22:
            rok = '19' + rok
        else:
            rok = '20' + rok

        return datetime.datetime(int(rok), int(mesic), int(den))

    # get rok narozeni from rodne cislo
    def getVek(self):
        den = self.rodne_cislo[4:6]
        mesic = self.rodne_cislo[2:4]
        rok = self.rodne_cislo[0:2]
        if int(rok) > 22:
            rok = '19' + rok
        else:
            rok = '20' + rok

        datum = datetime.datetime(int(rok), int(mesic), int(den))
        return math.floor((datetime.datetime.now() - datum).days / 365.25)


# create gui for input
root = Tk()
root.title("Processing rodne cislo")
root.geometry("300x100")
root.resizable(0, 0)

# create input
rodne_cislo = StringVar()
rodne_cislo_input = Entry(root, textvariable=rodne_cislo)
rodne_cislo_input.pack()
rodne_cislo_input.focus_set()

# create button
def process():
    udaje = Udaje(rodne_cislo.get())
    if udaje.jeSpravne():
        text.config(text=f"Pohlaví je {udaje.pohlavi()} narozen {udaje.datumNarozeni()} a má {udaje.getVek()} let.")


button = Button(root, text="Odeslat!", command=process)
button.pack()

# display text
text = Label(root, text="")
text.pack()

root.mainloop()
