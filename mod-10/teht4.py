# Auto-luokan määrittely, kopioitu tehtävästä: mod-09, teht 3.
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


class Kilpailu:
    def __init__(self, nimi, pituus, autolista):
        self.nimi = nimi
        self.pituus = pituus
        self.autolista = autolista

    def tunti_kuluu(self):
        # arvotaan kullekin autolle nopeuden muutos,
        # päivitetään auton tiedot ja ajetaan sillä tunti.
        for auto in self.autolista:
            nopeus_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeus_muutos)    # muutetaan auton nopeus
            auto.kulje(1)                   # ajetaan autolla 1h
        return

    def tulosta_tilanne(self):
        # tulostetaan jokaisen auton sen hetkinen tilanne
        print(f"Rekkari \tMax\tNopeus\tMatka")
        for auto in self.autolista:
            print(f"{auto.rekisteritunnus} \t\t{auto.huippunopeus} \t{auto.nopeus} \t{auto.matka} ")
        return

    def kilpailu_ohi(self):
        # metodin palauttama tieto, että onko kilpailu päättynyt vai ei
        kilpailu_paattynyt = False

        for auto in self.autolista:
            if auto.matka >= self.pituus:
                # jos auto on päässyt maaliin, niin kilpailu on loppunut
                kilpailu_paattynyt = True
                break       # lopetetaan for-toisto
        return kilpailu_paattynyt

    def lajittelija(self, kilpailija):
        # funktio palauttaa kuljetun matkan, jonka perusteella kilpailijat järjestetään.
        return kilpailija.matka

    def tulosta_lopputilanne(self):
        # järjestetään kilpailijat em. funktiuon avulla käänteiseen järjestykseen,
        # eli pisimmän matkan kulkenut on voittaja
        self.autolista.sort(reverse=True, key=self.lajittelija)
        self.tulosta_tilanne()
        return


# -- pääohjelma --

kilpailijat = []        # lista kilpailuun osallistuvista autoista

# luodaan 10 kilpailijaa (autoa) ja lisätään ne listaan
for nro in range(1, 11):
    rekkari = "ABC-" + str(nro)         # auton rekisteritunnus
    max = random.randint(100, 200)      # arvotaan auton huippunopeus (100 ... 200)
    auto = Auto(rekkari, max)           # luodaan uusi auto
    kilpailijat.append(auto)            # lisätään luotu auto listaan

# luodaan uusi kisa, pituus 8000 km.
kisa = Kilpailu("Suuri romuralli", 8000, kilpailijat)
kisa_aika = 0               # kuinka monta tuntia kisa on kestänyt
kisa_kaynnissa = True

# jatketaan kilpailua, kunnes se on päättynyt
while kisa_kaynnissa:
    kisa.tunti_kuluu()      # ajetaan tunti
    kisa_aika += 1              # päivitetään kisan kesto
    # tsekataan että onko jokum kilpalija päässyt maaliin
    if kisa.kilpailu_ohi() == True:
        kisa_kaynnissa = False
    # tulostetaan väliaikatietoja 10h välein.
    if kisa_aika % 10 == 0:
        print(f"\n-- Tilanne {kisa_aika} tunnin jälkeen: --")
        kisa.tulosta_tilanne()

# kisa on päättynyt, kun tänne tullaan
print(f"\n--- Kisa on päättynyt, se kesti {kisa_aika} tuntia ---")
print("Alla ovat kilpailun lopputulokset: \n")
kisa.tulosta_lopputilanne()

