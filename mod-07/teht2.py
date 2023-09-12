# luodaan aluksi tyhjä joukko
nimet = set()

# annetaan alkuarvo, jolla päästään aina while toistoon
nimi = "Dummy"

print("Kysyn nimiä, pelkkä Enter lopettaa")

# kysytään nimiä, kunnes käyttäjä antaa tyhjän merkkijonon ""
while nimi != "":
    # kysytään käyttäjältä uusi nimi
    nimi = input("Anna nimi: ")

    # testaan, onko saatu nimi jo listassa vai ei.
    # Jos nimi ei ole listassa, niin lisätään se listaan
    if nimi in nimet:
        print("Nimi oli jo annettu")
    else:
        print("Uusi nimi, lisään listaan")
        # lisätään uusi nimi listaa
        nimet.add(nimi)

# lopputervehdys
print("Kiitos ja näkemiin")


