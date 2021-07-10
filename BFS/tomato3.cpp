/*
Title   : 토마토
URL     : https://www.acmicpc.net/problem/7576
date    : 21.07.10
*/
#include <iostream>
#include <queue>
#include <utility>
#include <vector>
#define MAX_LEN 1001

using namespace std;

struct tomato
{  
    int x,y;
};

int dx[] = {-1,0,1,0};
int dy[] = {0,-1,0,1};
int box[MAX_LEN][MAX_LEN] = {0};
int n, m;
queue<tomato> q;

bool in_range(int x, int y){
    if(x>=0 && x<n && y>=0 && y<m)
        return true;
    else
        return false;
}

void dfs(){
    while(!q.empty()){
        int x = q.front().x;
        int y = q.front().y;
        q.pop();
        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(in_range(nx,ny) && box[nx][ny]==0){
                box[nx][ny] = box[x][y] + 1;
                q.push({nx,ny});
            }
        }
    }
}

int main(){
    cin >> m >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cin >> box[i][j];
            if(box[i][j]==1)
                q.push({i,j});
        }
    }
    dfs();
    int max_day = 0;
    bool possible = true;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if(box[i][j]==0)
                possible = false;
            if(max_day<box[i][j])
                max_day = box[i][j];
        }
    }
    if(possible)
        cout << max_day-1 << endl;
    else
        cout << "-1" << endl;
    
    return 0;
}