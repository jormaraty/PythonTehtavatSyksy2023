# luodaan monikko (tuple) eri vuodenajoille.
vuodenajat = ("kevät", "kesä", "syksy", "talvi")

# kysytään käyttäjältä kuukauden numero
nro = int( input("Kuinka mones kuukausi: ") )

# valitaan kuukauden numeron mukaan oikea alkio monikosta
# if nro >= 3 and nro <= 5:
if 3 <= nro <= 5:
    vastaus = vuodenajat[0]
elif 6 <= nro <= 8:
    vastaus = vuodenajat[1]
elif 9 <= nro <= 11:
    vastaus = vuodenajat[2]
elif 1 <= nro <=2  or  nro == 12:
    vastaus = vuodenajat[3]
else:
    vastaus = "tuntematon"

# tulostetaan vastaus
print(f"{nro}. kuukausi kuuluu vuodenaikaan {vastaus}.")
