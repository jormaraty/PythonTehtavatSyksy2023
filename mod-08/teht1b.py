# Tässä versiossa SQL-lause muodostetaan eri tavalla ns. parametrisoimalla.
# Käyttäjän antamaan arvoon viitataan sql-koodissa merkinnällä '%s'.
# Varsinainen parametri annetaan sql-lauselle vasta suorituksen yhteydessä.

# Toinen iso on ero: tässä versiossa funktio tekee vain hakutoiminnon tietokannasta.
# Pääohjelma hoitaa kaiken kommunikoinnin käyttäjän kanssa.

import mysql.connector

# funktio hakee kentän tiedot saamansa icao-koodin perusteella.
# Funktio palauttaa saamansa kentän tiedot sanakirja-tietorakenteessa.
# Funktio ei tulosta mitään.
def hae_lentokentta(ICAO_koodi):
    # muodostetaan parametrina saadusta koodista monikko.
    ICAO_monikko = (ICAO_koodi,)
    # sql-lause, parametrina (icao_koodi) saatu arvo tulee %s paikalle.
    sql = "SELECT name, municipality FROM airport WHERE ident = %s;"
    # muodostetaan kursori, jolla avulla toimitaan tietokannan kanssa.
    # dictionary-parametri saa aikaan sen että tulosta käsiteltäessä sen
    # eri kenttiin voidaan viitata kentän nimillä indeksin numeron sijasta.
    kursori = yhteys.cursor(dictionary=True)
    # sql-lauseen suoritus. Nyt tarvitaan 2 parametria.
    # varsinainen sql-lause sekä sen tarvitsemat parametrit (icao_monikko).
    kursori.execute(sql, ICAO_monikko)
    # pyydetään kursorilta yksi hakutulos (fetcone)
    tulos = kursori.fetchone()

    # palautetaan saatu hakutulos pääohjelmalle.
    return tulos


# -- pääohjelma alkaa --
# muodostetaan yhteys tietokantaan
# host='127.0.0.1' viittaa omaan koneeseen (alias on 'localhost'),
# eli tietokannan on sijaittava omalla koneellasi.
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='dbuser',
         password='sAL_a3ana',
         autocommit=True
         )

# kysytään käyttäjältä lentoaseman ICAO-koodi
koodi = input("Annan kentän ICAO-koodi: ")
# kutsutaan funktiota, joka hakee tiedot tietokannasta,
# funktio tarvitsee lähtötietona/parametrina lentoaseman ICAO-koodin.
# Nyt funktio palauttaa saamansa lentokentän tiedot, otetaan ne talteen (data)
data = hae_lentokentta(koodi)

# tarkistetaan että onko funktion palauttama data on tyyppiä sanakirja, eli
# tarkistetaan löysikö haku todellista dataa.
if isinstance(data, dict):
    print(f"Lentoaseman nimi on {data['name']} ja sijaintikunta on {data['municipality']}.")
else:
    print("Hakukoodillasi ei löytynyt dataa")
