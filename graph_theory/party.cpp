/*
TITLE   : 파티
URL     : https://www.acmicpc.net/problem/1238
DATE    : 21.07.11
*/
#include <iostream>
#include <algorithm>
#define MAX_TIME 101

using namespace std;

int main(){
    int n, m, x;
    cin >> n >> m >> x;

    int graph[n+1][n+1] = {0};

    for(int i=1; i<n+1; i++){
        for(int j=1; j<n+1; j++){
            if(i==j)
                graph[i][j] = 0;
            else
                graph[i][j] = MAX_TIME;
        }
    }

    for(int i=0; i<m; i++){
        int t,a,b;
        cin >> a >> b >> t;
        graph[a][b] = t;
    }
    
    // 플로이드 워셜
    for(int k=1; k<n+1; k++)
        for(int i=1; i<n+1; i++)
            for(int j=1; j<n+1; j++)
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j]);

    int max_sum = -1;
    for(int i=1; i<n+1; i++){
        max_sum = max(max_sum, graph[i][x] + graph[x][i]);
    }
    cout << max_sum << endl;

    return 0;
}