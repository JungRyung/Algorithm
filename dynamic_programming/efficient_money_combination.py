n , m = map(int, input().split())

# 메모이제이션
d = [10001] * (m+1)

for i in range(n):
    num = int(input())
    cnt = 1
    while num*cnt <= m:
        d[num*cnt] = min(d[num*cnt], cnt)
        cnt += 1

print(d[m] if d[m]<10001 else -1)