/*
TITLE   : 트리
URL     : https://www.acmicpc.net/problem/1068
DATE    : 21.07.13
*/
#include <iostream>
#include <vector>
#include <algorithm>
#define MAX_LEN 55

using namespace std;

vector<int> tree[MAX_LEN];
bool visit[MAX_LEN];
int cnt;

bool dfs(int curr, int removed){
    if(curr == removed)
        return false;
    int leng = tree[curr].size();
    bool searched = false;
    for(int i=0; i<leng; i++){
        int next = tree[curr][i];
        if(!visit[next]){
            bool valid = dfs(next,removed);
            if(valid){
                searched = true;
            }
        }
    }
    if(!searched)
        cnt++;
    return true;
}

int main(){
    int n=0;
    int root=0;
    scanf("%d",&n);
    for(int i=0; i<n; i++){
        int parent;
        scanf("%d",&parent);
        if(parent==-1)
            root = i;
        else
            tree[parent].push_back(i);
        
    }
    int removed_node;
    scanf("%d",&removed_node);
    
    dfs(root, removed_node);
    printf("%d\n",cnt);

    return 0;
}