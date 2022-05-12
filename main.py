import re, datetime


class Udaje():
    def __init__(self, rodne_cislo):
        self.rodne_cislo = rodne_cislo

    def jeSpravne(self):
        if not re.match(r'^\d{6}[/]\d{4}$', self.rodne_cislo):
            print('[\u2717] Nespravny format rodneho cisla')
            return False
        else:
            print("[\u2713] Rodne cislo je spravne")
            return True

    def pohlavi(self):
        self.rodne_cislo = self.rodne_cislo.replace('/', '')
        kontrola = self.rodne_cislo[2] + "" + self.rodne_cislo[3]
        if not int(kontrola) <= 50:
            print('[\u2713] Jsi zena')
            return 'zena'
        else:
            print('[\u2713] Jsi muz')
            return 'muz'

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

    def getVek(self):
        # ziskej vek z rodne_cislo
        rok = self.rodne_cislo[0:2]
        if int(rok) > 22:
            rok = '19' + rok
        else:
            rok = '20' + rok


print(Udaje('050627/1465').getVek())
