#include <iostream>
using namespace std;

int main()
{
    cout<<"Inserire dimensione lato quadrato: ";
    int l;
    cin>>l;

    for (int c = 1; c <= l; c++) { // per le colonne
        for (int r = 1; r <= l; r++) { // per le righe
            cout<<'*';
        }
        cout<<endl; //vado a capo
    }

    return 0;
}