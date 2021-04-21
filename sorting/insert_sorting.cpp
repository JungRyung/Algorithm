#include <iostream>
#define MAXLEN 10

using namespace std;

void insert_sort(int* arr){
    for(int i=1; i<MAXLEN; i++){
        for(int j=i; j>0; j--){
            if(arr[j]<arr[j-1]){
                int tmp = arr[j];
                arr[j] = arr[j-1];
                arr[j-1] = tmp;
            }else
                break;
        }
    }
}

int main(){
    int arr[MAXLEN] = {7,5,9,0,3,1,6,2,4,8};
    
    insert_sort(arr);

    for(int i=0; i<MAXLEN; i++){
        cout << arr[i] << " ";
    }
    cout << endl;
    
    return 0;
}