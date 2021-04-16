// Oct 4th '20
// Finding primes and prime factors in a range 
#include <iostream>
#include <cstring>
using namespace std;

bool findIfPrime(int n){
    bool prime[n+1];
    bool isPrime = false;
    memset(prime, true, sizeof(prime));
    
    for (int p = 2;  p*p <= n; p++)
    {
        if(prime[p]){
            for (int k = p*p; k<= n; k+=p)
            {
                prime[k] = false;
            }
        }
    }
 cout << "All prime numbers till " << n << endl;
    for (int p=2; p<=n; p++){   
       if (prime[p]){ 
          
          cout << p << " ";
          isPrime = true;
          } 
    }
    cout << endl;
    return isPrime;
}

int main(){
    int k;
    cin >> k;

    if(findIfPrime(k)){
        cout << k << " is prime."  << endl;
    }else{
        cout << k << " is not prime."  << endl;
    }
    return 0;
}