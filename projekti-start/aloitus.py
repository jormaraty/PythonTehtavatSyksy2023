'''
    Tämä esimerkki on tarkoitettu niille, jotka eivät jotka eivät pääse projektissa alkuun.
    Käytetään tietokanta-osiosta tuttua flight_game-tietokantaa.
    Sopimus:
       - tietokannasta haetaan vain lentokenttien ja eri maiden tiedot.
       - muut pelissä tarvittavat tiedot säilytetään python-ohjelmassa.

    Aluksi:
        - tee tietokantaan uusi käyttäjä nimeltä 'dbuser' ja hänen oikeuksiaan rajataan.
        - Ei käytetä root-tunnusta, koska salasana näkyy koodista (vaarallista).
        - ohjeet tähän löytyvät tiedostosta 'db_start.sql'.

    Tavoite:
    Luodaan ohjelma, joka käynnistää pelin ja näyttää ohjeet käyttäjälle.
    Tehdään tässä toiminto, joka listaa käyttäjälle Suomen lentokenttien koodit.
    Käyttäjä voi myös liikkua eri lentokentille.

    Tavoite:
        - pääohjelma on pieni ja selkeä
        - pääosa toiminnoista tapahtuu funktioissa
        - olen laittanut pääosan funktioista moduuliin omat_funktiot.
    Toivottavasti tällä pääsette eteenpäin!

'''

from funktiot import *              # ladataan omat funktiot mukaan

# ohjelman globaaleja tietoja
toiminto = 0                # käyttäjän valitseman toiminnon numero.
user_icao = "EFHK"          # käyttäjän lentokentän icao-koodi (aluksi Helsinki-Vantaa).


# tulostetaan käyttäjälle aloitusohjeet tms.
info()
# muodostetaan yhteys tietokantaan,
# nyt yhteys-olio sijaitsee 'funktiot.py' moduulissa

# Päävalikko:
#   - näytetään käyttäjälle eri vaihtoehdot
#   - tässä pyöritään kunnes käyttäjä lopettaa pelin.
#   - \t = tab-näppäin, \n = rivinvaihto
while toiminto != 9:
    print("\nValitse seuraavista:")
    print("\t1 = Missä olen nyt:")
    print("\t2 = Listaa lentokenttien ICAO-koodit:")
    print("\t3 = Mihin lennetään: ")
    print("\t9 = Lopetus")
    toiminto = int(input("Valitse toiminto: "))

    if toiminto == 1:
        lentokentan_tiedot(user_icao)


print("Kiitoksia pelaamisesta!")




