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

loadJSON("https://gist.githubusercontent.com/stockmind/8bcbbf9ac41bc196401b96084ec8c5d3/raw/2edda5cd32eb2b99d3d9b45413bc8b1135564260/province-italia.json" /*sito da inserire */, myData,'jsonp');

function myData(data){

    // Creazione lista Provicie
    let lista = document.getElementById("Provicie");
    let ul = document.createElement('ul');                      // creo la lista
    data.forEach(el => {
        
      // span per la sigla
      let sigla = document.createElement('span');
      sigla.innerHTML = el.sigla;
      sigla.classList.add('spanSigla');
      
      // span per la regione
      let regione = document.createElement('span');
      regione.innerHTML = el.regione;
      regione.classList.add('spanRegione');
      
      // span per il nome
      let nome = document.createElement('span');
      nome.innerHTML = el.nome;
      nome.classList.add('spanNome');

      let divSopra = document.createElement('div');
      divSopra.appendChild(sigla);
      divSopra.appendChild(regione);

      let divSotto = document.createElement('div');
      divSotto.appendChild(nome);

      let li = document.createElement('li');
      li.appendChild(divSopra);
      li.appendChild(divSotto);
        
      ul.appendChild(li);
    });
    lista.appendChild(ul);
}
