#include <iostream>
#include <vector>
#include <queue>

#define MAXNUM 100

using namespace std;

vector<int> graph[MAXNUM];
bool visit[MAXNUM];
queue<int> q;

void BFS(int start){
    q.push(start);
    visit[start] = true;
    // cout << start << " ";
    while(q.size()){
        int tmp = q.front();
        q.pop();
        for(int i=0; i<graph[tmp].size(); i++){
            int next = graph[tmp][i];
            if(!visit[next]){
                q.push(next);
                visit[next]=true;
                // cout << next << " ";
            }
        }
    }
    // cout << endl;
}

int main(){
    
    return 0;
}