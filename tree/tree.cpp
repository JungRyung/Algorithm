/*
TITLE   : 트리
URL     : https://www.acmicpc.net/problem/1068
DATE    : 21.07.13
*/
#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#define MAX_LEN 51

using namespace std;

vector<int> tree[MAX_LEN];
bool visit[MAX_LEN];

int main(){
    int n;
    int root;
    scanf("%d",&n);
    for(int i=0; i<n; i++){
        int parent;
        scanf("%d",&parent);
        tree[parent].push_back(i);
        if(parent==-1)
            root = i;
    }
    int removed_node;
    scanf("%d",&removed_node);

    vector<int>().swap(tree[removed_node]);
    for(int i=0; i<n; i++){
        auto it = find(tree[i].begin(), tree[i].end(), removed_node);
        if(it != tree[i].end())
            tree[i].erase(it);
    }
    
    // dfs
    stack<int> s;
    s.push(root);
    int cnt = 0;
    while(!s.empty()){
        int curr = s.top();
        bool first_time = false;
        if(!visit[curr]){
            first_time = true;
            visit[curr] = true;
        }
        int leng = tree[curr].size();
        bool searched = false;
        for(int i=0; i<leng; i++){
            int next = tree[curr][i];
            if(!visit[next]){
                visit[next] = true;
                s.push(next);
                searched = true;
                break;
            }
        }
        if(first_time && !searched){
            cnt++;
            s.pop();
        }else if(!searched){
            s.pop();
        }
    }
    
    printf("%d\n",cnt);

    return 0;
}