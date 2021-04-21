#include <iostream>
#include <stack>

using namespace std;

void print_stack(stack<int> stack){
    while(stack.size()){
        cout << stack.top() << " ";
        stack.pop();
    }
    cout << endl;
}

int main(){
    stack<int> s;

    s.push(5);
    s.push(2);
    s.push(3);
    s.push(7);
    s.pop();
    s.push(1);
    s.push(4);
    s.pop();

    print_stack(s);
    
    return 0;
}