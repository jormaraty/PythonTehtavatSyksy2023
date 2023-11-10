
/*
      Tämä sisältää teht3.html-tiedoston tarvitseman js-koodin.
 */

'use strict';

// prompt() palauttaa vastauksen aina merkkijonona
const lukuStr = prompt("Anna eka kokonaisluku: ");
// muunnetaan käyttäjän vastaus kokonaisluvuksi
// const lukuA = +lukuStr
const lukuA = parseInt(lukuStr);

// +prompt() muuntaa käyttäjän antaman arvon heti number-tyyppiseksi
const lukuB = +prompt("Anna toinen kokonaisluku: ");
const lukuC = +prompt('Anna vielä kolmas: ');

// lasketaan tulokset
const summa = lukuA + lukuB + lukuC;
const ka = (lukuA + lukuB + lukuC) / 3;
const tulo = lukuA * lukuB * lukuC;

// käytetään muotoiltua merkkijonoa (template string) tulostusta varten
// huomaa `...` merkit.
let tulostus =
    `Lukujesi summa = ${summa} <br>
     keskiarvo = ${ka} <br>
     tulo = ${tulo}`;

// tulostetaan vastaus html-sivulle
document.querySelector('#jstulostus').innerHTML = tulostus;
