'''
TITLE   : 트리 (전위순회, 중위순회를 입력으로 받고 후위순회를 출력하는 프로그램)
URL     : https://www.acmicpc.net/problem/4256
DATE    : 21.07.22
'''
import sys

t = int(sys.stdin.readline())

class Node:
    def __init__(self):
        self.key = None
        self.left = None
        self.right = None

class Btree:
    def __init__(self):
        self.root = Node()
    def make_tree(self, curr, preOrder, inOrder):
        curr.key = preOrder[0]
        index = inOrder.index(preOrder[0])
        # leftPre = []
        # rightPre = []
        if index > 0:               # left가 있을 때
            curr.left = Node()
            self.make_tree(curr.left, preOrder[1:index+1], inOrder[:index])
        if index < len(inOrder)-1:  # right가 있을 때
            curr.right = Node()
            self.make_tree(curr.right, preOrder[index+1:], inOrder[index+1:])
        # if len(preOrder) > 1:
        #     for num in preOrder[1:]:
        #         if num in inOrder[:index]:
        #             leftPre.append(num)
        #         else:
        #             rightPre.append(num)
        #     # left가 있을 때
        #     if leftPre:
        #         curr.left = Node()
        #         self.make_tree(curr.left, leftPre, inOrder[:index])
        #     # right가 있을 때
        #     if rightPre:
        #         curr.right = Node()
        #         self.make_tree(curr.right, rightPre, inOrder[index+1:])
    def postorder_trav(self,curr):
        if curr.left:
            self.postorder_trav(curr.left)
        if curr.right:
            self.postorder_trav(curr.right)
        print(curr.key,end=' ')

for _ in range(t):
    n = int(sys.stdin.readline())
    preOrder = list(map(int,sys.stdin.readline().split()))
    inOrder = list(map(int,sys.stdin.readline().split()))

    tree = Btree()
    tree.make_tree(tree.root, preOrder, inOrder)
    tree.postorder_trav(tree.root)
    print()