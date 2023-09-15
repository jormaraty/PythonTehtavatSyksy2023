import mysql.connector
import geopy.distance       # etäisyyden laskentaan

# Huom: ohjelma olettaa että annetaan olemassaoleva
# lentokentän koodi. Ohjelma kaatuu väärään icao-koodiin.

# muodostetaan yhteys tietokantaan
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='dbuser',
         password='sAL_a3ana',
         autocommit=True
         )

# ksytään ja haetaan eka kentän tiedot
icao = input("Anna lentokentän 1 ICAO-koodi : ")
sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '" + icao + "'"
kursori = yhteys.cursor()
kursori.execute(sql)
# luetaan 1 rivin tiedot
tulos = kursori.fetchone()
# otetaan saadusta tulosrivistä talteen gps-koordinaatit (lat, lon)
lat = tulos[0]
lon = tulos[1]
# talletetaan eka lentokentän gps-koordinaatit (lat, lon) muuttujaan 'airport1'.
airport1 = (lat, lon)

# kysytään ja talletetaan vastaavasti 2. lentokentän tiedot
icao = input("Anna lentokentän 2 ICAO-koodi : ")
sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '" + icao + "'"
kursori = yhteys.cursor()
kursori.execute(sql)
# otetaan talteen 1 riviin tiedot
tulos = kursori.fetchone()
lat = tulos[0]
lon = tulos[1]
# otetaan taltee 2. lentpkentän gps-koordinaatit (lat, lon)
airport2 = (lat, lon)

# lasketaan lentokentten välinen etäisyys geopy.distance-kirjaston
# funktiolla distance (geopy.distance.distance).
# .km kertoo, että etäisyys määritellään kilometreinä.
etaisyys = geopy.distance.distance(airport1, airport2).km

# tulostetaan etäisyys kilometreinä, ilman desimaaleja.
print(f"Lentokenttien välinen etäisyys on {etaisyys:.0f} km.")