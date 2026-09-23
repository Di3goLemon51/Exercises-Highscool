#include <iostream>
using namespace std;

int main()
{
    float capo1;
    float capo2;
    float capo3;
    cout<<"Inserisci il prezzo dei tre capi:"<<endl;
    cin>>capo1;
    cin>>capo2;
    cin>>capo3;
    
    cout<<"Inserire la percentuale di IVA:"<<endl;
    int iva;
    cin>>iva;
    
    float tot = (capo1 + capo2 + capo3) + (capo1 + capo2 +capo3) * iva / 100;
    cout<<"Il totale con IVA è di "<<tot<<" €";

    return 0;
}