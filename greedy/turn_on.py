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

        print_bolbs(bolbs)

        for i in range(m): 
            if f & 1<<i:
                cnt += 1
                for j in range(9):
                    nx = 1 + dx[j]
                    ny = i+1 + dy[j]
                    if 0<=nx<n and 0<=ny<m:
                        bolbs[nx][ny] = not bolbs[nx][ny]
        
        for i in range(n):
            if g & 1<<i:
                cnt += 1
                for j in range(9):
                    nx = i+1 + dx[j]
                    ny = 1 + dy[j]
                    if 0<=nx<n and 0<=ny<m:
                        bolbs[nx][ny] = not bolbs[nx][ny]
        
        for i in range(2,n):
            for j in range(2,m):
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