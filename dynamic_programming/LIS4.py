##### 가장 긴 증가하는 부분 수열 4 #####
# URL : https://www.acmicpc.net/problem/14002
import sys

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
lis = [[num] for num in seq]
cache = [1 for _ in range(n)]
print(lis)
print(cache)

for i in range(n):
    for j in range(i):
        if seq[j] < seq[i]:
            if cache[i] < cache[j] + 1:
                lis[i] = lis[j] + [seq[i]]
                cache[i] = cache[j] + 1
print(lis)
print(cache)
max_len = -1
idx = -1
for i in range(n):
    if max_len < cache[i]:
        max_len = cache[i]
        idx = i
print(max_len)
print(*lis[idx])