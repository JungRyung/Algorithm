#include <iostream>

using namespace std;

int recursive_factorial(int n){
    if(n==0)
        return 1;
    return n * recursive_factorial(n-1);
}

int main(){
    int n;
    cin >> n;
    int result = recursive_factorial(n);

    cout << result << endl;

    return 0;
}