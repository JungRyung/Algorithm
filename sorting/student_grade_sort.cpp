#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

class Student{
private:
    string name;
    int grade;
public:
    Student(string n, int g){
        set_name(n);
        set_grade(g);
    }
    string get_name() const{
        return name;
    }
    int get_grade() const{
        return grade;
    }
    void set_name(string s){
        name = s;
    }
    void set_grade(int i){
        grade = i;
    }
    bool operator <(const Student &other) const{
        return this->get_grade() < other.get_grade();
    }
};

int main(){
    int N;
    cin >> N;

    vector<Student> s;

    for(int i=0; i<N; i++){
        string name;
        int grade;
        cin >> name;
        cin >> grade;

        Student stud(name,grade);
        s.push_back(stud);
    }
    
    sort(s.begin(),s.end());

    for(int i=0; i<N; i++){
        cout << s[i].get_name() << " ";
    }
    cout << endl;

    return 0;
}