###
Versio: su 1.10
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
        - käyttäjä voi kysyä lentoasemalla on nyt
        - käyttäjä voi lentää toiselle kentälle (su 1.10 versio ei vielä osaa...)

Toteutuksen tavoitteet:
        - pääohjelma on pieni ja selkeä
            - löytyy tiedostosta 'aloitus.py'
        - pääosa toiminnoista tapahtuu funktioissa
        - olen laittanut pääosan funktioista moduuliin funktiot.py (tai funktiot_param.py).
            - omat funktiot otetaan mukaan 'aloitus.py'-tiedostossa import-lauseella.

Funktioista on nyt 2 eri toteutusta.
    - esimerkissä on funktioista 2 rinnakkaista toteutusta, molemmissa on samat toiminnot.
        - funktiot.py: funktiot on tehty kuten kurssin Python-materiaalissa on esitetty.
        - funktiot_param.py: sql-funktioista on tehty ns. parametrisoidut versiot
            - osa opettajista on esittänyt tämän tekniikan
    - valitse funktioista vain toinen versio
        - molemmissa .py-tiedostoissa on saman nimiset funktiot, toteutustapa poikkeaa hieman.
    - valinta tapahtuu tiedostossa 'aloitus.py', siellä on rivit:
        # ladataan omat funktiot mukaan, valitse alta jompi kumpi versio
            from funktiot import *
            # from funktiot_param import *


= = = = =     = = = = =     = = = = =
***  Kuinka saan esimerkin toimimaan?  ***

Aloitus:
    - suorita aluksi 'db_start.sql'-tiedosto
        - siinä luodaan uusi käyttäjä ja annetaan sille rajoitetut oikeudet
    - Varsinainen ohjelmisto sisältää 2 tiedostoa.
        - aloitus.py:
            - tästä ohjelman suoritus alkaa
            - sisältää ns. pääohjelman
        - funktiot.py / funktiot_param.py
            - vaihtoehtoisia, valitse vain jompi kumpi
            - valinta tapahtuu 'aloitus.py'-tiedoston import lauseella, ks edeltä.
    - Ohjelma on toimintavalmis, eikun kokeilemaan ja ihmettelemään.
= = = = =     = = = = =     = = = = =

Toivottavasti tällä pääsette eteenpäin!
jr




