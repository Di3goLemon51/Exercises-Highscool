
function wipe() {
    g1 = 0;
    g2 = 0;
    isg2 = false;
};

function gioca(mano) {
    if (!isg2) {
        g1 = mano
        console.log(g1)
    }
    else {
        g2 = mano
        console.log(g2)
    };
};

function ok(g) {
    switch (g1 && g2 && g) {
        case !0 && 0 && 1:
            isg2 = true;
            console.log('g1 selected', g1)
            break;

        case !0 && !0 && 2:
            console.log('g2 selected', g2)
            calculate();
            break;
    };
};

function calculate() {
    if (g1 == g2) {
        alert('Pareggio');
    }
    else {
        switch (g1 && g2) {
            case 1 && 2:    // sasso contro carta
                alert('G2 vince!');
                break;

            case 1 && 3:    // sasso contro forbice
                alert('G1 vince!');
                break;

            case 2 && 1:    // carta contro sasso
                alert('G1 vince!');
                break;

            case 2 && 3:    // carta contro forbice
                alert('G2 vince!');
                break;

            case 3 && 1:    // forbice contro sasso
                alert('G2 vince!');
                break;

            case 3 && 2:    // forbice contro carta
                alert('G1 vince!');
                break;
        };
    };
    wipe()
    console.log(g1, g2, isg2)
};