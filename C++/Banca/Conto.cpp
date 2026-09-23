#include <iostream>
#include <string>
using namespace std;

class ContoBancario
{
private:
    // inizializzo argomenti della classe
    string nome;
    double saldo;

public:
    // costruttore
    ContoBancario(string nomeCliente, double saldoIniziale) {
        nome = nomeCliente;
        saldo = saldoIniziale; 
    }
    
    // funzione info
    void info() {
        cout<<"Nome proprietario: "<<nome<<endl;
        cout<<"Saldo attuale: € "<<saldo<<endl;
    }

    // funzione deposito
    void deposito(double importo) {
        saldo += importo;
        cout<<"Deposito avvenuto con successo."<<endl;
        cout<<"Saldo attuale: € "<<saldo<<endl;
    }

    // funzione prelievo
    void prelievo(double importo) {
        if (saldo >= importo) {
            saldo -= importo;
            cout<<"Prelievo avvenuto con successo."<<endl;
            cout<<"Saldo attuale: € "<<saldo<<endl;
        } else {
            cout<<"Saldo insufficiente."<<endl;
        }
        
    }

    // get saldo
    void getSaldo() {
        return saldo;
    }
};