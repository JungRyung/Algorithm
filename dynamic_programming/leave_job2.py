import sys

n = int(sys.stdin.readline())
works = []
da = [0] * (n+1)
max_value = 0
for i in range(n):
    t, p = map(int, sys.stdin.readline().split())
    works.append((t,p))

for i in range(n-1, -1, -1):
    time = works[i][0] + i
    if time <= n:
        da[i] = max(works[i][1] + da[time], max_value)
        max_value = da[i]
    else:
        da[i] = max_value
print(max_value)