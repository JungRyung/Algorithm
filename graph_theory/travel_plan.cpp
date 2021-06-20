//////// 여행 계획 ////////
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int find_parent(int* parent, int x){
    if(parent[x] != x)
        parent[x] = find_parent(parent,parent[x]);
    return parent[x];
}

void union_parent(int* parent, int a, int b){
    a = find_parent(parent, a);
    b = find_parent(parent, b);
    
    if(a<b)
        parent[b] = a;
    else
        parent[a] = b;
}

int main(){
    int n, m;
    cin >> n >> m;
    
    int parent[n+1] = {0, };
    for(int i=1; i<n+1; i++)
        parent[i] = i;
    
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            int data;
            cin >> data;
            if(data == 1)
                union_parent(parent,i+1,j+1);
        }
    }

    string str;
    vector<int> route;
    while(getline(cin,str,' '))
        route.push_back(stoi(str));

    int tmp_node = parent[route[0]];
    string answer = "YES";
    for(int i=0; i<route.size(); i++){
        if(parent[route[i]] != tmp_node){
            answer = "NO";
            break;
        }
    }
    cout << answer << endl;


    return 0;
}