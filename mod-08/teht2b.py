# Tämä tekee samat toiminnot kuin teht2.
# Tämä versio käyttää sql-kyselyssä muuttujien parametrisointia.
# Ero teht2: tässä versiossa on funktio, joka tekee varsinaisen työn.

# otetaan käyttöön tietokanta-ajuri
import mysql.connector


# Funktio hakee halutusta maasta eri tyyppisten lentokenttien lukumäärät.
# Funktio tarvitsee parametrina tarkasteltavan maan iso-koodin.
# Funktio palauttaa saamansa tiedot pääohjelmalle.
def lentokentatTyypeittain(maakoodi):
    # sql-lause vaatii nyt monikko-tyyppisen muuttujan
    maakoodi_monikko = (maakoodi,)
    # sql-lause, parametrina saatu maakoodi tulee %s paikalle
    sql = ("SELECT type, COUNT(TYPE) as amount FROM airport "
           "WHERE iso_country = %s GROUP BY TYPE;")
    # muodostetaan kursori.
    kursori = yhteys.cursor(dictionary=True)
    # suoritetaan sql lause.
    kursori.execute(sql, maakoodi_monikko)
    # haetaan tulos-muuttujaan kaikki löytyneet rivit (fetchall)
    # tuloksena saadaan lista tulosalkioita. Kukin tulosalkio on monikko.
    tulos = kursori.fetchall()
    # palautetaan saatu lista
    return tulos


# -- pääohjelma alkaa --
# muodostetaan yhteys tietokantaan
yhteys = mysql.connector.connect(
    database='flight_game',
    host='127.0.0.1',
    port=3306,
    user='dbuser',
    password='sAL_a3ana',
    autocommit=True
    )

# kysytään käyttäjältä maan iso-koodi
maakoodi = input("Anna maakoodi: ")

# kutsutaan funktiota, joka halutut tiedot tietokannasta ja palauttaa ne.
# Tuloksena saadut tiedot ovat lista-tietorakenteessa.
data = lentokentatTyypeittain(maakoodi)

# tarkistetaan, että saatiinko tietokannasta todellista dataa,
# eli sisältääkö lista ('data') tulosrivejä
if len(data) > 0:
    # 'data' on lista-tyyppinen tietorakenne.
    for rivi in data:
        # nyt 'rivi' on monikko-tyyppinen tietorakenne.
        print(f"{rivi['type']}: {rivi['amount']}")
else:
    print("Antamasi maakoodi oli virheellinen")