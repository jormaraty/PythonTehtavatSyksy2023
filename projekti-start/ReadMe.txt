###
Versio: ma 2.10
Versio päivittyy tarpeen mukaan.
###

Tämä Python-moduuli on tarkoitettu auttamaan Ohjelmisto 1-teeman projektin tekemistä.
Varsinkin niille, joiden on vaikea päästä alkuun.

Tämä esimerkki on vain yksi tapa lähteä liikkeelle,
eli voit vapaasti lähteän toteuttamaan projektia aivan eri tavalla.

Sopimus:
    - Tämä esimerkki hyödyntää SQL-osuudessa käytettyä 'flight_game'-tietokantaa.
        - tietokannasta haetaan vain lentokenttien ja eri maiden tiedot.
        - muut pelissä tarvittavat tiedot säilytetään python-ohjelmassa.
Miksi: meillä ei ole vielä tarpeeksi tehdä tarvittavia muokkauksia tietokantaan.
Ohjelmisto 2-teemassa muokataan itselle sopiva tietokanta.

Tavoite:
    Luodaan toimiva ohjelma, joka käynnistää pelin ja näyttää ohjeet käyttäjälle.
    Esimerkki tuntee vain Suomen lentokentät.
    Toiminnot:
        - käyttäjä voi kysyä millä lentoasemalla on nyt
        - käyttäjä voi lentää toiselle kentälle
        - rajoitus: käyttäjän on syötettävä validi icao-koodi, muuten ohjelma kaatuu...

Toteutuksen tavoitteet:
        - pääohjelma on pieni ja selkeä
            - löytyy tiedostosta 'aloitus.py'
        - pääosa toiminnoista tapahtuu funktioissa
        - olen laittanut pääosan funktioista moduuliin funktiot.py
            - omat funktiot otetaan mukaan 'aloitus.py'-tiedostossa import-lauseella.

= = = = =     = = = = =     = = = = =
***  Kuinka saan esimerkin toimimaan?  ***

Aloitus:
    - suorita aluksi 'db_start.sql'-tiedosto
        - siinä luodaan uusi käyttäjä ja annetaan sille rajoitetut oikeudet
    - Varsinainen ohjelmisto sisältää 2 tiedostoa.
        - aloitus.py:
            - tästä ohjelman suoritus alkaa
            - sisältää ns. pääohjelman
        - funktiot.py
            - sisältää funktioita, joissa suurin osa logiikasta tapahtuu.
    - Ohjelma on toimintavalmis, eikun kokeilemaan ja ihmettelemään.

= = = = =     = = = = =     = = = = =

Toivottavasti tällä pääsette eteenpäin!
jr




