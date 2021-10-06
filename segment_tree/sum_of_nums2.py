'''
TITLE   : 수들의 합
URL     : https://www.acmicpc.net/problem/2268
DATE    : 21.10.06
'''
import sys
import heapq
from collections import deque
import copy
input = sys.stdin.readline
sys.setrecursionlimit(100000)
# sys.stdout.write()
#가장 작은 값에 존재하는 모든 소수를 곱한 값을 힙에 다시 넣음
tree = []
arr = []
def main():
    global tree, arr
    N, M = map(int, input().split())
    tree = [0 for _ in range(N+1)]
    arr = [0 for _ in range(N+1)]
    output = []
    quest = []
    # for _ in range(M):
    #     q, a, b = map(int, input().split())
    #     if q == 0:
    #         print("qqq")
    #         t = getSum(a,b)
    #         output.append(t)
    #     else:
    #         modify(a,b)
    for _ in range(M):
        quest.append(list(map(int, input().split())))
    for Q in quest:
        q,a,b = Q
        if q == 0:
            if a>b:
                a,b = b,a
            t = getSum(a-1,b)
            output.append(t)
        else:
            modify(a,b)
    print("\n".join(list(map(str, output))))

def modify(a,b):
    global tree, arr
    d = b-arr[a]
    arr[a] = b
    while(a<len(tree)):
        tree[a] += d
        a += (a & -a)
    # print(tree)
def getSum(a,b):
    global tree
    A, B = 0,0
    while(b):
        B += tree[b]
        b &= b-1
    while(a):
        A += tree[a]
        a &= a-1
    return B-A

main()