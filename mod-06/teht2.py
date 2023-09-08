import random as r          # r on nyt alias (lyhenne) kirjastolle random

# funktio, joka palauttaa arvotun nopan silmäluvn.
# Funktiolla on 1 parametri tahkonoppa, se kertoo nopan tahkojen lukumäärän.
# Ts. funktio palaluttaa nyt arvotun kokonaisluvun väliltä 1 ... tahkonoppa
def heitto(tahkonoppa):
    noppa = r.randint(1, tahkonoppa)
    return noppa

# -- pääohjelma alkaa  --
tahkot = int(input("Syötä tahkot: "))
maxArvo = tahkot        # nopan palauttama max arvo on tahkojen (sivujen) lkm

# muuttuja (True/False), joka kertoo että jatketaanko nopan heittämistä
jatketaan = True        # alkuarvono on True eli jatketaan heittämistä

# while jatketaan == True:      # alla on yleinen lyhennys tästä toistoehdosta
while jatketaan:
    heitot = heitto(tahkot)     # kutsutaan funktiota, paluuarvo sijoitetaan mjaan 'heitot'.
    print(heitot)
    # jos funktio palautti maksimiarvoon, niin lopetetaan
    if heitot == maxArvo:
        jatketaan = False

print("Sait nopan maksimiarvon, lopetetaan.")
