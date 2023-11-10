'use strict';

// funktio, joka heittää noppaa ja palauttaa saadun silmäluvun
function heita() {
    // arvotaan kokonaisluku väliltä 1 .. 6
    const arvottu = Math.floor( Math.random() * 6) + 1;
    // palautetaan arvottu luku
    return arvottu;
}


// pääohjelma, joka kutsuu funktiota niin kauan, kunnes saadaan arvo 6.
// tämän jälkeen ohjelma tulostaa kaikki saadut silmäluvut html-sivulle.

// tyhjä lista arvottuja lukuja varten
const arvotutLuvut = [];

// muuttuja, johon otetaan talteen funktion palauttama arvo,
// annetaan sille alkuarvo, jolla mennään aina while-toiston sisään
let silmaluku = 0;

while (silmaluku != 6) {
    // kutsutaan funktiota, joka heittää noppaa,
    // lisätään saatu silmäluku listaan.
    silmaluku = heita();
    arvotutLuvut.push(silmaluku);
}

// muodostetaan html-sivulle tulostettava html-koodi
let htmlKoodi = `<ul>`;
for (let alkio of arvotutLuvut) {
    // käydään yksitellen jokainen listan umero läpi
    htmlKoodi += `<li> ${alkio} </li>`;
}
htmlKoodi += `</ul>`;

// etsitään tulostuksen paikka html-sivulta
const tpaikka = document.querySelector('#jstulostus');

// tulostetaan saatu teksti html-sivulle siellä p-tagin sisällä jo
// olevan sisällön perään. Käytetään siis '+=' operaatiota.
tpaikka.innerHTML += htmlKoodi;
