'''
TITLE   : 이중 우선순위 큐
URL     : https://www.acmicpc.net/problem/7662
DATE    : 21.10.12
'''
import sys
MAXLEN = 1000005

class SMMH:
    def __init__(self, initialCapacity):
        self.last = 1
        self.arrayLength = initialCapacity+2
        self.h = [0] * self.arrayLength

    def insert(self, x):
        # currentNode starts at new leaf and moves up to tree
        self.last += 1
        currentNode = self.last
        
        if self.last % 2 == 1 and x < self.h[self.last - 1]:
            # left sibling must be smaller, P1
            self.h[self.last] = self.h[self.last - 1]
            currentNode -= 1

        done = False
        while not done and currentNode >= 4:
            # currentNode has a grandparent
            gp = currentNode // 4   # grandparent
            lcgp = 2 * gp           # left child of gp
            rcgp = lcgp + 1         # right child of gp
            if x < self.h[lcgp]:
                # P2 is violated
                self.h[currentNode] = self.h[lcgp]
                currentNode = lcgp
            elif x > self.h[rcgp]:
                # P3 is violated
                self.h[currentNode] = self.h[rcgp]
                currentNode = rcgp
            else:
                done = True     # neither P2 nor P3 violated
        self.h[currentNode] = x

    def deleteMin(self):
        # When queue is empty
        if self.last == 2:
            self.last -= 1
        elif self.last > 2:
            x = self.h[self.last]
            self.last -= 1
            currentNode = 2
            
            done = False
            while not done and currentNode <= self.last:
                # satisfied P1
                if currentNode + 1 <= self.last and x > self.h[currentNode + 1]:
                    x, self.h[currentNode + 1] = self.h[currentNode + 1], x

                # satisfied P2
                left_child = currentNode * 2
                left_child_sibling = (currentNode + 1) * 2
                if left_child <= self.last and left_child_sibling <= self.last:
                    min_child = 0
                    if self.h[left_child] < self.h[left_child_sibling]:
                        min_child = left_child
                    else:
                        min_child = left_child_sibling

                    if x > self.h[min_child]:
                        self.h[currentNode] = self.h[min_child]
                        currentNode = min_child
                    else:
                        done = True
                elif left_child <= self.last and left_child_sibling > self.last:
                    if x > self.h[left_child]:
                        self.h[currentNode] = self.h[left_child]
                    else:
                        done = True
                else:
                    done = True
            self.h[currentNode] = x
    
    def deleteMax(self):
        if self.last == 2 or self.last == 3:
            self.last -= 1
        elif self.last > 3:
            x = self.h[self.last]
            self.last -= 1
            currentNode = 3

            done = False
            while not done and currentNode <= self.last:
                # satisfied P1
                if x < self.h[currentNode - 1]:
                    x, self.h[currentNode - 1] = self.h[currentNode - 1], x

                # satisfied P3
                right_child = currentNode * 2 + 1
                right_child_sibling = currentNode * 2 - 1
                if right_child <= self.last and right_child_sibling <= self.last:
                    max_child = 0
                    if self.h[right_child] > self.h[right_child_sibling]:
                        max_child = right_child
                    else:
                        max_child = right_child_sibling

                    if x < self.h[max_child]:
                        self.h[currentNode] = self.h[max_child]
                        currentNode = max_child
                    else:
                        done = True
                elif right_child_sibling <= self.last and right_child > self.last:
                    if x < self.h[right_child_sibling]:
                        self.h[currentNode] = self.h[right_child_sibling]
                        currentNode = right_child_sibling
                    else:
                        done = True
                else:
                    done = True
            self.h[currentNode] = x

    def getMin(self):
        if self.last == 1:
            print("QueueEmpty")
        else:
            return self.h[2]

    def getMax(self):
        if self.last == 1:
            print("QueueEmpty")
        elif self.last == 2:
            return self.h[2]
        else:
            return self.h[3]

    def printAnswer(self):
        # when heap is empty
        if self.last == 1:
            print("EMPTY")
        else:
            print(self.getMax(),self.getMin())

for _ in range(int(sys.stdin.readline())):
    q = SMMH(MAXLEN)
    k = int(sys.stdin.readline())
    for __ in range(k):
        command, num = sys.stdin.readline().split()
        if command == 'I':
            q.insert(int(num))
        else:
            if num == '1':
                q.deleteMax()
            else:
                q.deleteMin()
    q.printAnswer()
