#include <iostream>
using namespace std;
int main(){
    int n=10;
    int licz=0;
    for( int i = n ; i > 0; i -- ) {
        for (int j = 1; j < n ; j ++) {
            for (int k = 0; k < n ; k += 2 ) {
                licz++;
        }
    }
}
    cout<<licz;
    return 0;
}
//dla n=10 licz=450 --> 10*10*9/2
//n*n*(n-1)/2*c