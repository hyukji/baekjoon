#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n;
    cin >> n;

    vector<long> v;
    v.push_back(0);
    v.push_back(1);
    v.push_back(1);
    if(n > 2){
        for(int i=3; i <= n; i++){
            v.push_back((v[i-1] + v[i-2]));
        }
    }
    cout << v[n];
}