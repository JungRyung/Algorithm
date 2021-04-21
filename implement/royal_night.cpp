#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int main(){
    string site;
    cin >> site;

    map<char,int> m;

    m['a']=1;
    m['b']=2;
    m['c']=3;
    m['d']=4;
    m['e']=5;
    m['f']=6;
    m['g']=7;
    m['h']=8;


    int i = site[1] - '0';
    int j = m.find(site[0])->second;
    int cnt=0;

    // (i-1, j-2)
    // (i+1, j-2)
    
    // (i-2, j-1)
    // (i-2, j+1)

    // (i-1, j+2)
    // (i+1, j+2)

    // (i+2, j-1)
    // (i+2, j+1)

    if(0<i-1 && i-1<9 && 0<j-2 && j-2<9)
        cnt++;
    if(0<i+1 && i+1<9 && 0<j-2 && j-2<9)
        cnt++;
    if(0<i-2 && i-2<9 && 0<j-1 && j-1<9)
        cnt++;
    if(0<i-2 && i-2<9 && 0<j+1 && j+1<9)
        cnt++;
    if(0<i-1 && i-1<9 && 0<j+2 && j+2<9)
        cnt++;
    if(0<i+1 && i+1<9 && 0<j+2 && j+2<9)
        cnt++;
    if(0<i+2 && i+2<9 && 0<j-1 && j-1<9)
        cnt++;
    if(0<i+2 && i+2<9 && 0<j+1 && j+1<9)
        cnt++;

    cout << cnt << endl;

    return 0;
}