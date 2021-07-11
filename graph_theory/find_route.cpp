/*
TITLE   : 경로 찾기
URL     : https://www.acmicpc.net/problem/11403
DATE    : 21.07.11
*/
#include <iostream>

using namespace std;

int main(){
    int n;
    cin >> n;
    int graph[n][n] = {0};
    
    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
            cin >> graph[i][j];

    // 플로이드 워셜
    for(int k=0; k<n; k++)
        for(int i=0; i<n; i++)
            for(int j=0; j<n; j++)
                if(graph[i][k]==1 and graph[k][j]==1)
                    graph[i][j] = 1;
    
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cout << graph[i][j] << ' ';
        }
        cout << endl;
    }

    return 0;
}