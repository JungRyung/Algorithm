/*
Title   : 토마토
URL     : https://www.acmicpc.net/problem/7576
date    : 21.07.10
*/
#include <iostream>
#include <stack>
#include <utility>
#include <vector>
#define MAX_LEN 1001

using namespace std;

int main(){
    int dx[] = {-1,0,1,0};
    int dy[] = {0,-1,0,1};
    int box[MAX_LEN][MAX_LEN] = {0};
    vector<pair<int,int>> ripe;
    int tomato_cnt = 0;
    int n, m;
    
    cin >> m >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cin >> box[i][j];
            if(box[i][j]==1 || box[i][j]==0){
                tomato_cnt ++;
                if(box[i][j]==1)
                    ripe.push_back(make_pair(i,j));
            }
        }
    }
    int day = 0;
    while(true){
        // for(int i=0; i<n; i++){
        //     for(int j=0; j<m; j++){
        //         cout << box[i][j] << ' ';
        //     }
        //     cout << endl;
        // }
        stack<pair<int,int>> s;
        int visit[MAX_LEN][MAX_LEN] = {0};
        int modify_cnt = 0;
        for(int i=0; i<ripe.size(); i++){
            int x = ripe[i].first;
            int y = ripe[i].second;
            for(int k=0; k<4; k++){
                int nx = x + dx[k];
                int ny = y + dy[k];
                if(nx>=0 && nx<n && ny>=0 && ny<m && box[nx][ny]==0 && visit[nx][ny]==0){
                    s.push(make_pair(nx,ny));
                    visit[nx][ny] = 1;
                    modify_cnt++;
                }
            }
        }
        while(!s.empty()){
            int x = s.top().first;
            int y = s.top().second;
            ripe.push_back(make_pair(x,y));
            s.pop();
            box[x][y] = 1;
        }
        if(modify_cnt==0 && ripe.size()!=tomato_cnt){
            cout << "-1" << endl;
            break;
        }else if(modify_cnt==0 && ripe.size()==tomato_cnt){
            cout << day << endl;
            break;
        }

        day++;
    }
    
    
    return 0;
}