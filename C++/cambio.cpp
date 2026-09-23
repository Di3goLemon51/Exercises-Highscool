#include <iostream>
using namespace std;

float tasso;    // variabile globale

float info() {
    cout<<"Inserire tasso di cambio: "<<endl;
    cin>>tasso;

    cout<<"Inserire valore valuta locale: "<<endl;
    float locale;
    cin>>locale;

    return locale;
}

float cambio(float locale) { // eseguo il cambio di valuta
    float estera = locale * tasso;
    return estera;
}

void get(float locale, float estera) {
    cout<<locale<<" in valuta locale con tasso di cambio pari a "<<tasso<<" corrisponde in valuta estera a "<<estera<<endl;
}

int main() {
    float locale = info();

    float estera = cambio(locale);
    get(locale, estera);

    return 0;
}