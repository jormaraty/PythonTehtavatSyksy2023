# luodaan tyhjä sanakirja lentoaseman tietoja varten
lentoasemat = {}

# kysytään käyttäjältä toiminto eka kerran ennen while toistoa
tieto = input("Haluatko syöttää uuden lentoaseman (uusi), hakea jo syötetyn "
              "lentoaseman tiedot (haku) vai lopettaa (lopeta)?\n")

while tieto != "lopeta":
    if tieto == "uusi":
        ICAO_koodi = input("Anna lentoaseman ICAO-koodi:\n")
        lentoaseman_nimi = input("Anna lentoaseman nimi:\n")
        lentoasemat.update({ICAO_koodi: lentoaseman_nimi})

    elif tieto == "haku":
        ICAO_koodi = input("Anna lentoaseman ICAO-koodi:\n")
        if ICAO_koodi in lentoasemat:
            print(f"{ICAO_koodi} koodin vastaava lentoasema on "
                  f"{lentoasemat[ICAO_koodi]}.")
        else:
            print(f"Lentoasema ei löytynyt ICAO-koodilla {ICAO_koodi}.")

    else:
        print("Tuntematon komento.")

    tieto = input("Haluatko syöttää uuden lentoaseman (uusi), hakea jo syötetyn "
                  "lentoaseman tiedot (haku) vai lopettaa (lopeta)?\n")