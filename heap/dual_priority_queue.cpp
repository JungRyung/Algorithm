/*
TITLE   : 이중 우선순위 큐
URL     : https://www.acmicpc.net/problem/7662
DATE    : 21.10.14
*/
#include <iostream>
#include <sstream>

using namespace std;

template <class T>
void ChangeSize1D(T*& a, const int oldSize, const int newSize){
    if (newSize < 0) throw "new length must be >= 0";
    
    T* temp = new T[newSize];
    int number = min(oldSize, newSize);
    copy(a, a + number, temp);
    delete []a;
    a = temp;
}

template <class T>
class SMMH{
public:
    SMMH(int initialCapacity = 10);
    ~SMMH() {delete []h;}
    
    void Display();
    void print_ans();
    const T& GetMin() const{
        // return min element
        if(last == 1) throw "QueueEmpty";
        return h[2];
    }

    const T& GetMax() const{
        // return max element
        if (last == 1) throw "QueueEmpty";
        if (last == 2) return h[2];
        else return h[3];
    }

    void Insert(const T&);
    void DeleteMin();
    void DeleteMax();
private:
    int last;           // position of last element in queue
    int arrayLength;    // queue capacity + 2
    T *h;               // element array
};

template <class T>
void SMMH<T>::Display(){
    int i;
    for(i=1; i <= arrayLength; i++) cout << i << ": " << h[i] << " ";
    cout << "\tlast : " << last << "\n";
}

template <class T>
void SMMH<T>::print_ans(){
    // 힙에 아무것도 없을 때
    if (last == 1){
        cout << "EMPTY\n";
    }else{
        cout << this->GetMax() << " " << this->GetMin() << "\n";
    }
}

template <class T>
SMMH<T>::SMMH(int initialCapacity){
    // Constructor.
    if(initialCapacity < 1){
        throw "Initial capacity Must be > 0";
    }
    arrayLength = initialCapacity + 2;
    h = new T[arrayLength];
    last = 1;
}

template <class T>
void SMMH<T>::Insert(const T& x){
    // Insert x into the SMMH.
    // increase array length if necessary
    if (last == arrayLength - 1){
        // double array length
        ChangeSize1D(h, arrayLength, 2 * arrayLength);
        arrayLength *= 2;
    }
    // find place for x
    // currentNode starts at new leaf and moves up tree
    int currentNode = ++last;
    if (last % 2 == 1 && x < h[last - 1]){
        // left sibling must be smaller, P1
        h[last] = h[last - 1];
        currentNode--;
    }
    bool done = false;
    while (!done && currentNode >= 4){
        // currentNode has a grandparent
        int gp = currentNode / 4;   // grandparent
        int lcgp = 2 * gp;          // left child of gp
        int rcgp = lcgp + 1;        // right child of gp
        if (x < h[lcgp]){
            // P2 is violated
            h[currentNode] = h[lcgp];
            currentNode = lcgp;
        }
        else if (x > h[rcgp]){
            // P3 is violated
            h[currentNode] = h[rcgp];
            currentNode = rcgp;
        }
        else done = true;   // neither P2 nor P3 violated
    }
    h[currentNode] = x;
}

template <class T>
void SMMH<T>::DeleteMin(){
    // when queue is empty
    if (last == 1){
        // throw "there are no elements in queue";
    }else if (last == 2){
        last--;
    }else{
        // last != 2
        T x = h[last--];
        // h[2] = x;
        int currentNode = 2;
        
        bool done = false;
        while (!done && currentNode <= last){
            // P1을 만족하는지
            if (currentNode + 1 <= last && x > h[currentNode + 1]){
                T tmp = x;
                x = h[currentNode + 1];
                h[currentNode + 1] = tmp;
            }

            // P2을 만족하는지
            int left_child = currentNode * 2;
            int left_child_sibling = (currentNode + 1) * 2;
            if (left_child <= last && left_child_sibling <= last){
                int min_child;
                if (h[left_child] < h[left_child_sibling])
                    min_child = left_child;
                else
                    min_child = left_child_sibling;
                
                if (x > h[min_child]){
                    h[currentNode] = h[min_child];
                    currentNode = min_child;
                }else{
                    done = true;
                }
            }else if ( left_child <= last && left_child_sibling > last){
                if (x > h[left_child]){
                    h[currentNode] = h[left_child];
                    currentNode = left_child;
                }else{
                    done = true;
                }
            }else
                done = true;
        }
        h[currentNode] = x;
    }
}

template <class T>
void SMMH<T>::DeleteMax(){
    if (last == 1){
        // throw "there are no elements in queue"; 
    }else if (last == 2 or last == 3){
        last--;
    }else{
        // last > 3
        T x = h[last--];
        int currentNode = 3;
        
        bool done = false;
        while (!done && currentNode <= last){
            // P1을 만족하는지
            if (x < h[currentNode - 1]){
                T tmp = x;
                x = h[currentNode - 1];
                h[currentNode - 1] = tmp;
            }

            // P3을 만족하는지
            int right_child = currentNode * 2 + 1;
            int right_child_sibling = currentNode * 2 - 1;
            if (right_child <= last && right_child_sibling <= last){
                int max_child;
                if (h[right_child] > h[right_child_sibling])
                    max_child = right_child;
                else
                    max_child = right_child_sibling;
                
                if (x < h[max_child]){
                    h[currentNode] = h[max_child];
                    currentNode = max_child;
                }else{
                    done = true;
                }
            }else if (right_child_sibling <= last && right_child > last){
                if (x < h[right_child_sibling]){
                    h[currentNode] = h[right_child_sibling];
                    currentNode = right_child_sibling;
                }else{
                    done = true;
                }
            }else
                done = true;
        }
        h[currentNode] = x;
    }
}
int main(){
    int t;
    cin >> t;
    while(t--){
        SMMH<int> q(1000005);
        int k;
        cin >> k;
        for(int i=0; i<k; i++){
            char command;
            int num;
            cin >> command >> num;
            if (command == 'I'){
                q.Insert(num);
            }else{
                if (num == 1)
                    q.DeleteMax();
                else
                    q.DeleteMin();
            }
        }
        q.print_ans();
    }

    return 0;
}