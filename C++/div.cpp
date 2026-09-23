#include <iostream>
using namespace std;

int divisori(int num) { // trova i divisori
    int div = 0;
        for (int i = 1; i <= num; i++) {    //cerco il divisore
            if (num % i == 0) {             // controllo se è divisore    
                div++;
            }
        }
        return div;
}

void get(int num, int div) { // printa i risultati
    cout<<num<<" ha "<<div<<" divisori"<<endl;
}

int main() { 
    
    cout<<"Numero di cui si vuole sapere il num di divisori: "<<endl;
    int num;
    cin>>num;

    int div = divisori(num); //passaggio per valore
    
    get(num, div);

    return 0;
}