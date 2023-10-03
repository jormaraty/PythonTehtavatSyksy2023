'''
    *** Tämä tiedosto on poistettu versiosta ma 2.10 ***
    
    Tämä tiedosto sisältää sql-lauseista ns. parametrisoidut versiot.
    Tätä ei ole käsitelty kurssin materiaaleissa.
    Vastaavat funktiot löytyvät tiedostosta funktiot.py
    Siinä funktiot ontehty kutten materiaaleissa on neuvottu.

'''
import mysql.connector              # yhteys tietokantaan vaatii tämän.

# otetaan yhteys tietokantaan.
# host='127.0.0.1' viittaa omaan koneeseen (alias on 'localhost'),
# eli tietokannan on sijaittava omalla koneellasi.
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='dbuser',
    password='sAL_a3ana',
    autocommit=True
)

# Tämä tulostaa käyttäjälle aloitusohjeet
def info():
    # \t = TAB-näppäin, \n = rivinvaihto
    print("\tHIENO PELI\n")
    print("Tervetuloa tähän 'HIENO PELI'-ohjelmaan!")
    print("Nauti pelistä!\n")
    return

# Haetaan yhden lentokentän tiedot, parametrina kentän icao-koodi.
# Funktio palauttaa kentän tiedot kutsujalle.
# Funktio hakee tiedot sanakirja-muodossa.
def hae_lentokentan_tiedot(loc):
    # sql-lause, %s paikalle tulee parametrin (icao) arvo
    sql = "SELECT ident, name, latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    # tehdään parametrista monikko sql-lausetta varten
    loc_monikko = (loc,)

    # muodostetaan kursori, jolla avulla toimitaan tietokannan kanssa.
    # dictionary-parametri saa aikaan sen että tulosta käsiteltäessä sen
    # eri kenttiin voidaan viitata kentän nimillä indeksin numeron sijasta.
    kursori = yhteys.cursor(dictionary=True)
    # sql-lauseen suoritus. Nyt tarvitaan 2 parametria.
    # varsinainen sql-lause sekä sen tarvitsemat parametrit (icao_monikko).
    kursori.execute(sql, loc_monikko)
    # pyydetään kursorilta yksi hakutulos (fetcone)
    tulos = kursori.fetchone()
    # palautetaan lentokentän tiedot kutsujalle
    return tulos


# funktio tulostaa parametrina saadusta lentokentän datasta sen icao-koodin ja kentän nimen.
def tulosta_tiedot(airport):
    print("Lentokenttäsi tiedot: ")
    print(f"ICAO-koodi: {airport['ident']}, Nimi: {airport['name']}")
    return
