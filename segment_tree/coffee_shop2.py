'''
TITLE   : 커피숍2
URL     : https://www.acmicpc.net/problem/1275
DATE    : 21.10.06
'''
import sys

def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    else:
        mid = (start+end)//2
        tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
        return tree[node]

def sub_sum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    return sub_sum(node*2, start, mid, left, right) + sub_sum(node*2+1, mid+1, end, left, right)

def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        mid = (start+end)//2
        update(node*2, start, mid, index, diff)
        update(node*2+1, mid+1, end, index, diff)

n, q = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
tree = [0] * 3000000

init(1,0,n-1)

for _ in range(q):
    x, y, a, b = map(int, sys.stdin.readline().split())
    if x > y:
        x, y = y, x
    print(sub_sum(1,0,n-1,x-1,y-1))
    a = a-1
    diff = b - nums[a]
    nums[a] = b
    update(1,0,n-1,a,diff)