//////// 행성 터널 /////////
// 최소신장트리 구하기 -> Kruscal
#include <iostream>
#include <tuple>
#include <vector>
#include <algorithm>
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
    int n;
    cin >> n;
    
    vector<tuple<int,int,int>> edges;
    int parent[n] = {0, };
    for(int i=0; i<n; i++)
        parent[i] = i;

    vector<pair<int,int>> x;
    vector<pair<int,int>> y;
    vector<pair<int,int>> z;

    for(int i=0; i<n; i++){
        int tmpX,tmpY,tmpZ;
        cin >> tmpX >> tmpY >> tmpZ;
        x.push_back(make_pair(tmpX,i));
        y.push_back(make_pair(tmpY,i));
        z.push_back(make_pair(tmpZ,i));
    }
    sort(x.begin(),x.end());
    sort(y.begin(),y.end());
    sort(z.begin(),z.end());

    for(int i=0; i<n-1; i++){
        edges.emplace_back(x[i+1].first-x[i].first, x[i].second,x[i+1].second);
        edges.emplace_back(y[i+1].first-y[i].first, y[i].second,y[i+1].second);
        edges.emplace_back(z[i+1].first-z[i].first, z[i].second,z[i+1].second);
    }
    sort(edges.begin(), edges.end());
    int answer = 0;

    for(int i=0; i<edges.size(); i++){
        int cost = get<0>(edges[i]);
        int a = get<1>(edges[i]);
        int b = get<2>(edges[i]);
        if(find_parent(parent,a) != find_parent(parent,b)){
            union_parent(parent,a,b);
            answer += cost;
        }
    }
    cout << answer << endl;

    return 0;
}