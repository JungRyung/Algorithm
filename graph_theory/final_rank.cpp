////// 최종 순위 //////
// 위상 정렬 알고리즘
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main(){
    int t;
    cin >> t;
    for(int v=0; v<t; v++){
        // 노드의 개수 입력
        int n;
        cin >> n;
        int indegree[n+1] = {0, };
        bool graph[n+1][n+1] = {false, };
        // 작년 순위 입력
        int rank[n];
        for(int i=0; i<n; i++)
            cin >> rank[i];
        // 그래프 초기화
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                graph[rank[j]][rank[i]] = true;
                indegree[rank[i]] += 1;
            }
        }
        // 변경된 순위 정보 입력
        int m;
        cin >> m;
        for(int i=0; i<m; i++){
            int a, b;
            cin >> a >> b;
            // 간선 방향 반대로
            if(graph[a][b]){
                graph[a][b] = false;
                graph[b][a] = true;
                indegree[a] += 1;
                indegree[b] -= 1;
            }else{
                graph[a][b] = true;
                graph[b][a] = false;
                indegree[a] -= 1;
                indegree[b] += 1;
            }
        }

        // 위상정렬 알고리즘
        vector<int> result;
        queue<int> q;
        for(int i=1; i<n+1; i++)
            if(indegree[i] == 0)
                q.push(i);
        bool only = true;
        bool cycle = false;

        for(int i=0; i<n; i++){
            if(q.size() == 0){
                cycle = true;
                break;
            }
            if(q.size() >= 2){
                only = false;
                break;
            }
            int current = q.front();
            q.pop();
            result.push_back(current);
            for(int j=1; j<n+1; j++){
                if(graph[current][j]){
                    indegree[j] -= 1;
                    if(indegree[j] == 0)
                        q.push(j);
                }
            }
        }
        if(cycle)
            cout << "IMPOSSIBLE" << endl;
        else if(!only)
            cout << "?" << endl;
        else{
            while(result.size()>0){
                cout << result.back() << " ";
                result.pop_back();
            }
            cout << endl;
        }
    }

    return 0;
}