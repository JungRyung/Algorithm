##### 플로이드 #####
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

table = [[0]*(n+1) for _ in range(n+1)]
table2 = [[0]*(n+1) for _ in range(n+1)]
table2[1][2] = 2
table2[1][3] = 3
table2[1][4] = 1
table2[1][5] = 10
table2[2][4] = 2
table2[3][4] = 1
table2[3][5] = 1
table2[4][5] = 3
table2[3][1] = 8
table2[5][1] = 7
table2[5][2] = 4

# for _ in range(m):
#     start, end, pay = map(int,sys.stdin.readline().split())
#     if table[start][end] == 0:
#         table[start][end] = pay
#     else:
#         table[start][end] = min(table[start][end], pay)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if table2[i][k]!=0 and table2[k][j]!=0 and i!=j:
                if table2[i][j]==0:
                    table2[i][j] = table2[i][k]+table2[k][j]
                else: 
                    table2[i][j] = min(table2[i][j], table2[i][k]+table2[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        print(table2[i][j], end=' ')
    print()