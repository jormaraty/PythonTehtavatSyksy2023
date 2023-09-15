# Tämä on laaja tehtävä, hyvää harjoittelua projektia varten.
# Suosittelen vahvasti, että teet eri toiminnot omiin funktioihinsa.

# funktio lisää uuden lentokentän tiedot sanakirjaan.
# Vaatii lähtötietona sanakirjan, johon lisäys tehdään.
def lisaa(kentat):
    # kysy käyttäjältä lentokentän ICAO-koodin ja lentokentän nimen.
    icao = input("Anna kentän ICAO-koodi: ")
    nimi = input("Anna kentän nimi: ")
    # lisää uusi kenttä sanakirjaan.
    kentat[icao] = nimi
    print("Lentokentän tiedot lisätty sanakirjaan")
    return

# funktio hakee lentokentän nimen ICAO-koodin avulla.
# Vaatii lähtötietona/parametrina sanakirjan, joka sisältää kenttien tiedot
def hae(airpots):
    # kysytään kentän ICAO-koodi
    icao = input("Anna kentän ICAO-koodi: ")
    # haetaan kentän nimeä saadulla koodilla
    if icao in airpots:
        # kentän tunnus löytyi
        print(f"Lentokentän tunnus: {icao}, nimi: {airpots[icao]} \n")
    else:
        print("Tunnuksella ei löytynyt mitään tietoja. \n")


# -- pääohjelma alkaa --

# luo uusi sanakirja, johon voit lisätä esim. Helsinki-Vantaan lentoaseman tiedot.
# Laita tässä luotu sanakirja funktioiden kutsujen parametriksi.
lentokentat = {}        # tyhjä sanakirja

# annetaan toiminto-muuttujalle arvo, jolla päästään while toistoon
toiminto = 0

# pysytään while-toistossa, kunnes käyttäjä lopettaa
while toiminto != 3:
    print("Valise toiminto: \n1 = lisää kenttä \n2 = hae kentän tiedot \n3 = lopeta")
    toiminto = int( input("Anna vaihtoehto: 1/2/3: ") )

    if (toiminto == 1):
        # kutsutaan hommat hoitavaa funktiota, annetaan parametrina sanakirja
        lisaa(lentokentat)
    elif (toiminto == 2):
        hae(lentokentat)
    elif (toiminto == 3):
        print("Lopetetaan")
    else:
        print("\nTuntematon toiminto")
