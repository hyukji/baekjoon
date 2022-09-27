#include <iostream>
#include <vector>

using namespace std;

void fill_prime_arr(int n, bool* prime_arr);


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    bool* prime_arr = new bool[1000001];
    fill_prime_arr(1000001, prime_arr);

    int n;
    while(true){
        cin >> n;
        if(!n) break;

        bool flag = false;
        for(int i = 3; i <= n/2; i+=2){
            if(prime_arr[i] && prime_arr[n-i]){
                cout << n << " = " << i << " + " << n-i << "\n";
                flag = true;
                break;
            }
        }
        if(!flag) cout << "Goldbach's conjecture is wrong.";
        
    }

}


void fill_prime_arr(int n, bool* prime_arr){
    for(int i = 0; i < n; i++){
        prime_arr[i] = true;
    }

    for(int i = 2; i < n; i++){
        if(prime_arr[i]){
            for(int j = 2*i; j <= n; j+=i){
                prime_arr[j] = false;
            }
        }
    }
}