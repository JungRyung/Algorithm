#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
    int N;
    cin >> N;

    int cnt=0;
    for(int i=0; i<=N; i++){
        for(int j=0; j<60; j++){
            for(int k=0; k<60; k++){
                string tmp = to_string(i) + to_string(j) + to_string(k);
                if(string::npos != tmp.find('3'))
                    cnt++;
            }
        }
    }

    cout << cnt << endl;

    return 0;
}