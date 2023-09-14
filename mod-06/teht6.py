# Funktio saa parametreina pizzan halkaisijan (cm) ja pizzan hinnan (€).
# Funktio palauttaa pizzan yksikköhinnan (€ / m^2).
import math

def laske(halk, hinta):
    # lasketaan pizzan säde metreinä (huom: halkaisija on cm)
    sade = halk / 200   # jos halkaisija on 100cm => säde on 0,5 m.
    # lasketaan pizzan pinta-ala neliömetreinä (pii * r^2)
    ala = math.pi * sade**2
    # lasketaan yksikköhinta (€ / m^2)
    yksHinta = hinta / ala
    # palautetaan saatu vastaus (pizzan yksikköhinta)
    return yksHinta


# -- pääohjelma alkaa --
# kysytään eka pizzan tiedot, muunnetaan vastaukset heti numeroksi
hinta1 = float( input("Annna eka pizzan hinta (€): "))
halk1 = int( input("Anna eka pizzan halkaisija(cm): "))
# vastaavasti toisen pizzan tiedot
hinta2 = float( input("Annna toisen pizzan hinta (€): "))
halk2 = int( input("Anna toisen pizzan halkaisija(cm): "))

# annetaan funktion laskea yksikköhinta kummallekin pizzalle.
# Otetaan tietenkin funktion palauttama arvo talteen muuttujaan
ekaYksHinta = laske(halk1, hinta1)
tokaYksHinta = laske(halk2, hinta2)

# huom: nyt mitä halvempi yksikköhinta => sitä parempi vastine rahalle
if ekaYksHinta < tokaYksHinta:
    print(f"Eka pizza antaa enemmän vastinetta rahoillesi: {ekaYksHinta:.2f} €/m^2")
elif ekaYksHinta > tokaYksHinta:
    print(f"Toka pizza antaa enemmän vastinetta rahoillesi: {tokaYksHinta:.2f} €/m^2")
else:
    print("Molemmat pizzat antavat saman vastineen rahoillesi")

# tulostetaan vielä yksikköhinnat
print(f"yksikköhinnat; eka: {ekaYksHinta:.2f}, toka: {tokaYksHinta:.2f}")
