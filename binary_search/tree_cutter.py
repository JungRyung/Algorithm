'''
TITLE   : 나무 절단기
URL     : https://www.acmicpc.net/problem/2805
DATE    : 21.07.28
'''
import sys

def cutting(trees, h):
    res = 0
    for tree in trees:
        if tree > h:
            res += tree - h
    return res

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

left = 0
right = max(trees)

max_H = 0
while left <= right:
    mid = (left + right) // 2
    cutted = cutting(trees, mid)
    if cutted > m:
        max_H = mid
        left = mid + 1
    elif cutted < m:
        right = mid - 1
    else:
        max_H = mid
        break
print(max_H)