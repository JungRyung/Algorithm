##### 와인 시식 #####
# URL : https://www.acmicpc.net/problem/2156
import sys
n = int(sys.stdin.readline())
w = [[] for _ in range(n)]
for i in range(n):
    w[i] = int(sys.stdin.readline())

if n == 1:
    print(w[0])
elif n == 2:
    print(w[0] + w[1])
else:
    d = [[0] for _ in range(n)]
    d[0] = w[0]
    d[1] = w[0] + w[1]
    d[2] = max(d[1], d[0]+w[2], w[1]+w[2])
    if n == 3:
        print(d[2])
    else:
        for i in range(3,n):
            d[i] = max(d[i-1], d[i-2]+w[i], d[i-3]+w[i-1]+w[i])
        print(d[n-1])