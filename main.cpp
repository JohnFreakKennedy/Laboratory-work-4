#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

int main()
{
    long long f=1,n;
    double d=1,x,a;
    cout<<"Dankov Artem,IS-01,10V"<<endl;
    cout<<"Put number x: "<<endl;
    cin>>x;
    cout<<"Put number n: "<<endl;
    cin>>n;
    for(int i=2;i<=2*n;i+=2)
    {
        d*=x;
        f*= i*(i-1);
        a = d/f;
        cout<<fixed<<setprecision(4)<<a<<" ";
    }
    return 0;
}
