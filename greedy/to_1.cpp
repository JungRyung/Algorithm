#include <iostream>
#include <vector>

using namespace std;

int main(){
    int N, K;
    cin >> N;
    cin >> K;
    
    int cnt=0;
    while(N>1){
        if(N%K==0){
            N /= K;
            cnt++;
        }else{
            N--;
            cnt++;
        }
    }

    cout << cnt << endl;

    return 0;
}