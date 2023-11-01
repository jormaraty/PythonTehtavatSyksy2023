'''
    Tässä versiossa on mukana myös poikkeustilanteiden (virhetilanteiden) käsittelyä.

    Virhealtis koodi laitetaan try-osion sisään.
    -   jos try-osan sisällä oleva koodi suoritetaan ilman ongelmia,
        niin except-osaa ei suoriteta ollenkaan.
    -   jos try-osassa tapahtuu poikkeustilanne (virhe), niin
        try-osan suoritus lopetetaan välittömästi ja siirrytään except-osaan.
        Except-osion suorituksen jälkeen ei palata enää takaisin try-osan suoritukseen.
    -   Poikkeuskäsittelijä poistaa ohjelman virhetilanteen, ja ohjelma voi jatkua normaalisti.

    Tässä koodissa on kaksi poikkeuskäsittelijää.
    -   jos esim. hakuosoite on virheellinen, niin sen hoitaa RequestException.
        Exception-poikkeuskäsittelijää ei silloin suoriteta.
    -   Exception-poikkeuskäsittelijä hoitaa ne poikkeustapaukset, joita ylempi
        RequestException-käsittelijä ei 'saa kiinni' eli ei osaa hoitaa.
'''

import requests

# Pyynnön malli: https://api.chucknorris.io/jokes/random
pyynto = "https://api.chucknorris.io/jokes/random"


try:
    # otetaan netistä tuleva data talteen json-formaatissa
    vastaus = requests.get(pyynto).json()

    # tulostetaan json-muotoinen data 'raakana'
    print(vastaus)
    # huomataan: data ei tule listan sisällä.

    print("Chuck Norris vitsi sinulle")
    print(vastaus["value"])

except requests.exceptions.RequestException as e:
    # tänne tullaan vain, jos try-osassa tapahtui jokin RequestException-poikkeustilanne
    print("Haku ei onnistunut, RequestException käsittely hoiti tilanteen tyylikkäästi")

except Exception as ex:
    # tämä poikkeuskäsittelijä hoitaa kaikki muut virhetilanteet
    print("Tapahtui jokin odottamaton virhe")

# haun jälkeen (onnistui tai ei) jatketaan aina tästä.
print("Hakutapahtuma on ohi.")

