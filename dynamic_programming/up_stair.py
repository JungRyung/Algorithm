##### 계단 오르기 #####
# URL : https://www.acmicpc.net/problem/2579
import sys
n = int(sys.stdin.readline())
s = [0] * n
for i in range(n):
    s[i] = int(sys.stdin.readline())

if n == 1:
    print(s[0])
elif n == 2:
    print(s[0] + s[1])
else:
    d = [0] * n
    d[0] = s[0]
    d[1] = s[0] + s[1]
    d[2] = max(s[2]+s[1], s[2]+s[0])
    if n == 3:
        print(d[2])
    else:
        for i in range(3,n):
            d[i] = max(s[i]+d[i-2], s[i]+s[i-1]+d[i-3])
        print(d[n-1])