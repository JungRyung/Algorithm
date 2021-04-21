#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<string> split(string input, char delimiter);

int main(){
    string plans = "";
    int N;
    cin >> N;

    //버퍼 비워야 됨
    cin.ignore();
    getline(cin,plans);
    vector<string> plan = split(plans, ' ');

    int n=1;
    int m=1;
    for(int i=0; i<plan.size(); i++){
        if(plan[i] == "U"){
            if(n>1)
                n--;
        }else if(plan[i] == "D"){
            if(n<N)
                n++;
        }else if(plan[i] == "L"){
            if(m>1)
                m--;
        }else if(plan[i] == "R"){
            if(m<N)
                m++;
        }
    }

    cout << n << " " << m << endl;
    return 0;
}

vector<string> split(string input, char delimiter){
    vector<string> answer;
    stringstream ss(input);
    string temp;
 
    while (getline(ss, temp, delimiter)) {
        answer.push_back(temp);
    }
 
    return answer;
}