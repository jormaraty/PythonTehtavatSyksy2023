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

# Haetaan ja tulostetaan lentokentän tiedot, parametrina kentän icao-koodi.
# Funktio hakee tiedot sanakija-muodossa.
def lentokentan_tiedot(loc):
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
    # tulostetaan käyttäjälle lentokentän tiedot
    print(f"Lentokenttäsi tiedot: \nICAO-koodi: {tulos['ident']}, nimi: {tulos['name']}")
    return

