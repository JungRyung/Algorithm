### 공유기 설치 ###
import sys
n, c = map(int, sys.stdin.readline().split())
homes = []
for i in range(n):
    homes.append(int(sys.stdin.readline()))
homes.sort()

min_dist = 1e9
for i in range(n-1):
    min_dist = min(min_dist, homes[i+1]-homes[i])

left = min_dist
right = homes[-1] - homes[0]
result = 0

while left<=right:
    mid = (left+right) // 2
    value = homes[0]
    cnt = 1

    for i in range(1,n):
        if homes[i] >= value + mid:
            value = homes[i]
            cnt += 1
    
    if cnt >= c:
        left = mid + 1
        result = mid
    else:
        right = mid -1

print(result)