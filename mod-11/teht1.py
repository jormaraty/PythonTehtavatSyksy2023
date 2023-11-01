class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        # kutsutaan yliluokan (Julkaisu) alustajaa, se asettaa oliolle sen 'nimi'-ominaisuuden
        super().__init__(nimi)
        # tämä aliluokan (Kirja) alustaja asettaa oliolle sen kirjoittaja ja sivumaara-ominaisuudet
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print("- Kirjan tiedot -")
        print(f"Nimi: {self.nimi} \n"
              f"Kirjoittaja: {self.kirjoittaja} \n"
              f"Sivumäärä: {self.sivumaara}" )
        return


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print("- Lehden tiedot -")
        print(f"Nimi: {self.nimi} \n"
              f"Päätoimittaja: {self.paatoimittaja}")
        return


# -- pääohjelma --

# luodaan uusi Lehti- ja Kirja- tyyppiset oliot
lehti = Lehti("Aku Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

# tulostetaan olioiden tiedot
lehti.tulosta_tiedot()
kirja.tulosta_tiedot()