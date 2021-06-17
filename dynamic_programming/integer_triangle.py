import sys

n = int(sys.stdin.readline())
tree = [[] for _ in range(n)]
da = [[] for _ in range(n)]

for i in range(n):
    tree[i] = list(map(int,sys.stdin.readline().split()))
    da[i] = tree[i]

for i in range(n):
    row_len = len(tree[i])
    for j in range(row_len):
        if i==0:
            da[0] = tree[i]
        else:
            # 왼쪽 위
            if j==0:
                left_up = 0
            else:
                left_up = da[i-1][j-1]
            # 오른쪽 위
            if j==(row_len-1):
                right_up = 0
            else:
                right_up = da[i-1][j]
            da[i][j] = tree[i][j] + max(left_up,right_up)

answer = 0
for i in range(len(da[-1])):
    answer = max(answer, da[-1][i])

print(answer)