#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int N, M, K;
    vector<int> num;
    int result=0;
    
    cin >> N;
    cin >> M;
    cin >> K;

    int tmp;
    for(int i=0; i<N; i++){
        cin >> tmp;
        num.push_back(tmp);
    }

    sort(num.begin(), num.end(), greater<int>());
    
    int cnt=0;
    for(int i=0; i<M; i++){
        if(cnt<K){
            result += num[0];
            cnt++;
        }else{
            cnt=0;
            result += num[1];
        }
    }

    cout << result << endl;
    
    return 0;
}