'''
TITLE   : 불 켜기
URL     : https://www.acmicpc.net/problem/1505
DATE    : 21.09.27
'''
import sys
INF = 10e9

dx = [-1,0,1,0,0,-1,1,-1,1]
dy = [0,-1,0,1,0,-1,1,1,-1]

def print_bolbs(bolbs):
    for i in range(n):
        for j in range(n):
            if bolbs[i][j] == True:
                print('O',end='')
            else:
                print('#',end='')
        print()
    print()

n, m  = map(int,sys.stdin.readline().split())
arr = []
for i in range(n):
    fires = list(sys.stdin.readline().strip())
    tmp = []
    for fire in fires:
        if fire == '*':
            tmp.append(True)
        else:
            tmp.append(False)
    arr.append(tmp)

ans = INF
for f in range(1 << m):
    for g in range(1 << n):
        cnt = 0
        bolbs = []
        for i in range(n):
            bolbs.append(arr[i][:])

        turned = [[False]*m for _ in range(n)]

        for i in range(m): 
            if f & 1<<i:
                cnt += 1
                turned[0][i] = True
                for j in range(9):
                    nx = dx[j]
                    ny = i + dy[j]
                    if 0<=nx<n and 0<=ny<m:
                        bolbs[nx][ny] = not bolbs[nx][ny]
        
        for i in range(n):
            if g & 1<<i and turned[i][0] == False:
                cnt += 1
                for j in range(9):
                    nx = i + dx[j]
                    ny = dy[j]
                    if 0<=nx<n and 0<=ny<m:
                        bolbs[nx][ny] = not bolbs[nx][ny]
        
        for i in range(1,n):
            for j in range(1,m):
                if bolbs[i-1][j-1] == False:
                    cnt += 1
                    for k in range(9):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0<=nx<n and 0<=ny<m:
                            bolbs[nx][ny] = not bolbs[nx][ny]

        for i in range(n):
            if False not in bolbs[i]:
                ans = min(ans, cnt)
            
if ans != INF:
    print(ans)
else:
    print(-1)