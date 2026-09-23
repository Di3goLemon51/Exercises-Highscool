#include <iostream>
using namespace std;

int main()
{
	int a,b;

	cout<<"Scrivi numero 1 e 2: ";

	cin>>a;
	cin>>b;

	a = a+b;

	cout<<"Inserisci terzo numero: ";

	cin>>b;

	a = a+b;

	cout<<"Somma: "<<a;

	return 0;
}