'''
TITLE   : 전구 끄기
URL     : https://www.acmicpc.net/problem/14927
DATE    : 21.09.27
'''
import sys
INF = 10e9

dx = [-1,0,1,0,0]
dy = [0,-1,0,1,0]

def print_bolbs(bolbs):
    for i in range(n):
        for j in range(n):
            if bolbs[i][j] == True:
                print('O',end='')
            else:
                print('#',end='')
        print()
    print()

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    fires = list(map(int, sys.stdin.readline().split()))
    tmp = []
    for fire in fires:
        if fire == 1:
            tmp.append(True)
        else:
            tmp.append(False)
    arr.append(tmp)

ans = INF
for f in range(1 << n):
    cnt = 0
    bolbs = []
    for i in range(n):
        bolbs.append(arr[i][:])

    for i in range(n):
        if f & 1<<i:
            cnt += 1
            for j in range(5):
                nx = 0 + dx[j]
                ny = i + dy[j]
                if 0<=nx<n and 0<=ny<n:
                    bolbs[nx][ny] = not bolbs[nx][ny]
    
    for i in range(1,n):
        for j in range(n):
            if bolbs[i-1][j] == True:
                cnt += 1
                for k in range(5):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        bolbs[nx][ny] = not bolbs[nx][ny]

    if True not in bolbs[-1]:
        ans = min(ans, cnt)

if ans != INF:
    print(ans)
else:
    print(-1)