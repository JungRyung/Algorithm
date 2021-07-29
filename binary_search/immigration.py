'''
TITLE   : 입국심사
URL     : https://www.acmicpc.net/problem/3079
DATE    : 21.07.29
'''
import sys

def count_num(sec):
    res = 0
    for checkpoint in checkpoints:
        res += sec // checkpoint
        if res > m:
            break
    return res

n, m = map(int, sys.stdin.readline().split())
checkpoints = []
for _ in range(n):
    checkpoints.append(int(sys.stdin.readline()))

left = 0
right = max(checkpoints) * m
answer = 0
while left <= right:
    mid = (left + right) // 2
    if count_num(mid) >= m:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(int(answer))