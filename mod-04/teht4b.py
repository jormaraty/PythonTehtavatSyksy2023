# Ratkaisu 2/2:
# Käyttäjältä kysytään arvaus kerran ennen while-toistoa.

# Tietokone arpoo luvun väliltä 1 .. 10.
# Kone kysyy käyttäjältä lukua, kunnes tämä arvaa oikein.
# Kone antaa käyttäjälle arvauksen jälkeen vinkin, esim. 'liian iso'.

# tämä kirjasto tarvitaan satunnaisluvun laskemiseen.
import random

# kone arpoo kokonaisluvun väliltä 1 .. 10.
arvottu = random.randint(1, 10)

# kysytään käyttäjältä eka arvaus ennen while-toistoa
arvaus = int(input('Arvaa kokonaisluku väliltä 1 .. 10: '))

# mennään while-toistoon, jos eka arvaus ei mennyt oikein.
# Huom: ei mennä while-toistoon, jos eka arvaus oli oikein.
# Jos mennään while-toistoon, niin toistetaan niin kauan kunnes saadaan oikea vastaus.
while arvaus != arvottu:
    # annetaan käyttäjälle vinkki, jos ei arvannut oikein
    if arvaus > arvottu:
        print("Arvaus oli liian suuri")
    elif arvaus < arvottu:
        print("Arvaus oli liian pieni")

    # muista kysyä uusi arvaus, jos edellinen ei ollut oikein
    if arvaus != arvottu:
        arvaus = int(input('Arvaa kokonaisluku väliltä 1 .. 10: '))

# tänne päästään vain jos on arvattu oikein
print("Onneksi olkoon! Arvasit lukuni!")

