let numeroUno = 0;
let numeroDue = 0;
let op = '';
let isNumeroDue = false;
let isInt = true;
let virg = 0.1;

function load(){
    document.getElementById('display').value = 0;
};

function n(el){
    if(!isNumeroDue){
        if(isInt){
            numeroUno = numeroUno * 10;
            numeroUno = numeroUno + parseInt(el.value);
        } else{
            numeroUno = numeroUno + parseInt(el.value) * virg;
            virg = virg / 10;
        };

        document.getElementById('display').value = numeroUno;
        console.log(numeroUno);

    } else{
        if(isInt){
            numeroDue = numeroDue * 10;
            numeroDue = numeroDue + parseInt(el.value);
        } else{
            numeroDue = numeroDue + parseInt(el.value) * virg;
            virg = virg / 10;
        };

        document.getElementById('display').value = numeroDue;
        console.log(numeroDue);
    };
};

function operazione(el){
    if(el.value == '='){
        if(op == '+'){
            numeroUno = numeroUno + numeroDue;
        };
        if(op == '-'){
            numeroUno = numeroUno - numeroDue;
        };
        if(op == '*'){
            numeroUno = numeroUno * numeroDue;
        };
        if(op == '/'){
            numeroUno = numeroUno / numeroDue;
        };

        console.log(el.value);
        document.getElementById('display').value = numeroUno;
        console.log(numeroUno);
        console.log('--');
        numeroDue = 0;
        isNumeroDue = false;

    } else if(el.value == '.'){
        isInt = false

    }else{
        op = el.value;
        isNumeroDue = true;
        isInt = true
        virg = 0.1
        console.log(el.value);
    };
};

function cancel(){
    numeroUno = 0;
    numeroDue = 0;
    op = '';
    isNumeroDue = false;
    isInt = true
    virg = 0.1

    document.getElementById('display').value = 0;
};

function del(){

    if(!isNumeroDue){
        // let ultimaCifra = 0
        // ultimaCifra = Number.isInteger(numeroUno) ? numeroUno % 10 : numeroUno.toString().slice(-1);
        numeroUno = numeroUno.toString().split('').slice(0, -1).join('');
        document.getElementById('display').value = numeroUno;
    } else{
        numeroDue = parseInt(numeroDue / 10);
        document.getElementById('display').value = numeroDue;
    };
};