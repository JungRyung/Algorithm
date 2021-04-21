#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int main(){
    string site;
    cin >> site;

    map<string,int> m;
    m.insert(make_pair("a",1));
    m.insert(make_pair("b",2));
    m.insert(make_pair("c",3));
    m.insert(make_pair("d",4));
    m.insert(make_pair("e",5));
    m.insert(make_pair("f",6));
    m.insert(make_pair("g",7));
    m.insert(make_pair("h",8));

    int i = std::stoi(site[1]);
    int j = m.find(site[0]);

    cout << "(" << i << "," << j << ")" << endl;
    

    return 0;
}