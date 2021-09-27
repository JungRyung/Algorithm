'''
TITLE   : 불 끄기
URL     : https://www.acmicpc.net/problem/14939
DATE    : 21.09.23
'''
import sys
INF = 10e9

dx = [-1,0,1,0,0]
dy = [0,-1,0,1,0]

# def switch(arr, x, y):
#     if arr[x][y] == 1:
#         arr[x][y] = 0
#     else:
#         arr[x][y] = 1
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if not(0<=nx<10 and 0<=ny<10):
#             continue
#         if arr[nx][ny] == 1:
#             arr[nx][ny] = 0
#         else:
#             arr[nx][ny] = 1

# def sum_list(bolbs):
#     total = 0
#     for i in range(10):
#         total += sum(bolbs[i])
#     return total

def print_bolbs(bolbs):
    for i in range(10):
        for j in range(10):
            if bolbs[i][j] == True:
                print('O',end='')
            else:
                print('#',end='')
        print()

bolbs = []
for _ in range(10):
    line = list(sys.stdin.readline().strip())
    tmp_list = []
    for ch in line:
        if ch =='O':
            tmp_list.append(True)
        else:
            tmp_list.append(False)
    bolbs.append(tmp_list)

ans = INF
for b in range(1<<10):
    cnt = 0
    arr = []
    for i in range(10):
        arr.append(bolbs[i][:])

    for i in range(10):
        if b & 1<<i:
            cnt += 1
            for j in range(5):
                nx = 0 + dx[j]
                ny = i + dy[j]
                if 0<=nx<10 and 0<=ny<10:
                    arr[nx][ny] = not arr[nx][ny]

    for i in range(1,10):
        for j in range(10):
            if arr[i-1][j] == True:
                cnt += 1
                for k in range(5):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<10 and 0<=ny<10:
                        arr[nx][ny] = not arr[nx][ny]

    if True not in arr[-1]:
        ans = min(ans, cnt)

if ans != INF:
    print(ans)
else:
    print(-1)