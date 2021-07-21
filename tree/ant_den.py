'''
TITLE   : 개미굴
URL     : https://www.acmicpc.net/problem/14725
DATE    : 21.07.20
'''
import sys

class Node:
    def __init__(self, key, level, data=None):
        self.key = key
        self.data = data
        self.level = level
        self.child = {}

class Trie:
    def __init__(self):
        self.root = Node(None,0)
    def insert(self,foods):
        curr = self.root
        for food in foods:
            if food not in curr.child:
                curr.child[food] = Node(food, curr.level+1)
            curr = curr.child[food]
        curr.data = foods
    def print_den(self,curr):
        for food in sorted(curr.child.keys()):
            print('--'*curr.level+food)
            self.print_den(curr.child[food])
        
n = int(sys.stdin.readline())
ants = [[] for _ in range(n)]
for i in range(n):
    ants[i] = list(sys.stdin.readline().split())[1:]

tree = Trie()
for foods in ants:
    tree.insert(foods)

tree.print_den(tree.root)