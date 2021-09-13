'''
TITLE   : 최솟값
URL     : https://www.acmicpc.net/problem/10868
DATE    : 21.09.13
'''
import sys
INF = 10e9

# 세그먼트 트리 알고리즘
def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    else:
        tree[node] = min(init(node*2, start, (start+end)//2), init(node*2+1, (start+end)//2+1, end))
        return tree[node]

def sub_min(node, start, end, left, right):
    if left > end or right < start:
        return INF
    if left <= start and end <= right:
        return tree[node]
    return min(sub_min(node*2, start, (start+end)//2, left, right), sub_min(node*2+1, (start+end)//2+1, end, left, right))

n, m = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(n)]
tree = [INF] * 3000000

init(1,0,n-1)
print(tree[:30])

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(sub_min(1,0,n-1,a-1,b-1))
