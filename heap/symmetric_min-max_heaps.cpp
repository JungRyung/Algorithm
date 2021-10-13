/*
Data Structure  : Min-Max Heaps
Date            : 21.10.13
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
class DEPQ{
public:
    virtual const T& GetMin() const = 0;
    virtual const T& GetMax() const = 0;
    virtual void Insert(const T&) = 0;
    virtual void DeleteMin() = 0;
    virtual void DeleteMax() = 0;
};

template <class T>
class SMMH{
public:
    SMMH(int initialCapacity = 10);
    ~SMMH() {delete []h;}
    
    void QueueEmpty(){ cout << "QueueEmpty" << "\n";};
    void Display();
    const T& GetMin() const{
        // return min element
        if(last == 1) throw QueueEmpty();
        return h[2];
    }

    const T& GetMax() const{
        // return max element
        if (last == 1) throw QueueEmpty();
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
    cout << "\n";
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
    if (last == 1) throw "there are no elements in queue";
    else if (last == 2){
        h[2] = 0;
        last--;
    }
    else{
        // last != 2
        int x = h[last--];
        h[2] = x;
        int currentNode = 2;
        
    }
    int x = h[last]
}

int main(){
    SMMH<int> m(20);
    m.Insert(4);
    m.Insert(8);
    m.Insert(12);
    m.Insert(20);
    m.Insert(60);
    m.Insert(10);
    m.Insert(16);
    m.Insert(80);
    m.Insert(6);
    m.Insert(14);
    m.Insert(30);
    m.Insert(40);
    m.Insert(2);
    m.Display();

    return 0;
}