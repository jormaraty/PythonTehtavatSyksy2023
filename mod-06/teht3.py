# funktio saa alkuarvona (parametrina) gallonien lkm.
def muunna(gallonat):
    # muunnetaan parametrina saatu gallonien määrä litroiksi.
    litrat = 3.785 * gallonat
    # palautetaan saatu tulos kutsujalle
    return litrat

# -- pääohjelma alkaa --

# kysytään käyttäjältä tarvittavat lähtötiedot
gallons = float( input("Anna gallonien lkm: ") )
# arvoja kysytään kunnes saadaan negatiivinen luku
while gallons >= 0:
    # kutsutaan funktio, Muista ottaa paluuarvo talteen
    liters = muunna(gallons)
    # tulostetaan saatu tulos
    print(f"Gallonat litroina: {liters} litraa")
    # Muista kysyä gallonat uudelleen!!!
    gallons = float(input("Anna gallonien lkm: "))


