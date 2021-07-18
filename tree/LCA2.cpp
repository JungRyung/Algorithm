/*
TITLE   : LCA 2
URL     : https://www.acmicpc.net/problem/11438
DATE    : 21.07.17
*/
#include <iostream>
#include <vector>
#include <string.h>
#define MAX 18  // log(2,100000)

using namespace std;

int depth[100001];
int parent[100001][MAX];
vector<int> adjacent[100001];

void make_tree(int curr){
    for(int next: adjacent[curr]){
        if(adjacent[curr][next] == -1){
            parent[next][0] = curr;
            depth[next] = depth[curr] + 1;
            make_tree(next);
        }
    }
}

int main(){
    int n=0;
    int m=0;
    scanf("%d",&n);
    for(int i=0; i<n-1; i++){
        int a, b;
        scanf("%d %d",&a,&b);
        adjacent[a].push_back(b);
        adjacent[b].push_back(a);
    }
    memset(parent,-1,sizeof(parent));
    fill(depth[0],depth[100001],-1);
    depth[1] = 0;
    
    make_tree(1);
    // parent 배열 채움
    for(int j=0; j<MAX-1; j++)
        for(int i=1; i<n; i++)
            if(parent[i][j] != -1)
                parent[i][j+1] = parent[parent[i][j]][j];

    scanf("%d",&m);
    for(int i=0; i<m; i++){
        int a, b;
        
    }
    
    
    return 0;
}