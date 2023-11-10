'use strict';

// tehdään lista osallistujien nimiä varten
const nimet = [];

// kysytään osallistujien lukumäärä
const lkm = +prompt("Kuinka monta osallistujaa? ");

// kysyn osallistujien nimet ja lisään ne listaan
for (let i = 0; i < lkm; i++) {
    let nimi = prompt("Anna nimi: ");
    nimet.push(nimi);
}

// lajittelen nimet aakkosjärjestykseen
nimet.sort();

// etsitään html-sivulta tulostuksen paikka
const tpaikka = document.querySelector('#jstulostus');

// tulostetaan html-sivulle nimet järjestettyyn eli numeroituun listaan (<ol>)
tpaikka.innerHTML = `Nimet aakkosjärjestyksessä: <br>`;
tpaikka.innerHTML += `<ol>`;
// käydään lista läpi, käytän ns. for .. of -tekniikkaa
for (let alkio of nimet) {
    tpaikka.innerHTML += `<li> ${alkio} </li>`;
}
// tulostetaan listan lopputagi
tpaikka.innerHTML += `</ol>`;



