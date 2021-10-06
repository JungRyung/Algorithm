/*
TITLE   : 수들의 합
URL     : https://www.acmicpc.net/problem/2268
DATE    : 21.10.06
*/
#include <iostream>
#define MAX 4000001

using namespace std;
typedef long long LL;

int nums[MAX];
LL tree[MAX];

LL init(int node, int start, int end){
    if(start == end){
        tree[node] = nums[start];
        return tree[node];
    }
    else{
        int mid = (start+end)/2;
        tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end);
        return tree[node];
    }
}

LL sub_sum(int node, int start, int end, int left, int right){
    if(left > end || right < start) return 0;
    if(left <= start && end <= right) return tree[node];
    int mid = (start+end)/2;
    return sub_sum(node*2, start, mid, left, right) + sub_sum(node*2+1, mid+1, end, left, right);
}

void update(int node, int start, int end, int index, int diff){
    if(index > end || index < start) return;
    tree[node] += diff;
    if(start != end){
        int mid = (start+end)/2;
        update(node*2, start, mid, index, diff);
        update(node*2+1, mid+1, end, index, diff);
    }
}

int main(){
    int n, m;
    scanf("%d %d", &n, &m);
    init(1,0,n-1);
    for(int i=0; i<m; i++){
        int cal, a, b;
        scanf("%d %d %d", &cal, &a, &b);
        // sum
        if(cal == 0){
            if(a > b){
                int tmp = a;
                a = b;
                b = tmp;
            }
            printf("%lld\n",sub_sum(1,0,n-1,a-1,b-1));
        }
        else{
            a = a-1;
            int diff = b - nums[a];
            nums[a] = b;
            update(1,0,n-1,a,diff);
        }
    }
    return 0;
}