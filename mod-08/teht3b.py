'''
Ohjelma kysyy käyttäjältä kahden lentokentän ICAO-koodit.
Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
Sql-lauseissa käytetään nyt parametrisoitua versiota.
'''

import mysql.connector          # yhteys tietokantaan
import geopy.distance           # etäisyyden laskentaan

# Funktio palauttaa parametrina saamansa lentokentän gps-koordinaatit.
# Parametri sisältää kentän icao-koodin.
def haeGpsKoord(icao):
    # sql-lause, %s paikalle tulee parametrin (icao) arvo
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    # tehdään parametrista monikko sql-lausetta varten
    icaoMonikko = (icao, )
    # luodaan kursori tietokannan operaatioita varten
    # Huom: nyt ei pyydetä tulosta sanakirja-muodossa
    # (ei dictionary parametria)  => vastaus saadaan (lat,lon) monikkona.
    kursori = yhteys.cursor()
    # suoritetaan haku
    kursori.execute(sql, icaoMonikko)
    # luetaan 1 rivin tiedot
    tulos = kursori.fetchone()
    # palautetaan saatu hakutulos (sisältää lat ja lon arvot)
    return tulos

# Funktio laskee 2 gps-koordinaattien välisen etäisyyden kilometreina.
# Laskentaan käytetään pythonin geopy.distance-kirjastoa.
# funktio palauttaa lasketun etäisyyden
def laskeEtaisyys(gps1, gps2):
    # lasketaan gps-koordinaattien välinen etäisyys kilometreina
    etaisyys = geopy.distance.distance(gps1, gps2).km
    # palautetaan saatu etäisyys
    return etaisyys


# -- pääohjelma alkaa --
# muodostetaan yhteys tietokantaan
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='dbuser',
         password='sAL_a3ana',
         autocommit=True
         )

# kysytään ja haetaan eka kentän tiedot
icao = input("Anna eka lentokentän ICAO-koodi : ")
gps1 = haeGpsKoord(icao)

# kysytään ja haetaan toisen kentän tiedot
icao = input("Anna toisen lentokentän ICAO-koodi : ")
gps2 = haeGpsKoord(icao)

# lasketaan gps-koordinaattien välinen etäisyys
etaisyys = laskeEtaisyys(gps1, gps2)

# tulostetaan vastaus täysinä kilometreinä (0 kpl desimaaleja)
print(f"Kenttien välinen etäisyys on {etaisyys:.0f} km.")


