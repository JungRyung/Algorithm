#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int N, M, K;
    vector<int> num;
    int result=0;
    
    // N, M, K를 입력받기
    cin >> N;
    cin >> M;
    cin >> K;

    // N개의 수를 입력받기
    int tmp;
    for(int i=0; i<N; i++){
        cin >> tmp;
        num.push_back(tmp);
    }

    // 입력받은 수를 정렬하기
    sort(num.begin(), num.end(), greater<int>());
    int first = num[0];
    int second = num[1];
    
    // 가장 큰 수가 더해지는 횟수 계산
    int count = int(M / (K + 1)) * K;
    count += M % (K + 1);

    result += (count) * first;    // 가장 큰 수 더하기
    result += (M - count) * second;  // 두 번째로 큰 수 더하기

    cout << result << endl;

    return 0;
}