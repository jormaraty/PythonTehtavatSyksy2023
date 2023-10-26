import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )

def hae_lentokentta(ICAO_koodi):
    ICAO_monikko = (ICAO_koodi,)
    sql = "SELECT name, municipality FROM airport WHERE ident = %s;"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, ICAO_monikko)
    if kursori.rowcount > 0:
        tulos = kursori.fetchone()
    else:
        tulos = ""

    return tulos

ICAO_koodi = input("Anna lentoaseman ICAO-koodi:\n")
lentokentta = hae_lentokentta(ICAO_koodi)

if len(lentokentta) > 0:
    print(f"Lentoaseman nimi on {lentokentta['name']} ja lentoaseman sijaintikunta "
          f"on {lentokentta['municipality']}.")
else:
    print("Koodilla ei löytynyt tietoja")