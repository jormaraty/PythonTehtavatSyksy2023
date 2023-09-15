# otetaan käyttöön tietokanta-ajuri
import mysql.connector

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

# kysytään käyttäjältä maakoodi
koodi = input("Annan maan ISO-koodi: ")

# suoritettava sql-lause
sql = "SELECT TYPE, COUNT(*) FROM airport WHERE iso_country = '" + koodi + "' GROUP BY TYPE;"
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
        print(f"Lentoaseman tyyppi: {rivi[0]}, lkm: {rivi[1]}")
else:
    # kursori.rowcount = 0 eli haulla ei löytynyt yhtään tulosriviä
    print("Emme löytäneet iso-koodillasi mitään tietoja.")
