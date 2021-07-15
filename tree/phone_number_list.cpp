/*
TITLE   : 전화번호 목록
URL     : https://www.acmicpc.net/problem/5052
DATE    : 21.07.14
*/
#include <iostream>
#include <string>
#include <string.h>

using namespace std;

struct Node{
    bool is_end;
    Node *next[10];
    Node():is_end(false){
        memset(next,0,sizeof(next));
    }
    ~Node(){
        for(int i=0; i < 10; ++i){
			if(next[i])
				delete next[i];
		}
    }
};

class Dictree{
private:
    Node* root;
public:
    Dictree(){
        root = new Node;
    }
    bool insert(Node *curr,char* num){
        cout << curr->is_end;
        if(curr->is_end)
            return false;
        if(*num == '\n'){
            curr->is_end = true;
            return true;
        }
        else{
            int curr_num = *num - '0';
            if(curr->next[curr_num]==nullptr)
                curr->next[curr_num] = new Node;
            return insert(curr->next[curr_num], num + 1);
        }
    }
    Node* get_root(){
        return root;
    }
};

int main(){
    int t=0;
    scanf("%d",&t);
    while(t--){
        int n=0;
        scanf("%d",&n);
        Dictree tree;
        for(int i=0; i<n; i++){
            char* s;
            scanf("%s",s);
            bool valid = tree.insert(tree.get_root(),s);
            if(valid)
                printf("valid!\n");
            else
                printf("not valid!\n");
        }
    }

    return 0;
}