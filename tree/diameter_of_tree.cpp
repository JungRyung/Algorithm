/*
TITLE   : 트리의 지름
URL     : https://www.acmicpc.net/problem/1967
DATE    : 21.07.13
*/
#include <iostream>
#include <vector>
#include <utility>
#include <string.h>
#define MAX_LEN 10001

using namespace std;

vector<pair<int,int>> graph[MAX_LEN];
bool visit[MAX_LEN];
int max_cost;
int end_point;

void dfs(int curr, int length){
    visit[curr] = true;
    if(length > max_cost){
        max_cost = length;
        end_point = curr;
    } 
    for(int i=0; i<graph[curr].size(); i++){
        int next = graph[curr][i].first;
        if(!visit[next]){
            int cost = graph[curr][i].second;
            dfs(next, length + cost);
        }
    }
}

int main(){
    int n;
    scanf("%d",&n);
    for(int i=0; i<n-1; i++){
        int a, b, c;
        scanf("%d %d %d",&a,&b,&c);
        graph[a].push_back(make_pair(b,c));
        graph[b].push_back(make_pair(a,c));
    }

    //dfs
    dfs(1,0);
    max_cost = 0;
    fill(&visit[0],&visit[MAX_LEN],false);
    dfs(end_point,0);
    printf("%d\n",max_cost);

    return 0;
}