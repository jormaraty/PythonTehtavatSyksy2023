# Auto-luokan määrittely
import random


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
# luodaan tyhjä lista kilpa-autoja varten.
autot = []

# luodaan 10 autoa, jokaisen huippunopeus arvotaan välille 100 .. 200 km/h.
# autot lisätään edellä luotuun listaan.
for nro in range(1, 11):
    # nro saa arvot 1, 2, ..., 10
    # auton rekkari
    rekkari = "ABC-" + str(nro)
    # arvotaan nyt luotavan auton huippunopeus (100 ... 200)
    max = random.randint(100, 200)
    # luodaan uusi auto
    kilpailija = Auto(rekkari, max)
    # lisätään luotu auto listaan
    autot.append(kilpailija)

# Xtra: kiihdytän aluksi jokaisen auton nopeuden 0 -> 80 km/h,
# jotta kilpailu olisi ohi nopeammin.
for kilpailija in autot:
    kilpailija.kiihdyta(80)


jatketaan = True        # jatketaanko kilpailua vai ei?
kesto = 0               # kuinka monta tuntia kilpailu on jatkunut.

# kilpailua jatketaan, kunnes joku kilpailija on kulkenut yli 10,000km
while jatketaan:
    # käydään listan jokainen auto yksitellen läpi
    for auto in autot:
        # arvotaan autolle sen nopeuden muutos (-10 ... +15 km/h)
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)       # muutetaan auton nopeutta
        auto.kulje(1)               # auto ajaa 1h uudella nopeudella
        # tarkistetaan, että onko auto päässyt maaliin
        if auto.matka >= 10000:
            jatketaan = False       # lopetetaan kilpailu
    # lisätään kilpailuun käytettyä aikaa tunnilla
    kesto += 1

# kilpailu on päättynyt, ilmoitetaan tulokset:
print(f"Kilpailun kesto oli {kesto}h.")

# tulostetaan kaikkien kilpailijoiden kulkemat matkat
# \t on sarkain- eli tab-näppäin

'''
* Tämä koodinpätkä on nyt kommentoitu pois kolmen heittomerkin avulla *
print(f"Rekkari \tMax\tNopeus\tMatka")
for kilpailija in autot:
    print(f"{kilpailija.rekisteritunnus} \t\t{kilpailija.huippunopeus} "
          f"\t{kilpailija.nopeus} \t{kilpailija.matka} ")
'''

# xtra: järjestetään kilpailijat paremmuusjärjestykseen
def lajittelija(kilpailija):
    # funktio palauttaa kuljetun matkan, jonka perusteella kilpailijat järjestetään.
    return kilpailija.matka

# järjestetään kilpailijat em. funktiuon avulla käänteiseen järjestykseen,
# eli pisimmän matkan kulkenut on voittaja
autot.sort(reverse=True, key=lajittelija)

# tulostetaan autot paremmuusjärjestyksessä, paras ensin.
print(f"Rekkari \tMax\tNopeus\tMatka")
for kilpailija in autot:
    print(f"{kilpailija.rekisteritunnus} \t\t{kilpailija.huippunopeus} "
          f"\t{kilpailija.nopeus} \t{kilpailija.matka} ")
