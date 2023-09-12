# Alla on Vesan tekemä toimiva ja hieno koodi.
# Se näyttää kuinka monikko voidaan purkaa jo koodissa eri muuttujiksi.
# Alempana on sitten sama koodi, jossa on käytetty monikkoa perusmuodossaan.

import random

def heitä():
    eka, toka = random.randint(1,6), random.randint(1,6)
    return eka, toka

noppa1, noppa2 = heitä()
print(f"Alkuperäinen: Nopista tuli {noppa1} ja {noppa2}.")


# -- Vaihtoehto 1: käytetty monikkoa sekä funktiossa että pääohjelmassa --
# Nyt funktio näyttää, että se palauttaa oikeasti yhden monikon.
# Edellä olevassa versiossa monikko oli puretty muuttujiksi eka ja toka.

def heitä2():
    numerot = random.randint(1,6), random.randint(1,6)
    return numerot      # funktio palauttaa yhden monikon

# pääohjelma kutsuu funktiota heita2 ja ottaa vastaan yhden monikon
vastaus = heitä2()
# tulostetaan vastaus, huomaa kuinka monikosta saadaan esille sen arvot.
print(f"Vaihtoehto 1: Nopista tuli {vastaus[0]} ja {vastaus[1]}.")


# -- Vaihtoehto 2: käytetty monikkoa vain funktiossa. --
# Nyt funktio näyttää, että se palauttaa oikeasti yhden monikon.
# Tässä versiossa funktio ei ota vastaan monikkoa vaan purkaa sen heti 2 muuttujaksi.

def heitä3():
    numerot = random.randint(1,6), random.randint(1,6)
    return numerot      # funktio palauttaa yhden monikon

# pääohjelma kutsuu funktiota heita3 ja purkaa heti saadun monikon 2 muuttujaksi
kolmas, neljas = heitä3()
# tulostetaan vastaus
print(f"Vaihtoehto 3: Nopista tuli {kolmas} ja {neljas}.")
