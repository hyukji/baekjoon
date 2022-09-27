#include <iostream>
#include <string>
#include <sstream>


using namespace std;

string s ="1 2 3 4";

int main()
{
    int word;
    istringstream ss(s);
    ss >> word;
    
    int M = word;
    int m = word;
    
    while (ss >> word){
        if(word > M) M = word;
        else if(word < m) m = word;
    }
    
    
}
