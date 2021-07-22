'''
TITLE   : 완전 이진 트리
URL     : https://www.acmicpc.net/problem/9934
DATE    : 21.07.22
'''
import sys

def append_answer(start, end, level):
    if level == k:
        return
    root = start + (end - start) // 2
    answer[level].append(inorder[root])
    append_answer(start, root-1, level+1)
    append_answer(root+1, end, level+1)

k = int(sys.stdin.readline())
answer = [[] for _ in range(k)]

inorder = list(map(int, sys.stdin.readline().split()))

append_answer(0,len(inorder)-1, 0)

for i in range(k):
    for num in answer[i]:
        print(num,end=' ')
    print()