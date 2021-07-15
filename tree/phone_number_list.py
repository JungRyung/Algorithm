'''
TITLE   : 전화번호 목록
URL     : https://www.acmicpc.net/problem/5052
DATE    : 21.07.15
'''
import sys

t = int(sys.stdin.readline())

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.next = {}

class Trie(object):
    def __init__(self):
        self.root = Node(None)
    def insert(self, numbers):
        curr = self.root
        for number in numbers:
            if number not in curr.next:
                curr.next[number] = Node(number)
            curr = curr.next[number]
        curr.data = numbers
    def is_valid(self, number):
        curr = self.root
        leng = len(number)
        for i in range(leng):
            if number[i] in curr.next:
                curr = curr.next[number[i]]
                if curr.data != None and i<leng-1:
                    return False
            else:
                return print("number is not in")
        return True

for _ in range(t):
    n = int(sys.stdin.readline())
    numbers = []
    for i in range(n):
        numbers.append(sys.stdin.readline().strip())
    number_list = Trie()
    for i in range(n):
        number_list.insert(numbers[i])
    is_valid = True
    for i in range(n):
        if not number_list.is_valid(numbers[i]):
            is_valid = False
            break
    if is_valid:
        print("YES")
    else:
        print("NO")