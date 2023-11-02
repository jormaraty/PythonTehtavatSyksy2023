# tämä kirjasto sisältää nettihakujen tarvitsemia toimintoja
import requests

'''
    Virhealtis koodi laitetaan try-osion sisään.
    -   jos try-osan sisällä oleva koodi suoritetaan ilman ongelmia,
        niin except-osaa ei suoriteta ollenkaan.
    -   jos try-osassa tapahtuu poikkeustilanne (virhe), niin
        try-osan suoritus lopetetaan välittömästi ja siirrytään except-osaan.
        Except-osion suorituksen jälkeen ei palata enää takaisin try-osan suoritukseen.
    -   Poikkeuskäsittelijä poistaa ohjelman virhetilanteen, ja ohjelma voi jatkua normaalisti.
'''

# Ahaa, nyt ei tarvitse kysyä käyttäjältä mitään

# Pyynnön malli: https://api.chucknorris.io/jokes/random
# nettiin lähetettävä lopullinen hakulause
pyyntö = "https://api.chucknorris.io/jokes/random"

# Debug: tulostetaan lopullinen hakulause testausvaiheessa.
# Vinkki: kopioi hakulause selaimeen ja katso toimiiko se.
print(pyyntö)

try:
    # haetaan netistä data, otetaan se vastaan sellaisena ('raakadata')
    vastaus = requests.get(pyyntö)
    # tarkistetaan että onnistuiko hakuoperaatio (200 = ok)
    if vastaus.status_code==200:
        # jos haku onnistui, niin muutetaan saatu data json-muotoon
        json_vastaus = vastaus.json()
        # json-datan käsittely tähän
        print("Tässä sinulle Chuck Norris vitsi, ole hyvä")
        print(json_vastaus ["value"])
except requests.exceptions.RequestException as e:
    # tänne tullaan, jos hakutapahtumassa tuli poikkeustilanne (virhe)
    print ("Hakua ei voitu suorittaa.")

# tämä tulostetaan aina, onnistuiko datan haku tai ei
print("Hakutapahtuma on ohi.")