/*
TITLE   : 트리의 부모 찾기
URL     : https://www.acmicpc.net/problem/11725
DATE    : 21.07.13
*/
#include <iostream>
#include <vector>
#include <queue>
#define MAX_LEN 100001

using namespace std;

vector<int> edges[MAX_LEN];
int parent[MAX_LEN] = {0};
// bool visit[MAX_LEN];

int main(){
    int n;
    cin >> n;
    for(int i=0; i<n-1; i++){
        int a, b;
        scanf("%d %d",&a,&b);
        edges[a].push_back(b);
        edges[b].push_back(a);
    }

    // 루트부터 BFS하면서 메모
    queue<int> q;
    q.push(1);
    // visit[1] = true;

    while(!q.empty()){
        int before_node = q.front();
        q.pop();
        int leng = edges[before_node].size();
        for(int i=0; i<leng; i++){
            int next = edges[before_node][i];
            if(parent[before_node]==next)
                continue;
            q.push(next);
            parent[next] = before_node;
        }
    }

    for(int i=2; i<=n; i++)
        printf("%d\n",parent[i]);

    return 0;
}