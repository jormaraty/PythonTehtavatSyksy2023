# Ratkaisu 1/2:
# Annetaan alkuarvo, jolla päästään aina while-toistoon

# Tietokone arpoo luvun väliltä 1 .. 10.
# Kone kysyy käyttäjältä lukua, kunnes tämä arvaa oikein.
# Kone antaa käyttäjälle arvauksen jälkeen vinkin, esim. 'liian iso'.

# tämä kirjasto tarvitaan satunnaisluvun laskemiseen.
import random

# kone arpoo kokonaisluvun väliltä 1 .. 10.
arvottu = random.randint(1, 10)

# esitellään muuttuja, johon käyttäjän arvaus otetaan talteen.
# Idea: annetaan käyttäjän arvaukselle alkuarvo 0,
# jolloin päästään varmasti while-toistorakenteeseen.
arvaus = 0          # tähän muuttujaan talletetaan käyttäjän arvaus

# toistetaan, kunnes käyttäjä arvaa oikein
while arvaus != arvottu:
    # kysytään käyttäjän arvaus, muutetaan vastaus heti kokonaisluvuksi
    arvaus = int( input('Arvaa luku väliltä 1 .. 10: '))

    # kerrotaan, oliko vastaus liian suuri, pieni vai oikein
    # Alla olevasta rakenteesta tulostetaan aina vain 1 lause.
    if arvaus > arvottu:
        print("Arvaus oli liian suuri")
    elif arvaus < arvottu:
        print("Arvvaus oli liian pieni")
    else:
        print("Oikein")

# Vielä loppuonnittelut  (\n aiheuttaa rivinvaihdon)
print("Hienoa, ratkaisit numeron! \nNäkemiin!")