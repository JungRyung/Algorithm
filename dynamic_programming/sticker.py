##### 스티커 #####
# URL : https://www.acmicpc.net/problem/9465
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    sticker = []
    for i in range(2):
        sticker.append(list(map(int, sys.stdin.readline().split())))
    sticker[0].append(0)
    sticker[1].append(0)
    for i in range(n):
        sticker[0][i] += max(sticker[1][max(i-1,-1)],sticker[1][max(i-2,-1)])
        sticker[1][i] += max(sticker[0][max(i-1,-1)],sticker[0][max(i-2,-1)])
    print(max(sticker[0][n-1],sticker[1][n-1]))