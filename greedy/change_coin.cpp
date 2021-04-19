#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n = 1260;   // 거슬러 줘야 할 돈
    int count = 0;

    //큰 단위의 화폐부터 차례대로 확인
    vector<int> coin_types;
    coin_types.push_back(500);
    coin_types.push_back(100);
    coin_types.push_back(50);
    coin_types.push_back(10);
    
    for(int i=0; i<coin_types.size(); i++){
        count += n / coin_types[i];
        n %= coin_types[i];
    }

    cout << count << endl;

    return 0;
}