/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
using namespace std;

int main()
{
    cout<<"Definire numeratore 1 e numeratore 2."<<endl;
    int a;
    int b;
   
    cout<<"Numeratore 1: ";
    cin>>a;

    cout<<"Numeratore 2: ";
    cin>>b;
    
    int add = a + b;
    int sot = a - b;
    int mol = a * b;
    float divi = (float) a / b;
  

    cout<<endl<<"Addizione: "<<add;
    cout<<endl<<"Sottrazione: "<<sot;
    cout<<endl<<"Moltiplicazione: "<<mol;
    cout<<endl<<"Divisione: "<<divi;
    return 0;
}