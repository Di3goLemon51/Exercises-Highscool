data = {
    "studenti":[
        {
            "nome": "Diego",
            "cognome": "Doria",
            "sesso": "M"
        },
        {
            "nome": "Tommaso", 
            "cognome": "Ballico",
            "sesso": "M"
    },
        {
            "nome": "Francesco", 
            "cognome": "Mariutto",
            "sesso": "M"
    }
    ], 
    
    "docenti":[
        {
            "nome": "Kevin", 
            "cognome": "Gemolo",
            "sesso": "M"
        },
        {
            "nome": "Valentina Maria", 
            "cognome": "Pilloni",
            "sesso": "F"
        },
        {
            "nome": "Alberto", 
            "cognome": "Signoretti",
            "sesso": "M"
        }
    ]
};

function readJSON() {
    parsedData = JSON.parse(JSON.stringify(data));
};
readJSON()


// Creazione lista Docenti
let listaDoc = document.getElementById("Docenti");
let ulDoc = document.createElement('ul');                 // creo la lista
for(let i = 0; i < data.docenti.length; i++) {
    let li = document.createElement('li');                // creo elemento lista
    
    switch (data.docenti[i].sesso) {                      // modifico elemento lista
        case 'M':
            li.innerHTML = 'Prof. ' + data.docenti[i].nome + ' ' + data.docenti[i].cognome;
            break;
        case 'F':
            li.innerHTML = 'Professoressa ' + data.docenti[i].nome + ' ' + data.docenti[i].cognome;
            break;
    };
    
    ulDoc.appendChild(li);                                 // aggiungo elemento alla lista
}
listaDoc.appendChild(ulDoc);                               // aggiungo la lista al div


// Creazione lista Studenti
let listaStu = document.getElementById("Studenti");
let ulStu = document.createElement('ul');                  // creo la lista
for(let i = 0; i < data.studenti.length; i++) {
    let li = document.createElement('li');                 // creo elemento lista
    
    switch (data.studenti[i].sesso) {                      // modifico elemento lista
        case 'M':
            li.innerHTML = 'Studente ' + data.studenti[i].nome + ' ' + data.studenti[i].cognome;
            break;
        case 'F':
            li.innerHTML = 'Studentessa ' + data.studenti[i].nome + ' ' + data.studenti[i].cognome;
            break;
    };
    
    ulStu.appendChild(li);                                 // aggiungo elemento alla lista
}
listaStu.appendChild(ulStu);                               // aggiungo la lista al div