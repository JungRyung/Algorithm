/*
TITLE   : Count Circle Groups
URL     : https://www.acmicpc.net/problem/10216
DATE    : 21.10.07
*/
#include <iostream>
#include <tuple>
#include <vector>
#include <cmath>
#include<algorithm>
#define MAX 3005

using namespace std;

int find_parent(int* parent, int x){
    if(parent[x] != x)
        parent[x] = find_parent(parent, parent[x]);
    return parent[x];
}

void union_parent(int* parent, int a, int b){
    a = find_parent(parent, a);
    b = find_parent(parent, b);
    if(a < b)
        parent[b] = a;
    else
        parent[a] = b;
}

bool can_connected(tuple<int,int,int> point1, tuple<int,int,int> point2){
    int x1 = get<0>(point1);
    int y1 = get<1>(point1);
    int r1 = get<2>(point1);
    int x2 = get<0>(point2);
    int y2 = get<1>(point2);
    int r2 = get<2>(point2);
    int dist = pow(x2-x1, 2) + pow(y2-y1, 2);
    int dist2 = pow(r1+r2, 2);
    if(dist <= dist2)
        return true;
    return false;
}

int main(){
    int t;
    scanf("%d",&t);
    for(int i=0; i<t; i++){
        int n;
        scanf("%d",&n);
        vector<tuple<int, int, int> > points;
        // vector<int> parent;
        int parent[n];
        // parent init
        for(int j=0; j<n; j++){
            int x, y, r;
            scanf("%d %d %d",&x,&y,&r);
            points.push_back(make_tuple(x,y,r));
            parent[j] = j;
        }
        for(int j=0; j<n; j++){
            for(int k=j+1; k<n; k++){
                // printf("(%d, %d) : ",j,k);
                if(can_connected(points[j], points[k]))
                    union_parent(parent, j, k);
            }
        }
        int ans = 0;
        for(int j=0; j<n; j++)
            if(parent[j] == j)
                ans++;
        printf("%d\n",ans);
        // for(int j=0; j<parent.size(); j++)
        //     printf("%d ",parent[j]);
        // printf("\n");
        // parent.erase(unique(parent.begin(), parent.end()), parent.end());
        // printf("%lu\n",parent.size());
    }

    return 0;
}