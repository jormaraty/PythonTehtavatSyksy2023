# Lasketaan piin arvo simuloimalla.

# Seuraava toistetaan esim. 100 000 kertaa:
# - arvotaan pisteen (x, y) koordinaatit
# - x-koordinaatti saa arvon väliltä -1 ... 1. Samoin y-koordinaatti.
# - lasketaan onko arvotun (x,y) pisteen etäisyys origosta alle 1.

# Merkitään: simulointiLkm = arvottujen pisteiden lukumäärä (esim. 100 000),
# sisalla = niiden (x,y) pisteiden lkm, joiden etäisyys origosta on alle 1.
# Tällöin piin arvo saadaan laskettua kaavasta:
# π ≈ (4 * sisalla) / simulointiLkm

import math
import random

# kysytään käyttäjältä, kuinka monta pistettä arvotaan
simulointiLkm = int(input("Kuinka monta (x,y) pistettä arvotaan: "))

# arvottujen pisteiden lkm, aluksi = 0
arvottu = 0

# sisällä (etäisyys alle 1 origosta lkm), aluksi nolla.
sisalla = 0

# toistetaan käyttäjän haluama määrä (arvottu on 0, 1, 2, ... (simulointiLkm - 1) )
while arvottu < simulointiLkm:
    # arvotaan pisteen x- ja y-koordinaatit välille -1 ,, 1 (desim. luku)
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    # lasketaan (x,y) pisteen etäisyys origosta
    etaisyys = math.sqrt( x**2 + y**2)
    # jos etäisyys alle 1, niin piste on 1-ympyrän sisällä
    if etaisyys < 1:
        sisalla += 1        # lisätään 1-ympyrän sisällä olevien lkm yhdellä.

    # lisätään arvottujen pisteiden lukumäärää yhdellä
    arvottu += 1

# lasketaan piin likiarvo saadulla kaavalla
pii = 4 * sisalla / simulointiLkm

# tulostus 2 desimaalilla
print(f"Piin likiarvoksi saatiin: {pii:.3f}")
