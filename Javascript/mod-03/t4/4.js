'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

// etsitään tulostuksen paikka html-sivulta
const targetElement = document.querySelector('#target');
// or const targetElement = document.getElementById('target');

// käydään kaikki students-taulukon alkiot läpi yksitellen.
// html-sivulle-tulee nyt option-tageja, joita käytetään esim. valikoissa.
// huomaa: html-sivulla ei näy opiskelijan id-arvo, vain nimi.
for (let student of students) {
  const item = document.createElement('option');
  item.innerHTML = student.name;
  item.value = student.id;
  targetElement.appendChild(item);
}
