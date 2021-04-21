#include <iostream>
#include <vector>

using namespace std;

int main(){
    int N, M;
    cin >> N;
    cin >> M;

    int max_num = 0;
    for(int i=0; i<N; i++){
        int min_num = 10001;
        for(int j=0; j<M; j++){
            int tmp_num;
            cin >> tmp_num;
            if(tmp_num < min_num)
                min_num = tmp_num;
        }
        if(min_num > max_num)
            max_num = min_num;
    }

    cout << max_num << endl;

    return 0;
}