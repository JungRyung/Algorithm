'''
TITLE   : 구간 곱 구하기
URL     : https://www.acmicpc.net/problem/11505
DATE    : 21.09.13
'''
import sys
DIV = 1000000007

# 세그먼트 트리 알고리즘
def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    else:
        tree[node] = init(node*2, start, (start+end)//2) * init(node*2+1, (start+end)//2+1, end) % DIV
        return tree[node]

def sub_mul(node, start, end, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    return sub_mul(node*2, start, (start+end)//2, left, right) * sub_mul(node*2+1, (start+end)//2+1, end, left, right) % DIV

def update(node, start, end, index, newValue):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = newValue
        return
    update(node*2, start, (start+end)//2, index, newValue)
    update(node*2+1, (start+end)//2+1, end, index, newValue)

    tree[node] = tree[node*2]*tree[node*2+1] % DIV

n, m, k = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(n)]
tree = [0] * 3000000

init(1, 0, n-1)

for _ in range(m+k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        b = b-1
        nums[b] = c
        update(1, 0, n-1, b, c)
    elif a == 2:
        print(sub_mul(1, 0, n-1, b-1, c-1)%DIV)
