'''
TITLE   : 구간 합 구하기 2
URL     : https://www.acmicpc.net/problem/10999
DATE    : 21.09.14
'''
import sys

# 세그먼트 트리 알고리즘
def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    else:
        mid = (start+end)//2
        tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
        return tree[node]

def update_range(node, start, end, left, right, diff):
    update_lazy(node, start, end)
    if end < left or start > right:
        return
    if left <= start and end <= right:
        tree[node] += (end - start + 1) * diff
        if start != end:
            lazy[node*2] += diff
            lazy[node*2+1] += diff
        return
    mid = (start+end)//2
    update_range(node*2, start, mid, left, right, diff)
    update_range(node*2+1, mid+1, end, left, right, diff)
    tree[node] = tree[node*2] + tree[node*2+1]

def update_lazy(node, start, end):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0

def sub_sum(node, start, end, left, right):
    update_lazy(node, start, end)
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    return sub_sum(node*2, start, mid, left, right) + sub_sum(node*2+1, mid+1, end, left, right)
        
n, m, k = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(n)]
tree = [0] * n*4
lazy = [0] * n*4

init(1, 0, n-1)

for _ in range(m+k):
    temp_list = list(map(int, sys.stdin.readline().split()))
    # 수의 변경
    if temp_list[0] == 1:
        left, right, diff = temp_list[1:]
        update_range(1, 0, n-1, left-1, right-1, diff)
    elif temp_list[0] == 2:
        left, right = temp_list[1:]
        print(sub_sum(1, 0, n-1, left-1, right-1))