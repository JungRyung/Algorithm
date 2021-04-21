#include <iostream>
#include <vector>
#include <queue>

#define MAXNUM 100

using namespace std;

bool visit[MAXNUM];
vector<int> graph[MAXNUM];
queue<int> q;

void BFS(int start){
    q.push(start);
    visit[start] = true;
    cout << start << " ";
    while(q.size()){
        int tmp = q.front();
        q.pop();
        for(int i=0; i<graph[tmp].size(); i++){
            int next = graph[tmp][i];
            if(!visit[next]){
                q.push(next);
                visit[next]=true;
                cout << next << " ";
            }
        }
    }
    cout << endl;
}

int main(){
    graph[1].push_back(2);
    graph[1].push_back(3);
    graph[1].push_back(8);

    graph[2].push_back(1);
    graph[2].push_back(7);

    graph[3].push_back(1);
    graph[3].push_back(4);
    graph[3].push_back(5);

    graph[4].push_back(3);
    graph[4].push_back(5);

    graph[5].push_back(3);
    graph[5].push_back(4);

    graph[6].push_back(7);

    graph[7].push_back(2);
    graph[7].push_back(6);
    graph[7].push_back(8);

    graph[8].push_back(1);
    graph[8].push_back(7);

    BFS(1);

    return 0;
}