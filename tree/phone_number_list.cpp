/*
TITLE   : 전화번호 목록
URL     : https://www.acmicpc.net/problem/5052
DATE    : 21.07.14
*/
#include <iostream>
#include <string>
#include <string.h>
#include <vector>

using namespace std;

struct Node{
    bool is_end;
    Node *next[10];
    Node(){
        is_end = false;
        for(int i=0; i < 10; i++){
            next[i] = nullptr;
        }
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
    void insert(Node *curr,char* num){
        if(*num == '\0')
            curr->is_end = true;
        else{
            int curr_num = *num - '0';
            if(curr->next[curr_num]==nullptr)
                curr->next[curr_num] = new Node;
            return insert(curr->next[curr_num], num + 1);
        }
    }
    bool is_valid(Node *curr, char* num){
        if(curr->is_end && *num != '\0'){
            return false;
        }else if(curr->is_end && *num == '\0'){
            return true;
        }else{
            int curr_num = *num - '0';
            if(curr->next[curr_num]==nullptr){
                printf("number is not in\n");
                return false;
            }
            return is_valid(curr->next[curr_num], num + 1);
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
        bool is_valid = true;
        vector<string> numbers;
        scanf("%d",&n);
        cin.ignore();
        Dictree tree;
        for(int i=0; i<n; i++){
            string s;
            getline(cin,s);
            numbers.push_back(s);
            char* c = &s[0];
            tree.insert(tree.get_root(),c);
        }
        for(int i=0; i<n; i++){
            string s = numbers[i];
            char* c = &s[0];
            is_valid = tree.is_valid(tree.get_root(),c);
            if(!is_valid)
                break;
        }
        if(is_valid)
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}