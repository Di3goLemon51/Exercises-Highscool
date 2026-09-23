let turnX = true;
let field = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
];

function clicked(el) {
    if (el.value === '' && !checkWin()) {
        let symbol = turnX ? 'X' : 'O';
        el.value = symbol;
        let pos = el.id.split(' ');
        field[pos[0]][pos[1]] = symbol;
        turnX = !turnX;
        console.log(field);
        checkWin();
    }
}

function checkWin() {
    for (let i = 0; i < 3; i++) {
        // Controlla Righe
        if (field[i][0] !== '' && field[i][0] === field[i][1] && field[i][0] === field[i][2]) {
            announceWinner(field[i][0]);
            return true;
        }

        // Controlla Colonne
        if (field[0][i] !== '' && field[0][i] === field[1][i] && field[0][i] === field[2][i]) {
            announceWinner(field[0][i]);
            return true;
        }
    }

    // Controlla Diagonali
    if (field[0][0] !== '' && field[0][0] === field[1][1] && field[0][0] === field[2][2]) {
        announceWinner(field[0][0]);
        return true;
    }

    if (field[0][2] !== '' && field[0][2] === field[1][1] && field[0][2] === field[2][0]) {
        announceWinner(field[0][2]);
        return true;
    }

    // Controlla Pareggio
    if (field.flat().every(cell => cell !== '')) {
        announceWinner('Tie');
        return true;
    }

    return false;
}

function announceWinner(winner) {
    alert(winner === 'Tie' ? 'Pareggio!' : `${winner} vince!`);
    resetBoard();
}

function resetBoard() {
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            field[i][j] = '';
            document.getElementById(`${i} ${j}`).value = '';
        }
    }
    turnX = true;
}
