'use strict';

// etsitään form-elementti html-sivulta,
// huom: jouduin lisäämään html-sivulle id arvon sen form-tagille
const tvForm = document.querySelector('#tv');

tvForm.addEventListener('submit', async function (evt) {
  // estetään oletustoiminta eli action-komennon suoritus
  evt.preventDefault();

  // luetaan lomakkeen syöttökentästä sinne syötetty hakusana
  const query = document.querySelector('input[name=q]').value;

  // muodostetaan hakukysely
  const hakuKysely = `https://api.tvmaze.com/search/shows?q=${query}`;
  // tulostetaan nettiin lähetettävä hakukysely ainakin debuggausvaiheessa
  console.log("-- Hakukysely: " + hakuKysely);

  try {
    // error handling: try/catch/finally

    // fetch palauttaa ns. raakadatan netistä (response-tyyppinä)
    const response = await fetch(
      hakuKysely
    );

    // muunnetaan raakadata json-dataksi
    const jsonData = await response.json();

    // kutsutaan omaa funktiota, joka hoitaa tulosten käsittelyn
    kasitteData(jsonData);

  } catch (error) {
    console.log(error.message);
  }
});



function kasitteData(jsonData) {
    // tulostus menee nyt konsoliin
    console.log(jsonData);
}
