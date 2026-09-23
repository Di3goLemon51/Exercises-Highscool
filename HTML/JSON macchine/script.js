// loadJSON method to open the JSON file.
function loadJSON(path, success, error) {
    var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                success(JSON.parse(xhr.responseText));
            }
            else {
                error(xhr);
            }
        }
    };
    xhr.open('GET', path, true);
    xhr.send();
}

loadJSON("https://raw.githubusercontent.com/siimple/colors/develop/colors.json" /*sito da inserire */, myDataColori,'jsonp');
loadJSON("https://raw.githubusercontent.com/vega/vega/main/docs/data/cars.json" /*sito da inserire */, myDataMacchine,'jsonp');


function colori(JSONcolori) {
    let lista = [];
    for (let i = 0; i < 3; i++) {
        lista.push(JSONcolori[Math.floor(Math.random() * JSONcolori.length)]);
    };
    return lista;
}

function macchine(JSONmacchine) {
    let lista = [];
    for (let i = 0; i < 3; i++) {
        lista.push(JSONmacchine[Math.floor(Math.random() * JSONmacchine.length)]);
    };
    return lista;
}



function myDataColori(data) {
    
    // Carico liste
    lista = colori(data);

    for (let i = 0; i < 5; i++) {
        blocco = document.getElementById('blocco' + String(i+1));
        console.log(lista)
        blocco.style.background = lista[i].color;              // Colore Background
    };
}

function myDataMacchine(data) {
    
    // Carico liste
    lista = macchine(data);

    for (let i = 0; i < 3; i++) {
        titolo = document.getElementById('titolo' + String(i+1));
        titolo.innerHTML = lista[i].Name;
        info = document.getElementById('info' + String(i+1));
        info.innerHTML = "Miles per gallon: " + String(lista[i].Miles_per_Gallon) + "\n Cylinders: " + String(lista[i].Cylinders) + "\n Displacement: " + String(lista[i].Displacement) + "\n Horsepower: " + String(lista[i].Horsepower) + "\n Weight: " + String(lista[i].Weight_in_lbs) + "\n Acceleration: " + String(lista[i].Acceleration) + "\n Year: " + lista[i].Year + "\n Origin: " + lista[i].Origin;
    };
}
