/*
        ../Teht4e.html käyttää tätä js-koodia.
        E-ryhmäläiset korjasivat open bugin, kiitoksia!
        jr
 */

'use strict';

// tyhjä lista tulevia lukuja varten
const numerot = [];

// kysytään käyttäjältä lukuja, kunnes saadaan nolla.
// Nyt kysyn eka luvun ennen while-toistoa
let arvo = +prompt("Anna kokonaisluku, nolla lopettaa: ");

while (arvo !== 0) {
    // lisätään saatu arvo listaan
    numerot.push(arvo);
    // muista kysyä uusi arvo!
    arvo = +prompt("Anna kokonaisluku, nolla lopettaa: ");
}

// järjestetään listan luvut suurimmasta pienimpään
numerot.sort((a,b) => a-b);     // luvut pienimmästä suurimpaan
numerot.reverse();                       // -> suurin ensin.

// muodostetaan html-sivulle lähetettävä merkkijono
let htmlKoodi = `<ul>`;

// käydään numerolista läpi for...of -tekniikalla
for (let alkio of numerot) {
    htmlKoodi += `<li> ${alkio} </li>`;
}
htmlKoodi += `</ul>`;

// etsitään tulostuksen paikka html-sivulta
const tpaikka = document.querySelector('#jstulostus');

// tulostetaan data web-sivulle
tpaikka.innerHTML = htmlKoodi;