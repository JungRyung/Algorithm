##### 정확한 순위 #####
import sys
n, m = map(int, sys.stdin.readline().split())
table = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    table[start][end] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if table[i][k]!=0 and table[k][j]!=0 and i!=j:
                if table[i][j] == 0:
                    table[i][j] = 1

answer = 0
for i in range(1,n+1):
    cnt = 0
    # i보다 성적이 높은 학생의 수
    cnt += table[i].count(1)
    # i보다 성적이 낮은 학생의 수
    for j in range(1,n+1):
        if table[j][i] == 1:
            cnt += 1
    if cnt == n-1:
        answer += 1

print(answer)