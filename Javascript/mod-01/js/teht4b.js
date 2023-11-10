/*
        Tämä tiedosto sisältää ../teht4b.html tarvitseman js-koodin
 */

'use strict';

const nimi = prompt("Mikä on nimesi: ");

// arvotaan tuvan numero väliltä 1 .. 4
const tuvanNro = Math.floor( Math.random() * 4) + 1;

// päätellään tuvan nimi (1 = Rohkelikko, 2 = Puuskupuh jne)
let tuvanNimi = 'arvoitus';

switch (tuvanNro) {
        case 1:
                tuvanNimi = "Rohkelikko";
                break;
        case 2:
                tuvanNimi = "Puuskupuh";
                break;
        case 3:
                tuvanNimi = "Korpinkynsi";
                break;
        case 4:
                tuvanNimi = "Luihuinen";
                break;
        default:
                tuvanNimi = "Lajitteluhattu on huppelissa!";
}

// html-sivulle tulostettava lause, huomaa `...` merkit
const vastaus = `${nimi}, sinä olet ${tuvanNimi}`;

// etsitään tulostuksen paikka html-sivulta
const tpaikka = document.querySelector('#jstulostus');

// tulostetaan data html-sivulle
tpaikka.innerHTML = vastaus;