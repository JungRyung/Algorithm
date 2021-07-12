/*
TITLE   : 파티
URL     : https://www.acmicpc.net/problem/1238
DATE    : 21.07.11
*/
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <queue>

using namespace std;

const int MAX_LEN = 1001;
const int MAX_TIME = 1000;

vector<pair<int,int>> graph[MAX_LEN];
int distance_to[MAX_LEN][MAX_LEN];

void dijkstra(int start){
    priority_queue<pair<int,int>> pq;
    pq.push(make_pair(0,start));
    distance_to[start][start] = 0;
    while(!pq.empty()){
        int dist = -pq.top().first;
        int now = pq.top().second;
        pq.pop();
        if(distance_to[start][now] < dist)
            continue;
        for(auto i=graph[now].begin(); i!=graph[now].end(); i++){
            int next = (*i).first;
            int next_dist = (*i).second;
            int cost = distance_to[start][now] + next_dist;
            if(cost < distance_to[start][next]){
                distance_to[start][next] = cost;
                pq.push(make_pair(-cost,next));
            }
        }
    }
}

int main(){
    int n, m, x;
    cin >> n >> m >> x;

    fill(&distance_to[0][0],&distance_to[MAX_LEN-1][MAX_LEN],MAX_TIME);

    for(int i=0; i<m; i++){
        int t,a,b;
        cin >> a >> b >> t;
        graph[a].push_back(make_pair(b,t));
    }
    
    // 다익스트라
    for(int i=1; i<n+1; i++)
        dijkstra(i);

    int max_sum = 0;
    for(int i=1; i<n+1; i++)
        if(i!=x)
            max_sum = max(max_sum, distance_to[i][x]+distance_to[x][i]);
    cout << max_sum << endl;

    return 0;
}