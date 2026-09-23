/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
using namespace std;

float r;
float a;
float c;

void raggio()
{
    cout<<"Valore del raggio: ";
    cin>>r;
}

void area()
{
    a = r*r*3.14;

}

void circ()
{
    c = 2*r*3.14;
}

int main()
{
    raggio();
    area();
    circ();
    
    cout<<"Area: "<<a<<endl;
    cout<<"Circonferenza: "<<c<<endl;
    return 0;
}