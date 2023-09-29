#
# Sinun täytyy olla kirjautuneena root-tunnuksella.
# Muilla ei ole tarvittavia oikeuksia.
# Jos lentokenttien tiedot eivät ole flight_game-tietokannassa, niin
# muuta alla olevista komennoista 'flight_game' oman tietokantasi nimeksi.
#

# luodaan uusi käyttäjä ('dbuser') sekä määrätään hänen salasanansa
CREATE USER 'dbuser'@'localhost' IDENTIFIED BY 'sAL_a3ana';

# annetaan äsken luodulle käyttäjälle oikeudet vain flight_game-tietokantaan
GRANT SELECT, UPDATE, DELETE, INSERT ON flight_game.* TO 'dbuser'@'localhost';
# varmistetaan, että uudet asetukset astuvat heti voimaan
FLUSH PRIVILEGES;