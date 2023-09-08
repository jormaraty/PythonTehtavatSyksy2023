# Funktio saa alkuarvona (parametrina) listan kokonaislukuja.
# Funktio laskee laskee listassa olevien lukujen summan,
# ja palauttaa kutsujalle saamansa lopputuloksen.
def laske(lista):
    tulos = 0       # lukujen summa, palautettava arvo

    # käydään listan alkiot yksitellen läpi,
    # lisätään listan alkion (solun) arvo muuttujaan 'tulos'.
    for alkio in lista:
        # tulos = tulos + alkio
        tulos += alkio
    # palautetaan saatu lopputulos kutsujalle
    return tulos

# -- pääohjelma alkaa --
luvut = [2, 3, 4, 6]        # lista, jolle on annettu heti arvoja

# kutsutaan funktiota, annetaan sille luotu lista parametrina,
# muista ottaa paluuarvo talteen!
vastaus = laske(luvut)
# tulostetaan saatu vastaus
print(f"Funktion mukaan listan lukujen summa = {vastaus} ?!?")

