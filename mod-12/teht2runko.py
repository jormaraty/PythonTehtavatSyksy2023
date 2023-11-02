# tämä kirjasto sisältää nettihakujen tarvitsemia toimintoja
import requests

'''
    Virhealtis koodi laitetaan try-osion sisään.
    -   jos try-osan sisällä oleva koodi suoritetaan ilman ongelmia,
        niin except-osaa ei suoriteta ollenkaan.
    -   jos try-osassa tapahtuu poikkeustilanne (virhe), niin
        try-osan suoritus lopetetaan välittömästi ja siirrytään  except-osaan.
        Except-osion suorituksen jälkeen ei palata enää takaisin try-osan suoritukseen.
    -   Poikkeuskäsittelijä poistaa ohjelman virhetilanteen, ja ohjelma voi jatkua normaalisti.
'''

# kysytään käyttäjältä haun tarvitsemat lähtötiedot
hakusana = input("Anna hakusana: ")

# Pyynnön malli: https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# Huom: kun lisäät todellisen hakuehdon, niin poista myös sulut { }, esim. q={city name} => q=helsinki
# Nettiin lähetettävä lopullinen hakulause
pyyntö = "tähän_tulee_lopullinen_hakulause"

# Debug: tulostetaan lopullinen hakulause testausvaiheessa.
# Vinkki: kopioi hakulause selaimeen ja katso toimiiko se.
# Voit poistaa tämän, kun homma pelittää...
print(pyyntö)

try:
    # haetaan netistä data, otetaan se vastaan sellaisena ('raakadata')
    vastaus = requests.get(pyyntö)
    # tarkistetaan että onnistuiko hakuoperaatio (200 = ok)
    if vastaus.status_code==200:
        # jos haku onnistui, niin muutetaan saatu data json-muotoon
        json_vastaus = vastaus.json()
        # json-datan käsittely tähän

except requests.exceptions.RequestException as e:
    # tänne tullaan, jos hakutapahtumassa tuli poikkeustilanne (virhe)
    print ("Hakua ei voitu suorittaa.")

# tämä tulostetaan aina, onnistuiko datan haku tai ei
print("Hakutapahtuma on ohi.")