/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
using namespace std;

int main()
{
    cout<<"Definire numeratore 1, operazione e numeratore 2."<<endl;
    int a;
    char o;
    float b;
    cout<<"Numeratore 1: ";
    cin>>a;
    cout<<"Operatore (+ - * /): ";
    cin>>o;
    cout<<"Numeratore 2: ";
    cin>>b;
    
    float ris;
    
    switch (o) {
        case '+':
        ris = a + b;
        break;
        
        case '-':
        ris = a - b;
        break;
        
        case '*':
        ris = a * b;
        break;
        
        case '/':
        ris = a / b;
        break;
    }
    
  /*  else {
        cout<<"Operatore non valido!";
        return 0;
    }*/

    cout<<endl<<"Risultato: "<<ris;
    return 0;
}