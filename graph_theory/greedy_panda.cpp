/*
TITLE   : 욕심쟁이 판다
URL     : https://www.acmicpc.net/problem/1937
DATE    : 21.08.24
*/
#include <iostream>
#include <algorithm>
#define MAXLEN 501

using namespace std;

int n;
int forest[MAXLEN][MAXLEN];
int dp[MAXLEN][MAXLEN];

int dx[4] = {-1,0,1,0};
int dy[4] = {0,-1,0,1};

int dfs(int x, int y){
    if(dp[x][y] < 0){
        dp[x][y] = 0;
        for(int i=0; i<4;i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx >= 0 && nx < n && ny >= 0 && ny < n && forest[x][y] < forest[nx][ny])
                dp[x][y] = max(dp[x][y], dfs(nx,ny));
        }
        ++dp[x][y];
    }
    return dp[x][y];
}

int main(){
    fill(&dp[0][0], &dp[MAXLEN - 1][MAXLEN], -1);
    scanf("%d",&n);
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            scanf("%d",&forest[i][j]);
        }
    }

    int ans = 0;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            ans = max(ans, dfs(i,j));
        }
    }
    printf("%d\n",ans);

    return 0;
}