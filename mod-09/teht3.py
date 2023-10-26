# Auto-luokan määrittely
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        # xtra: asetetaan uuden auton nopeus ja kuljettu matka aina nollaksi,
        #       vaikka käyttäjä antaisi erilaiset alkuarvot.
        self.nopeus = 0
        self.matka = 0
        # konstruktorin eli alustajan loppuun ei tule return-lausetta

    def kiihdyta(self, muutos):
        # muutetaan aluksi auton nopeutta ilmoitetun muutoksen verran
        self.nopeus = self.nopeus + muutos
        # check: auton nopeus ei saa olla yli hhuippunopeuden
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        # check: auton nopeus ei saa olla negatiivinen
        if self.nopeus < 0:
            self.nopeus = 0
        return

    def kulje(self, aika):
        # muutetaan auton kulkemaa matkaa (lisämatka = nopeus * aika)
        lisa_matka = self.nopeus * aika
        self.matka = self.matka + lisa_matka
        return


# -- pääohjelma alkaa --
# luodaan uusi Auto-luokan olio
autoA = Auto("ABC-123", 142)

# tulostetaan auton kaikki ominaisuudet
print(f"Auton ominaisuudet: \n"
      f"rekkari: {autoA.rekisteritunnus} \n"
      f"huippunopeus: {autoA.huippunopeus} km/h \n"
      f"tämän hetkinen nopeus: {autoA.nopeus} km/h \n"
      f"kuljettu matka: {autoA.matka} km")

# nostetaan nopeutta 30 km/h.
autoA.kiihdyta(30)
# nostetaan nopeutta 70 km/h.
autoA.kiihdyta(70)
# nostetaan nopeutta 50 km/h.
autoA.kiihdyta(50)
# tulostetaan auton nykyinen nopeus
print(f"Auton nopeus kiihdytysten jälkeen on {autoA.nopeus} km/h.")

# hätäjarrutus
autoA.kiihdyta(-200)
# tulostetaan auton nopeus hätäjarrutuksen jälkeen
print(f"Auton nopeus hätäjaruutuksen jälkeen: {autoA.nopeus} km/h.")

# xtra: testataan kulje()-metodin toimintaa
# nostetaan auton nopeus 0 -> 60 km/h.
autoA.kiihdyta(60)
# ajetaan autoa 1,5h
autoA.kulje(1.5)
# testitulostus
print(f"Autolla on nyt ajettu {autoA.matka} km.")