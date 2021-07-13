'''
TITLE   : 트리 순회
URL     : https://www.acmicpc.net/problem/1991
DATE    : 21.07.12
'''
import sys

class node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)

def preorder_trav(node):
    print(node.data, end='')
    if node.left != '.':
        preorder_trav(tree[node.left])
    if node.right != '.':
        preorder_trav(tree[node.right])

def inorder_trav(node):
    if node.left != '.':
        inorder_trav(tree[node.left])
    print(node.data, end='')
    if node.right != '.':
        inorder_trav(tree[node.right])

def postorder_trav(node):
    if node.left != '.':
        postorder_trav(tree[node.left])
    if node.right != '.':
        postorder_trav(tree[node.right])
    print(node.data, end='')

n = int(sys.stdin.readline())

tree = {}

for _ in range(n):
    a, b, c = map(str, sys.stdin.readline().split())
    tree[a] = node(a, b, c)
preorder_trav(tree['A'])
print()
inorder_trav(tree['A'])
print()
postorder_trav(tree['A'])
print()