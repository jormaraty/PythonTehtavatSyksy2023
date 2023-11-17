'use strict';

// etsitään tulostuksen paikka html-sivulta
const targetElem = document.querySelector('#target');

// muodostetaan koodi, joka lähetetään html-sivulle
let htmlKoodi =
    `<li>First item</li>
     <li>Second item</li>
     <li>Third item</li>`

// lisätään html-koodi web-sivulle
targetElem.innerHTML = htmlKoodi;

// lisätään css luokkamääritys tulostuksen elementille
targetElem.classList.add('my-list');

