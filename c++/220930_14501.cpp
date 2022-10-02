#include <iostream>
#include <vector>

using namespace std;


int main(){
    int n;
    cin >> n;
    int res[16];
    int t[16];
    int p[16];

    for(int i = 1; i <= n; i++){
        cin >> t[i];
        cin >> p[i];
    }
    
    int value = 0;
    for(int i = n; i > 0; i--){
        int end = i + t[i];
        if(end > n+1) {
            res[i] = res[i+1];
        }
        else{
            res[i] = max(res[i+1], res[end] + p[i]);
        }

    }
    
    cout << res[1];

    
}
