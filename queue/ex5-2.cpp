#include <iostream>
#include <queue>

using namespace std;

void print_queue(queue<int> q){
    while(q.size()){
        cout << q.front() << " ";
        q.pop();
    }
    cout << endl;
}

int main(){
    queue<int> q;

    q.push(5);
    q.push(2);
    q.push(3);
    q.push(7);
    q.pop();
    q.push(1);
    q.push(4);
    q.pop();

    print_queue(q);
    
    return 0;
}