class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.sijainti = alin      # hissin nykyinen kerros

    def kerros_ylos(self):
        if self.sijainti < self.ylin:
            # jos hissi ei ole ylimmässä kerroksessa, niin hissi noudee 1 kerroksen ylöspäin
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


# -- pääohjelma --

# luodaan uusi hissi
hissiA = Hissi(1, 7)
# ajetaan hissi 5. kerrokseen ja sen jälkeen 1. kerrokseen
hissiA.siirry_kerrokseen(5)
hissiA.siirry_kerrokseen(1)

