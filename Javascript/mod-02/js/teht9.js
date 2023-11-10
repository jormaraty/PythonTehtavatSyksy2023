
'use strict';

// funktio palauttaa uuden taulukon (listan), joka sisältää
// vain parilliset luvut alkuperäisestä taulukosta.
// Funktio ei tee muutoksia alkuperäiseen taulukkoon.
function even(lista) {
    // tehdään uusi, tyhjä taulukko/lista, joka lopuksi palautetaan
    let uusiLista = [];

    // käydään parametrina saadun taulukon luvut yksitellen läpi.
    // Jos luku on parillinen, niin lisätään se uuteen listaan.
    for (let alkio of lista) {
        if (alkio % 2 == 0) {
            // löytyi parillinen luku, jos tänne tultiin
            uusiLista.push(alkio);
        }
    }

    // palautetaan lopuksi parilliset luvut sisältävä uusi taulukko/lista.
    return uusiLista;
}


// -- pääohjelma --

// luodaan taulukko, joka sisältää kokonaislukuja
const luvut = [1, 4, 5, 6, 7, 9, 12, 15, 18, 22, 29];

// tulostetaan konsoliin listan sisältö
console.log("Alkuperäinen lista aluksi: " + luvut);

// kutsutaan funktiota, parametrina annetaan alkuperäinen taulukko.
// otetaan funktion palauttama lista talteen
console.log("- kutsutaan funktiota -");
let vastaus = even(luvut);

// tulostetaan alkuperäinen ja funktion palauttama lista konsoliin.
console.log("Alkuperäinen lista lopuksi: " + luvut);
console.log("Funktion palauttama lista: " + vastaus);