#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    const float pi = 3.14;

    cout<<"Inserire dimensioni raggio del cerchio: ";

    float r;
    cin>>r;

    float a = pow(r,2) * pi; 
    float p = 2 * pi * r;

    cout<<"Area: "<<a<<endl;
    cout<<"Perimetro: "<<p;

    return 0;
}