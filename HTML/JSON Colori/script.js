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

loadJSON("https://raw.githubusercontent.com/cheprasov/json-colors/master/colors.json" /*sito da inserire */, myData,'jsonp');

function colori(JSONcolori) {
    let lista = [];
    for (let i = 0; i < 5; i++) {
        lista.push(JSONcolori[Math.floor(Math.random() * JSONcolori.length)]);
    };
    return lista;
}


function myData(data) {
    
    // Carico colori
    lista = colori(data);

    for (let i = 0; i < 5; i++) {
        divColore = document.getElementById('colore' + String(i+1));
        divColore.style.background = lista[i].hex;              // Colore Background
        nome = document.getElementById('nome' + String(i+1));
        nome.innerHTML = lista[i].name;                         // Nome Colore
        codice = document.getElementById('codice' + String(i+1))
        codice.innerHTML = lista[i].hex;                        // Codice Colore
    };
}