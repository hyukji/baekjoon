#include <iostream>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int cnt,a,b;
    cin >> cnt;
    for(int i = 0; i < cnt; i++){
        cin >> a >> b;
        cout << a + b << "\n";
    }
}



/*
https://st-lab.tistory.com/232

    cin.tie(NULL); => 입력과 출력 분리 즉 입력에 따라 출력이 바로 아니고 입력 다 받고나서 출력나오게

    ios_base::sync_with_stdio(false) => c형식의 입출력이랑 동기화 되도록. but 우리는 c++표준입력 cin, cout만 쓸거여서 false로

    endl vs \n => endl은 개행줄 만이 아니라 출력버퍼를 비우는 역할까지 한ㄷ.
*/
