import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Arwen1997',
         autocommit=True
         )

def hae_lentokentat(maakoodi, tyyppi):
    parametrit_monikkona = (maakoodi, tyyppi)
    sql = "SELECT * FROM airport WHERE iso_country = %s AND type = %s ORDER BY name;"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, parametrit_monikkona)
    tulos = kursori.fetchall()
    return tulos

def hae_lentokentta(icao):
    parametrit_monikkona = (icao,)
    sql = "SELECT * FROM airport WHERE ident = %s;"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, parametrit_monikkona)
    tulos = kursori.fetchone()
    return tulos

kentat = hae_lentokentat("FI", "heliport")
for kentta in kentat:
    print(kentta["name"], kentta["iso_country"])

yksi_kentta = hae_lentokentta("EFHK")
print(yksi_kentta["name"])