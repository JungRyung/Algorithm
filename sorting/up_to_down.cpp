#include <iostream>
#include <algorithm>

using namespace std;

bool compare(int a, int b){
    return a > b;
}

int main(){
    int N;
    cin >> N;

    int arr[N];

    for(int i=0; i<N; i++){
        cin >> arr[i];
    }

    sort(arr,arr+N,compare);

    for(int i=0; i<N; i++){
        cout << arr[i] << " ";
    }    
    cout << endl;
    return 0;
}