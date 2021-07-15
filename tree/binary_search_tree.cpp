/*
TITLE   : 이진 검색 트리
URL     : https://www.acmicpc.net/problem/5639
DATE    : 21.07.15
*/
#include <iostream>
#include <string>

using namespace std;

struct Node{
    int data;
    Node* left;
    Node* right;
    Node(){
        data = 0;
        left = nullptr;
        right = nullptr;
    }
    ~Node(){
        delete left;
        delete right;
    }
};

class Bitree{
private:
    Node* root;
public:
    Bitree(){
        root = nullptr;
    }
    void add_node(int num){
        Node* node = new Node;
        node->data = num;
        if(root == nullptr)
            root = node;
        else{
            Node* curr = root;
            while(curr){
                if(curr->data > num){
                    if(curr->left!=nullptr)
                        curr = curr->left;
                    else{
                        curr->left = node;
                        return;
                    }
                }
                else if(curr->data < num){
                    if(curr->right!=nullptr)
                        curr = curr->right;
                    else{
                        curr->right = node;
                        return;
                    }
                }
                else{
                    printf("It is already existed!\n");
                    return;
                }
            }
            curr = node;
        }
    }
    void postorder_trav(Node* curr){
        if(curr->left!=nullptr)
            postorder_trav(curr->left);
        if(curr->right!=nullptr)
            postorder_trav(curr->right);
        printf("%d\n",curr->data);
    }
    
    Node* get_root(){
        return root;
    }
};

int main(){
    Bitree tree;
    string s;
    while(getline(cin,s)){
        int num = stoi(s);
        tree.add_node(num);
    }
    tree.postorder_trav(tree.get_root());
    return 0;
}