# Funktio saa parametrina listan kokonaislukuja.
# Funktio palauttaa uuden (toisen) listan, jossa
# on vain alkuperäisen listan parilliset numerot.
def muokkaa(lista):
    # luodaan tyhjä lista parillisia lukuja varten
    # Huom: tämä lista näkyy vain funktion sisällä.
    parilliset = []

    # käydään alkuperäisen listan luvut yksitellen läpi,
    # alkuperäisen listan numero tulee muuttujan 'luku' arvoksi.
    for luku in lista:
        # jos muuttuja luku sisältää parillisen luvun,
        # niin lisätään se uuteen listaan.
        if luku % 2 == 0:
            parilliset.append(luku)

    # palautetaan uusi lista kutsujalle
    return parilliset


# -- pääohjelma alkaa --
# luodaan lista kokonaislukuja
alkuperainen = [1, 3, 4, 5, 7, 8, 11, 12, 23, 24, 25]

# kutsutaan funktiota, annetaan sille parametrina äsken luotu lista.
# Muista ottaa funktion palauttama lista talteen:
# nyt funktion paluuuarvo talletetaan muuttujaan 'muokattu'.
muokattu = muokkaa(alkuperainen)

# tulostetaan alkuperäinen lista ja funktion palauttama lista.
print("Alkuperäinen lista:")
print(alkuperainen)
print("Funktion palauttama lista:")
print(muokattu)
