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


# Tämä funktio tulostaa käyttäjälle aloitusohjeet
def info():
    # \t = TAB-näppäin, \n = rivinvaihto
    print("\tHIENO PELI\n")
    print("Tervetuloa tähän 'HIENO PELI'-ohjelmaan!")
    print("Nauti pelistä!\n")
    return


# Haetaan yhden lentokentän tiedot, parametrina kentän icao-koodi.
# Funktio palauttaa kentän tiedot kutsujalle.
def hae_lentokentan_tiedot(loc):
    # suoritettava sql-lause
    sql = "SELECT ident, name FROM airport WHERE ident = '" + loc + "'"
    # tulostetaan sql-lause testausvaiheessa
    print(f"debug: {sql}")

    # muodostetaan kursori, jolla avulla toimitaan tietokannan kanssa.
    kursori = yhteys.cursor()
    # sql-lauseen suoritus.
    kursori.execute(sql)
    # pyydetään kursorilta yksi hakutulos (fetchone),
    tulos = kursori.fetchone()

    # palautetaan lentokentän tiedot kutsujalle
    return tulos


# funktio tulostaa parametrina saadusta lentokentän datasta sen icao-koodin ja kentän nimen.
def tulosta_tiedot(airport):
    print("Lentokenttäsi tiedot: ")
    print(f"ICAO-koodi: {airport[0]}, Nimi: {airport[1]}")
    return


def siirry_kentalle():
    # kysytään käyttäjältä uuden kentän icao-koodi
    icao = input("Anna uuden kentän ICAO-koodi: ")
    # haetaan kentän tiedot valmiilla funktiolla
    data = hae_lentokentan_tiedot(icao)

    print("Hyvää matkaa..")

    # palautetaan pääohjelmalle uuden kentän icao-koodi
    return data[0]
