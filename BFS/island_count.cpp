/*
Title   : 섬의 개수
URL     : https://www.acmicpc.net/problem/4963
date    : 21.07.10
*/
#include <iostream>
#include <queue>
#include <string.h>
#define MAX_LEN 50

using namespace std;

int dx[8] = {-1,-1,-1,0,0,1,1,1};
int dy[8] = {-1,0,1,-1,1,-1,0,1};
int map[MAX_LEN][MAX_LEN] = {0}; 
bool visit[MAX_LEN][MAX_LEN] = {false};

struct island{
    int x,y;
};

bool in_range(int x, int y, int h, int w){
    if(x>=0 && x<h && y>=0 && y<w)
        return true;
    else
        return false;
}

int main(){
    int w, h;
    while(true){
        queue<island> q;
        cin >> w >> h;
        if(w==0 and h==0)
            break;
        
        for(int i=0; i<h; i++){
            for(int j=0; j<w; j++){
                cin >> map[i][j];
                cout << map[i][j] << ' ';
            }
            cout << endl;
        }
        int island_cnt = 0;
        for(int i=0; i<h; i++){
            for(int j=0; j<w; j++){
                if(map[i][j]==1 && !visit[i][j]){
                    island_cnt++;
                    visit[i][j] = true;
                    q.push({i,j});
                    while(!q.empty()){
                        int x = q.front().x;
                        int y = q.front().y;
                        q.pop();
                        for(int k=0; k<8; k++){
                            int nx = x + dx[k];
                            int ny = y + dy[k];
                            if(in_range(nx,ny,h,w) && !visit[nx][ny] && map[nx][ny]==1){
                                visit[nx][ny] = true;
                                q.push({nx,ny});
                            }
                        }
                    }
                }
            }
        }
        cout << island_cnt << endl;
        memset(map,0,sizeof(map));
        memset(visit,false,sizeof(visit));
    }
    return 0;
}