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


# -- pääohjelma alkaa --
# luodaan uusi Auto-luokan olio
autoA = Auto("ABC-123", 142)

# tulostetaan auton kaikki ominaisuudet
print(f"Auton ominaisuudet: \n"
      f"rekkari: {autoA.rekisteritunnus} \n"
      f"huippunopeus: {autoA.huippunopeus} \n"
      f"tämän hetkinen nopeus: {autoA.nopeus} \n"
      f"kuljettu matka: {autoA.matka}")

