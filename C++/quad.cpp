#include <iostream>
using namespace std;

int main()
{
    cout<<"Inserire dimensione lato quadrato: ";
    float l;
    cin>>l;

    float a = l * l;
    float p = l * 4;

    cout<<"Area: "<<a<<endl;
    cout<<"Perimetro: "<<p;

    return 0;
}