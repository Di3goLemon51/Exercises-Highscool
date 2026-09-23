#include <iostream>
using namespace std;

void raggio(float &r)
{
    cout<<"Valore del raggio: ";
    cin>>r;
}

void area(float r, float &a)
{
    a = r*r*3.14;
}

void circ(float r, float &c)
{
    c = 2*r*3.14;
}

int main()
{
    float r;
    float a;
    float c;
    
    raggio(r);
    area(r, a);
    circ(r, c);
    
    cout<<"Area: "<<a<<endl;
    cout<<"Circonferenza: "<<c<<endl;
    return 0;
}