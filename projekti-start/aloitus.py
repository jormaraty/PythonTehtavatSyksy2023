'''
    Tästä tiedostosta ohjelma käynnistyy.
'''


# ladataan omat funktiot mukaan, valitse alta jompi kumpi versio
from funktiot import *                    # sql-lauseet kurssin materiaalin mukaiset, perustapa.
# from funktiot_param import *            # sql-lauseet ovat ns. parametrisoituja

# ohjelman globaaleja tietoja
toiminto = '0'              # käyttäjän valitseman toiminnon numero.
user_icao = "EFHK"          # käyttäjän lentokentän icao-koodi (aluksi Helsinki-Vantaa).


# tulostetaan käyttäjälle aloitusohjeet tms.
info()                      # löytyy 'funktiot.py' tai 'funktiot_param.py'

# muodostetaan yhteys tietokantaan, tämä tapahtuukin nyt toisessa moduulissa.
# nyt yhteys-olio sijaitsee 'funktiot.py' tai 'funktiot_param.py' moduulissa

# Päävalikko:
#   - näytetään käyttäjälle eri vaihtoehdot
#   - tässä pyöritään kunnes käyttäjä lopettaa pelin.
#   - \t = tab-näppäin, \n = rivinvaihto
while toiminto != '9':
    print("\nValitse seuraavista:")
    print("\t1 = Missä olen nyt:")
    print("\t2 = Listaa lentokenttien ICAO-koodit:")
    print("\t3 = Mihin lennetään: ")
    print("\t9 = Lopetus")

    # Niksi: lueteen käyttäjän syöte merkkijonona vaikka pyydetään numeroa.
    # Miksi: ohjelma ei kaadu, jos käyttäjä syöttää jotakin roskaa..
    # nyt verrataankin arvoja merkkijonoon!?!
    toiminto = input("Valitse toiminto: ")

    if toiminto == '1':
        # haetaan lentokentän tiedot muuttujaan data
        data = hae_lentokentan_tiedot(user_icao)
        # tulostetaan lentokentän tiedot funktion avulla.
        tulosta_tiedot(data)

    elif toiminto == '2':\
        print("Toiminto ei ole vielä käytössä..")

    elif toiminto == '3':\
        print("Toiminto ei ole vielä käytössä..")

    elif toiminto == '9':\
        print("debug: while-toisto päättyy pian...")

    else:
        print("Tuntematon toiminto")


print("Kiitoksia pelaamisesta!")




