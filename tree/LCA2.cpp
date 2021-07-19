/*
TITLE   : LCA 2
URL     : https://www.acmicpc.net/problem/11438
DATE    : 21.07.17
*/
#include <iostream>
#include <vector>
#include <string.h>
#define MAX 18

using namespace std;

int depth[100000];
int parent[100000][MAX];
vector<int> adjacent[100000];

void make_tree(int curr){
    for(int next: adjacent[curr]){
        if(depth[next] == -1){
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
        a--;
        b--;
        adjacent[a].push_back(b);
        adjacent[b].push_back(a);
    }
    memset(parent,-1,sizeof(parent));
    fill(depth,depth+n,-1);
    depth[0] = 0;
    
    make_tree(0);
    for(int j=0; j<MAX-1; j++)
        for(int i=1; i<n; i++)
            if(parent[i][j] != -1)
                parent[i][j+1] = parent[parent[i][j]][j];

    scanf("%d",&m);
    for(int i=0; i<m; i++){
        int a, b;
        scanf("%d %d",&a,&b);
        a--;
        b--;
        if(depth[a] < depth[b]) swap(a,b);
        int diff = depth[a] - depth[b];

        int j=0;
        while(diff){
            if(diff%2)
                a = parent[a][j];
            j++;
            diff /= 2;
        }
        
        if(a!=b){
            for(j=MAX-1; j>=0; j--){
                if(parent[a][j] != parent[b][j]){
                    a = parent[a][j];
                    b = parent[b][j];
                }
            }
            a = parent[a][0];
        }
        printf("%d\n",a+1);
    }
    return 0;
}