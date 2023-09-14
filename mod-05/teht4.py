# Tehdään tyhjä lista kaupunkien nimiä varten
kaupungit = []

print("Kysyn sinulta 5 kaupungin nimeä")

# Kysytään käyttäjältä 5 kaupungin nimet.
# Alla muuttuja nro saa arvot: 0, 1, 2, 3 ja 4. Eli 5 kpl.
for nro in range(5):
    # Ekalla kertaa nro = 0 => (nro+1) = 1
    city = input(f"Anna {nro+1}. kaupungin nimi: ")
    # lisätään saatu kaupungin nimi listan loppuun
    kaupungit.append(city)

# erikoismerkki \n tekee rivinvaihdon
print("\nTässä vielä kaupunkien nimet allekkain:")

# tulostetaan listan jokainen alkio yksitellen.
# Muuttujaan alkio tulee yksitellen jokainen listassa
# oleva kaupungin nimi. Muuttujan nimen 'alkio' saa itse keksiä.
for alkio in kaupungit:
    print(alkio)


