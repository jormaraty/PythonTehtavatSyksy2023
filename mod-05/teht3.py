# Luku on alkuluku, jos se on jaollinen vain 1:llä ja itsellään.
# Idea: jos käyttäjä antaa luvun 73 =>
# Jaetaan käyttäjän antamaa lukua arvolla 2, 3, 4, ..., 72.
# Jos käyttäjän luku on jaollinen yhdelläkin luvuista 1 ... 72,
# niin käyttäjän luku ei ole alkuluku. Muuten se on alkuluku.

# esitellään boolean-tyyppinen (True/False) muuttuja, joka kertoo onko käyttäjän luku alkuluku.
# Laitetaan alkuarvoksi True eli alkuoletus on että käyttäjän luku on alkuluku.
onAlku = True

# kysytään käyttäjältä tutkittava luku, muutetaan heti kokonaisluvuksi
luku = int(input("Anna kokonaisluku, niin kerron onko se alkuluku: "))


# jakaja on arvo, jolla käyttäjän lukua jaetaan.
# jakaja saa nyt arvot 2, 3, 4, ... (käyttäjän luku -1)
for jakaja in range(2, luku):
    # luku on jaollinen jakajan arvolla, jos jakojäännös on nolla
    if luku % jakaja == 0:
        # jos käyttäjän luku on jaollinen jakajan arvolla, niin luku ei ole alkuluku
        onAlku = False
        break               # break lopettaa heti toistorakenteen suorituksen

# kerrotaan tulos
# if onAlku == True:        # alla lyhyempi versio tästä yhtäsuuruuden vertailusta.
if onAlku:                  # Tämä toimii vain boolean tyyppisillä muuttujilla.
    # onAlku on True, jos tähän tultiin
    print(f"Lukusi {luku} ON alkuluku")
else:
    # onAlku on False, jos tänne tullaan
    print(f"Lukusi {luku} EI ole alkuluku")



