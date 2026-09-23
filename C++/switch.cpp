#include <iostream>
using namespace std;

int main()
{
    int a = 10;
    int b = 20;
    int c = 30;
    int d;
    
    d = a;
    a = c;
    c = b;
    b = d;
    
    cout<<"a: "<<a<<", b: "<<b<<", c: "<<c;

	return 0;
}