/*
      Tämä js-tiedosto on ../teht10.html tiedostoa varten.
 */

'use strict';

// kysytään käyttäjältä tarvittavat lähtötiedot
const noppienLkm = +prompt(("Kuinka monta noppaa: "));
const tavoite = +prompt("Mitä summaa tavoittelet? ");

// alkuarvoja
const toistoLkm = 10000;    // kuinka monta kertaa heitän noppia
let toistoja = 0;           // kuinka monta kertaa olen heittänyt noppia
let osumia = 0              // kuinka monta kertaa on saatu haluttu summa

// heitetään noppia 'toistoLkm' kertaa, jos summaksi saatiin haluttu
// arvo, niin kasvatetaan laskuria 'osumia' yhdellä.
for (let i = 0; i < toistoLkm; i++)  {
    let summa = 0;      // noppien summa

    for (let nro = 0; nro < noppienLkm; nro++)  {
        // lisätään noppien summaan saatu heiton tulos
        summa += Math.floor(Math.random() * 6) + 1
    }

    // oliko noppien summa tavoiteltu arvo
    if (summa == tavoite) {
        osumia++;
    }
}

// lasketaan osumaprosentti
const osumapros = 100 * (osumia / toistoLkm);

// etsitään tulostuskohta html-sivulta
const tulostuskohta = document.querySelector('#jstulostus');

// tulostetaan vastaus html-sivulle,
// huom: prosenttiluku ilmoitetaan 2 desimaalilla (toFixed)
tulostuskohta.innerHTML =
    `${noppienLkm} noppaa, summa on ${tavoite},
     todennäköisyys on noin ${osumapros.toFixed(2)}%`;