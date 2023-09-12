# luodaan aluksi tyhjä joukko
nimet = set()

# annetaan alkuarvo, jolla päästään aina while toistoon
nimi = "Dummy"

print("Kysyn nimiä, pelkkä Enter lopettaa")

# kysytään nimiä, kunnes käyttäjä antaa tyhjän merkkijonon ""
while nimi != "":
    # kysytään käyttäjältä uusi nimi
    nimi = input("Anna nimi: ")

    # testaan, onko saatu nimi jo joukossa vai ei.
    # Jos nimi ei ole joukossa, niin lisätään se joukkoon
    if nimi in nimet:
        print("Nimi oli jo annettu")
    else:
        # lisätään nimi joukkoon vain, jos se ei ole lopetusmerkki
        if nimi != "":
            print("Uusi nimi, lisään joukkoon")
            # lisätään uusi nimi joukkoon
            nimet.add(nimi)

# Xtra: listaan kaikki nimet joukosta ja lopputervehdys
print("Joukkorakenteesta löytyi seuraavia nimiä: ")
print(nimet)
print("Kiitos ja näkemiin")


