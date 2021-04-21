#include <iostream>

using namespace std;

void recursive_fuction(int i){
    if(i==100)
        return;
    cout << i << "번째 재귀 함수에서 " << i+1 << "번째 재귀 함수를 호출합니다." << endl;
    recursive_fuction(i+1);
    cout << i << "번째 재귀 함수를 종료합니다." << endl;
}
int main(){
    recursive_fuction(1);

    return 0;
}