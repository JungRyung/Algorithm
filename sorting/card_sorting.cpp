#include <iostream>
#include <queue>
using namespace std;

int main(){
    int n;
    priority_queue<int, vector<int>, greater<int>> q;
    cin >> n;
    for(int i=0; i<n; i++){
        int tmp_card;
        cin >> tmp_card;
        q.push(tmp_card);
    }
    int answer = 0;
    while(q.size() > 1){
        int card1 = q.top();
        q.pop();
        int card2 = q.top();
        q.pop();
        int sum = card1 + card2;
        answer += sum;
        q.push(sum);
    }
    cout << answer << endl;
    return 0;
}