/*
TITLE   : 정점들의 거리
URL     : https://www.acmicpc.net/problem/1761
DATE    : 21.07.20
*/
#include <iostream>
#include <string.h>
#include <vector>
#include <utility>
#define MAX 18

using namespace std;

int depth[40001];
int parent[40001][MAX];
long long dist[40001];
vector<pair<int,int>> adj[40001];

void make_tree(int curr){
    int leng = adj[curr].size();
    for(int i=0; i<leng; i++){
        int next = adj[curr][i].first;
        int next_dist = adj[curr][i].second;
        if(depth[next] == -1){
            depth[next] = depth[curr] + 1;
            dist[next] = dist[curr] + next_dist;
            parent[next][0] = curr;
            make_tree(next);
        }
    }
}

int main(){
    int n;
    scanf("%d",&n);
    for(int i=0; i<n-1; i++){
        int a, b, cost;
        scanf("%d %d %d",&a,&b,&cost);
        a--;
        b--;
        adj[a].push_back(make_pair(b,cost));
        adj[b].push_back(make_pair(a,cost));
    }
    memset(parent,-1,sizeof(parent));
    fill(depth,depth+n,-1);
    fill(dist,dist+n,-1);

    depth[0] = 0;
    dist[0] = 0;
    make_tree(0);

    for(int j=MAX-2; j>=0; j--)
        for(int i=1; i<n; i++)
            if(parent[i][j]!=-1)
                parent[i][j+1] = parent[parent[i][j]][j];

    int m;
    scanf("%d",&m);
    for(int i=0; i<m; i++){
        int a, b;
        scanf("%d %d",&a,&b);
        a--;
        b--;
        int tmp_a = a;
        int tmp_b = b;
        
        if(depth[a]<depth[b]) swap(a,b);
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
                if(parent[a][j] != -1 && parent[a][j]!=parent[b][j]){
                    a = parent[a][j];
                    b = parent[b][j];
                }
            }
            a = parent[a][0];
        }
        long long answer = dist[tmp_a] + dist[tmp_b] - (2 * dist[a]);
        printf("%lld\n",answer);
    }
    
    return 0;
}