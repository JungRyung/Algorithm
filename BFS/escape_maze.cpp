#include <iostream>
#include <vector>
#include <queue>

#define MAXNUM 100

using namespace std;

int N, M;
int graph[MAXNUM][MAXNUM] = {0,};
queue<pair<int,int> > q;

int dx[4] = {0,1,0,-1};
int dy[4] = {-1,0,1,0};

// void BFS(int start){
//     q.push(start);
//     visit[start] = true;
//     cout << start << " ";
//     while(q.size()){
//         int tmp = q.front();
//         q.pop();
//         for(int i=0; i<graph[tmp].size(); i++){
//             int next = graph[tmp][i];
//             if(!visit[next]){
//                 q.push(next);
//                 visit[next]=true;
//                 cout << next << " ";
//             }
//         }
//     }
//     cout << endl;
// }
void escape(int x, int y){
    q.push(make_pair(x,y));
    while(q.size()){
        int tmp_x = q.front().first;
        int tmp_y = q.front().second;
        q.pop();
        for(int i=0; i<4; i++){
            int nx = tmp_x + dx[i];
            int ny = tmp_y + dy[i];
            // 정해진 공간을 벗어난 경우 무시
            if(nx < 0 || ny < 0 || nx >= N || ny >= M)
                continue;
            if(graph[nx][ny]==1){
                cout << "(" << nx << ", " << ny << ")" << endl;
                q.push(make_pair(nx,ny));
                graph[nx][ny] = graph[tmp_x][tmp_y] + 1;
            }
        }
    }
}

int main(){
    cin >> N;
    cin >> M;
    cout << "input N,M complete" << endl;

    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cin >> graph[i][j];
        }
    }
    cout << "input complete" << endl;
    escape(0,0);
    cout << graph[N-1][M-1] << endl;
    return 0;
}