#include <iostream>
#include <vector>
#include <stack>

#define MAXNUM 100

using namespace std;

bool visit[MAXNUM];
vector<int> graph[MAXNUM];
stack<int> s;

//스택을 사용한 DFS함수
void DFS(int start){
    //탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
    s.push(start);
    visit[start] = true;
    cout << start << " ";
    while(s.size()){
        //스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문처리를 한다.
        bool searched = false;
        for(int i=0; i<graph[s.top()].size(); i++){
            int next = graph[s.top()][i];
            if(!visit[next]){
                searched = true;
                s.push(next);
                visit[next]=true;
                cout << next << " ";
                break;
            }
        }
        //방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
        if(!searched)
            s.pop();
    }
    cout << endl;
}

//재귀적 방식을 사용한 DFS함수
void DFS_recursive(int v){
    //현재 노드 방문 처리
    visit[v] = true;
    cout << v << " ";
    //현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for(int i=0; i<graph[v].size(); i++){
        int next = graph[v][i];
        if(!visit[next]){
            DFS_recursive(next);
        }
    }
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

    // DFS(1);
    DFS_recursive(1);
    cout << endl;

    return 0;
}