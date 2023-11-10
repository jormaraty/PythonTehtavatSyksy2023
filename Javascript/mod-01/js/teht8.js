/*
      Tämä tiedosto sisältää ../teht8.html tarvitseman js-koodin
 */

'use strict';

// kysytään aloitus- ja lopetusvuosi
const alku = +prompt("Anna aloitusvuosi: ");
const loppu = +prompt("Anna lopetusvuosi: ");

// aletaan koostamaan html-sivulle tulevaa koodia, huomaa `...`
let htmlKoodi =
    `Karkausvuodet väliltä ${alku} - ${loppu}: <br>
     <ul>`;     // listan aloitus

// käydään jokainen vuosi läpi valitulta väliltä,
// jos vuosi on karkausvuosi, niin lisätään se listaan (huomaa +=)
for (let vuosi = alku; vuosi <= loppu; vuosi++)  {
    if (vuosi % 400 == 0  || (vuosi % 4 == 0  && vuosi % 100 != 0) ) {
        // tulostetaan entisen perään += avulla
        htmlKoodi += `<li>${vuosi} </li>`;
    }
}

// lopetetaan ul-lista
htmlKoodi += `</ul>`;

// etsitään tulostuksen paikka html-sivulta
const tpaikka = document.querySelector('#jstulostus');

// tulostetaan saatu html-koodi web-sivulle
tpaikka.innerHTML = htmlKoodi;
