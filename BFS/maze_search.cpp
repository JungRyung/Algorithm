/*
Title   : 미로 탐색
URL     : https://www.acmicpc.net/problem/2178
Date    : 21.07.10
*/
#include <iostream>
#include <string.h>
#include <queue>
#include <tuple>

using namespace std;


int main(){
    int dx[] = {-1,0,1,0};
    int dy[] = {0,-1,0,1};

    int n, m;
    cin >> n >> m;
    int **maze = new int*[n];
    int **visit = new int*[n];
    for(int i=0; i<n; i++){
        maze[i] = new int[m];
        visit[i] = new int[m];
        memset(maze[i],0,sizeof(int)*m);
        memset(visit[i],0,sizeof(int)*m);
        string tmp;
        cin >> tmp;
        for(int j=0; j<m; j++){
            maze[i][j] = tmp[j]-48;
        }
    }
    queue<tuple<int,int,int>> q;
    visit[0][0] = 1;
    q.push(make_tuple(0,0,1));
    while(!q.empty()){
        int x = get<0>(q.front());
        int y = get<1>(q.front());
        int t = get<2>(q.front());
        q.pop();
        if(x==n-1 && y==m-1){
            cout << t << endl;
            break;
        }
        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(0<=nx && nx<n && 0<=ny && ny<m && maze[nx][ny] == 1 && visit[nx][ny]==0){
                q.push(make_tuple(nx,ny,t+1));
                visit[nx][ny] = 1;
            }
        }
    }

    return 0;
}