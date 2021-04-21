#include <iostream>
#include <vector>
#include <queue>

#define MAXNUM 100

using namespace std;

int N, M;
int graph[MAXNUM][MAXNUM] = {1,};

bool DFS(int x,int y){
    if(x<0 || x>=N || y<0 || y>=M)
        return false;
    if(graph[x][y]==0){
        // cout << "(" << x << ", " << y << ")" << endl;
        graph[x][y] = 1;
        DFS(x-1,y);
        DFS(x+1,y);
        DFS(x,y-1);
        DFS(x,y+1);
        return true;
    }
    return false;
}

int main(){
    cin >> N;
    cin >> M;
    int result = 0;

    //그래프 초기화 (입력받음)
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cin >> graph[i][j];
        }
    }

    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            if(DFS(i,j))
                result++;
        }
    }

    cout << result << endl;
    
    return 0;
}