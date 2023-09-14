# otetaan käyttöön tietokanta-ajuri
import mysql.connector

# Funktio hakee lentokentän nimen ja sijaintikunnan
# parametrina saadun ICAO-koodin perustella.
# Funktio tulostaa saadut tiedot, ei palauta mitään.


def haeKentta(icao):
    # suoritettava sql-lauseen alkuosa
    sql = "SELECT NAME, municipality FROM airport"
    # lisätään vielä loppuosa, huom: icao-koodi täytyy ympyröiä '-merkeillä
    sql += " WHERE ident = '" + icao + "'"
    # tulostetaan saatu sql-lause sellaisenaan
    print(sql)
    # luodaan ns. kursori, sen avulla tehdään sql-toiminnot
    kursori = yhteys.cursor()
    # pyydetään kursoria suorittamaan edellä luotu sq-lause
    kursori.execute(sql)
    # pyydetään kursoria hakemaan hakutulokset, otetaan talteen muuttujaan 'tulos'.
    tulos = kursori.fetchall()
    # kysytään kursorilta, että saatiinko kyselystä vastausrivejä
    if kursori.rowcount > 0:
        # tulostetaan hakutuloksen tiedot rivi kerrallaan
        for rivi in tulos:
            print(f"Lentoaseman nimi: {rivi[0]}, kunta: {rivi[1]}")
    else:
        # kursori.rowcount = 0 eli haulla ei löytynyt yhtään tulosriviä
        print("Emme löytäneet ICAO-koodillasi yhtään lentoasemaa.")

    return


# -- pääohjelma alkaa --
# muodostetaan yhteys tietokantaan
# Huom: nyt open tunnukset ovat tosi vaaralliset (oletustunnukset).
# host='127.0.0.1' viittaa omaan koneeseen (alias on 'localhost'),
# eli tietokannan on sijaittava omalla koneellasi.
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )

# kysytään käyttäjältä lentoaseman ICAO-koodi
koodi = input("Annan kentän ICAO-koodi: ")
# kutsutaan funktiota, joka hakee tiedot tietokannasta,
# funktio tarvitsee lähtötietona/parametrina lentoaseman ICAO-koodin.
haeKentta(koodi)