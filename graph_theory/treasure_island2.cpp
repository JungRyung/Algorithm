/*
TITLE   : 보물섬
URL     : https://www.acmicpc.net/problem/2589
DATE    : 21.07.12
*/
#include <iostream>
#include <queue>
#include <tuple>
#define MAX_LEN 50

using namespace std;

int dx[4] = {-1,0,1,0};
int dy[4] = {0,-1,0,1};
int site_map[MAX_LEN][MAX_LEN] = {0,};

bool in_range(int h, int w, int x, int y){
    if(x>=0 && x<h && y>=0 && y<w)
        return true;
    else    
        return false;
}

int find_max_dist(int h, int w, int x, int y){
    bool visit[h][w] = {false,};
    int max_dist = 0;
    queue<tuple<int,int,int>> q;
    visit[x][y] = true;
    q.push(make_tuple(x,y,0));
    while(!q.empty()){
        int now_x = get<0>(q.front());
        int now_y = get<1>(q.front());
        int dist = get<2>(q.front());
        q.pop();
        for(int i=0; i<4; i++){
            int nx = now_x + dx[i];
            int ny = now_y + dy[i];
            if(in_range(h,w,nx,ny) && !visit[nx][ny] && site_map[nx][ny]==1){
                q.push(make_tuple(nx,ny,dist+1));
                visit[nx][ny] = true;
                max_dist = max(max_dist,dist+1);
            }
        }
    }
    return max_dist;
}

int main(){
    int h, w;
    cin >> h >> w;
    for(int i=0; i<h; i++){
        for(int j=0; j<w; j++){
            char tmp;
            cin >> tmp;
            if(tmp == 'L')
                site_map[i][j] = 1;
            else
                site_map[i][j] = 0;
        }
    }

    int treasure_dist = 0;
    int tmp_dist = 0;
    for(int i=0; i<h; i++){
        for(int j=0; j<w; j++){
            if(site_map[i][j]==1){
                tmp_dist = find_max_dist(h,w,i,j);
                cout << tmp_dist << endl;
                treasure_dist = max(treasure_dist, tmp_dist);
            }
        }
    }
    cout << treasure_dist << endl;
    
    return 0;
}