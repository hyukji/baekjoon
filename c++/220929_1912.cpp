#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n;
    cin >> n;

    vector<int> v(n);
    for(int i =0; i < n; i++){
        cin >> v[i];
    }

    int res = v[0];
    int M = v[0];
    for(int i = 1; i < n; i++){
        M = max(M + v[i], v[i]);
        if(res < M) res = M;
    }

    cout << res;
}
