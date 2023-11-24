'use strict';

// html-sivulta ei tarvita nyt mitään tietoja

// nettiin lähetettävä kysely
const hakuKysely = "https://api.chucknorris.io/jokes/random";

// tehdään haku netistä (kauneuspilkku: ei oteta talteen
// asynkronisen haeData-funktion palauttamaa Promise-oliota)
haeData();

async function haeData() {
    try {
    // error handling: try/catch/finally

    // fetch palauttaa ns. raakadatan netistä (response-tyyppinä)
    const response = await fetch(hakuKysely);

    // muunnetaan raakadata json-dataksi
    const jsonData = await response.json();

    // kutsutaan omaa funktiota, joka hoitaa tulosten käsittelyn
    kasitteData(jsonData);

    } catch (error) {
        console.log(error.message);
    }
}

function kasitteData(jsonData) {
    console.log(jsonData.value);
}
