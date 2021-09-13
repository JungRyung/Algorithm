'''
TITLE   : 최솟값과 최대값
URL     : https://www.acmicpc.net/problem/10868
DATE    : 21.09.13
'''
import sys
INF = 10e9

# 세그먼트 트리 알고리즘
def init_min(node, start, end):
    if start == end:
        min_tree[node] = nums[start]
        return min_tree[node]
    else:
        min_tree[node] = min(init_min(node*2, start, (start+end)//2), init_min(node*2+1, (start+end)//2+1, end))
        return min_tree[node]

def init_max(node, start, end):
    if start == end:
        max_tree[node] = nums[start]
        return max_tree[node]
    else:
        max_tree[node] = max(init_max(node*2, start, (start+end)//2), init_max(node*2+1, (start+end)//2+1, end))
        return max_tree[node]

def sub_min(node, start, end, left, right):
    if left > end or right < start:
        return INF
    if left <= start and end <= right:
        return min_tree[node]
    return min(sub_min(node*2, start, (start+end)//2, left, right), sub_min(node*2+1, (start+end)//2+1, end, left, right))

def sub_max(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return max_tree[node]
    return max(sub_max(node*2, start, (start+end)//2, left, right), sub_max(node*2+1, (start+end)//2+1, end, left, right))

n, m = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(n)]
min_tree = [INF] * 3000000
max_tree = [0] * 3000000

init_min(1,0,n-1)
init_max(1,0,n-1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(sub_min(1,0,n-1,a-1,b-1), sub_max(1,0,n-1,a-1,b-1))