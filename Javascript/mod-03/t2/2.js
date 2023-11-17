'use strict';

// etsitään tulostuksen paikka html-sivulta
const targetElem = document.getElementById('target');

// luodaan elementti listan eka riviä (<li> ... </li>) varten
const ekaElem = document.createElement('li');
// määritellään li-elementin sisältö
ekaElem.innerHTML = 'First item';

// luodaan vastaavasti toinen li-elementti
const tokaElem = document.createElement('li');
tokaElem.innerHTML = 'Second item';

// luodaan vielä kolmas li-elementti
const kolmasElem = document.createElement('li');
kolmasElem.innerHTML = 'Third item';

// lisätään äsken luodut li-elementit target-elementin sisään
targetElem.appendChild(ekaElem);
targetElem.appendChild(tokaElem);
targetElem.appendChild(kolmasElem);

// etsitään toinen li-elementti
// - aluksi haetaan kaikki li-elementit
const liElementit = document.querySelectorAll('li');
// - etsitään listan toinen alkio
const listanTokaElem = liElementit[1];
// - lisätään toiselle li-elementille css luokkamääritys
listanTokaElem.classList.add('my-item');


