class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.sijainti = alin      # hissin nykyinen kerros

    def kerros_ylos(self):
        if self.sijainti < self.ylin:
            # jos hissi ei ole ylimmässä kerroksessa, niin hissi nousee 1 kerroksen ylöspäin
            self.sijainti += 1
        print(f"Hissi on nyt {self.sijainti}. kerroksessa")
        return

    def kerros_alas(self):
        if self.sijainti > self.alin:
            self.sijainti = self.sijainti - 1
        print(f"Hissi on nyt {self.sijainti}. kerroksessa")
        return

    def siirry_kerrokseen(self, haluttu_kerros):
        if self.sijainti < haluttu_kerros:
            # haluttu kerros on nykyistä ylempänä
            while self.sijainti < haluttu_kerros:
                self.kerros_ylos()
        elif self.sijainti > haluttu_kerros:
            # haluttu kerros on nykyistä alempana
            while self.sijainti > haluttu_kerros:
                self.kerros_alas()
        print("Hissi on nyt halutussa kerroksessa")
        return


class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []        # lista sisältää talon hissit
        # luodaan tarvittavat hissit ja talletetaan ne listaan
        for i in range(hissien_lkm):
            hissi = Hissi(self.alin, self.ylin)
            self.hissit.append(hissi)

    def aja_hissia(self, hissin_nro, kohdekerros):
        # oletus: käyttäjä antaa hissin numeron 1, 2, 3, ...
        # listan indeksointi alkaa nollasta.
        hissi = self.hissit[hissin_nro - 1]
        hissi.siirry_kerrokseen(kohdekerros)
        print(f"Hissi {hissin_nro} on nyt halutussa kerroksessa {kohdekerros}")
        return

    # xtra metodi toimintojen tarkistamiseksi
    def kerro_hissien_sijainnit(self):
        print("- Talon hissien sijainnit -")
        for i in range(len(self.hissit)):
            # jos talossa on 3 hissiä, niin i saa arvot 0, 1 ja 2.
            print(f"hissi {i+1} on kerroksessa {self.hissit[i].sijainti}")
        return


# pääohjelma
# luodaan 12-kerroksinen talo, jossa on 3 hissiä
talo = Talo(1, 12, 3)
talo.aja_hissia(3, 10)      # ajetaan hissillä nro 3 kerrokseen 10.
talo.aja_hissia(1, 7)
# tarkistetaan talon hissien sijainnit
talo.kerro_hissien_sijainnit()


