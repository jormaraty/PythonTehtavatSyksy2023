'use strict';

// etsitään syöttölomake html-sivulta
const formElem = document.querySelector('#norris');

// etsitään lomakkeen hakukenttä
const hakuElem = document.querySelector('input[name=q]');

// etsitään tulostuksen paikka html-sivulta
const resultsElem = document.querySelector('#results');

// nettiin lähetettävän hakukyselyn vakio-osa
let hakuLause = "https://api.chucknorris.io/jokes/search?query=";


// määritellään syöttölomakkeelle sen tapahtumankäsittelijä
formElem.addEventListener('submit', async function(evt) {
    // estetään lomakkeen vakiotoiminto
    evt.preventDefault();

    // luetaan tarvittavien syöttökenttien arvot
    const hakuArvo = hakuElem.value;

    // muodostetaan lopullinen nettiin lähetettävä kysely
    hakuLause += hakuArvo;
    console.log("-- nettiin lähtee: " + hakuLause);

    // kutsutaan funktiota, joka tekee varsinaisen nettihaun
    haeData(hakuLause);

});


async function haeData(nettikysely) {
    // error handling: try/catch/finally
    try {

    // fetch palauttaa ns. raakadatan netistä (response-tyyppinä)
    const response = await fetch(nettikysely);

    // muutetaan raakadata json-dataksi
    const jsonData = await response.json();

    // kutsutaan omaa funktiota, joka hoitaa tulosten käsittelyn
    kasitteData(jsonData);

    } catch (error) {
        console.log(error.message);
    }
}


function kasitteData(jsonData) {
    /*
        kun laitetaan hakulause selaimeen, niin nähdään että nyt vitsit
        ovat listassa avaimen 'result' arvona
     */

    for (let vitsi of jsonData.result) {
        let htmlkoodi =
            `<article>
                <p>${vitsi.value}<p>
             </article>`;

        // lisätään vitsi html-sivulle entisten perään
        resultsElem.innerHTML += htmlkoodi;
    }

}
