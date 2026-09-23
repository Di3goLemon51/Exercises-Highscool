/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
using namespace std;



float raggio()
{
    cout<<"Valore del raggio: ";
    float r;
    cin>>r;
    return r;
}

float area(float r)
{
    float a = r*r*3.14;
    return a;
}

float circ(float r)
{
    float c = 2*r*3.14;
    return c;
}

int main()
{
    float r;
    r = raggio();
    
    float a;
    a = area(r);
    cout<<"Area: "<<a<<endl;
    
    float c;
    c = circ(r);
    cout<<"Circonferenza: "<<c<<endl;
    return 0;
}