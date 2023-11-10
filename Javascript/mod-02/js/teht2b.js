/*
        ../teht2b.html käyttää tätä js-koodia.
 */

'use strict';

// tyhjä lista nimiä varten
const nimet = [];

const lkm = +prompt("Kuinka monta osallistujaa? ");

// kysytään osallistujien nimet ja lisätään ne listaan
for (let i = 0; i < lkm; i++) {
    let nimi = prompt("Anna osallistujan nimi: ");
    // lisätään saatu nimi listan loppuun
    nimet.push(nimi);
}

// järjestetään nimet aakkosjärjestykseen
nimet.sort();

// tulostetaan nimet järjestettyyn eli numeroituun listaan (<ol>).
// Aletaan muodostamaan html-sivulle tulevaa koodia
let htmlKoodi = `Osallistujat aakkosjärjestyksessä <br>`;
htmlKoodi += `<ol>`;         // listan aloitustagi

// listan läpikäynti ns. for..of -tekniikalla
for (let arvo of nimet) {
    htmlKoodi += `<li> ${arvo} </li>`;
}

htmlKoodi += `</ol>`;        // listan lopetustagi

// etsitään html-sivulta sopiva kohta tulostusta varten
const tpaikka = document.querySelector('#jstulostus');

// tulostetaan edellä muodostettu html-koodi web-sivulle
tpaikka.innerHTML = htmlKoodi;