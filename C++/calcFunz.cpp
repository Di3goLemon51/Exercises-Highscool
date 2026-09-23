#include <iostream>
using namespace std;

int addizione(int a, float b)
{
	int ris = a + b;
	return ris;
}

int moltiplicazione(int a, float b)
{
	int ris = a * b;
	return ris;
}

int sottrazione(int a, float b)
{
    int ris = a - b;
    return ris;
}

float divisione(int a, float b)
{
    if (b != 0) {
        float ris = a / b;
        return ris;
    } else {
        cout<<"Impossibile dividere per 0"<<endl;
        return 0;
    }
    
}

int main()
{
	cout<<"Primo numero: "<<endl;
    int a;
    cin>>a;
    
    cout<<"Operatore: "<<endl;
    char op;
    cin>>op;
    
    cout<<"Secondo numero: "<<endl;
    int b;
    cin>>b;

    switch (op) {
        case '+':
            addizione(a, b);
            break;
            
        case '-':
            sottrazione(a, b);
            break;
            
        case '*':
            moltiplicazione(a, b);
            break;
            
        case '/':
            divisione(a, b);
            break;
            
        default:
            cout<<"Errore"<<endl;
            break;
    }

	return 0;
}