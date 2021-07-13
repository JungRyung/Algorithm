/*
TITLE   : 트리 순회
URL     : https://www.acmicpc.net/problem/1991
DATE    : 21.07.12
*/
#include <iostream>
#include <map>

using namespace std;

map<char, pair<char,char>> tree;

void preorder_trav(char node){
    cout << node;
    if(tree[node].first != '.')
        preorder_trav(tree[node].first);
    if(tree[node].second != '.')
        preorder_trav(tree[node].second);
}
void inorder_trav(char node){
    if(tree[node].first != '.')
        inorder_trav(tree[node].first);
    cout << node;
    if(tree[node].second != '.')
        inorder_trav(tree[node].second);
}
void postorder_trav(char node){
    if(tree[node].first != '.')
        postorder_trav(tree[node].first);
    if(tree[node].second != '.')
        postorder_trav(tree[node].second);
    cout << node;
}

int main(){
    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        char data,left,right;
        cin >> data >> left >> right;
        tree[data] = make_pair(left,right);
    }

    preorder_trav('A');
    cout << endl;
    inorder_trav('A');
    cout << endl;
    postorder_trav('A');
    cout << endl;

    return 0;
}