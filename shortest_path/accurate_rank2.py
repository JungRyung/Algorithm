INF = int(1e9)

n, m = map(int, input().split())
table = [[INF]*(n+1) for _ in range(n+1)]
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            table[a][b] = 0

for _ in range(m):
    start, end = map(int, input().split())
    table[start][end] = 1

# 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            table[a][b] = min(table[a][b], table[a][k]+table[k][b])

answer = 0
for i in range(1,n+1):
    cnt = 0
    for j in range(1,n+1):
        if table[i][j]!=INF or table[j][i]!=INF:
            cnt+=1
    if cnt == n:
        answer += 1
print(answer)