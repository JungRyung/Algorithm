###### 금광 ######
import sys
        
answer = []
t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    array = list(map(int, sys.stdin.readline().split()))
    mine = [[] for _ in range(n)]
    dynamic_arr = [[] for _ in range(n)]

    for j in range(n*m):
        row = j // m
        mine[row].append(array[j])
    
    for j in range(m):
        for k in range(n):
            if j==0:
                dynamic_arr[k].append(mine[k][j])
            else:
                if k==0:
                    left_up = 0
                else:
                    left_up = dynamic_arr[k-1][j-1]
                if k==n-1:
                    left_down = 0
                else:
                    left_down = dynamic_arr[k+1][j-1]
                left = dynamic_arr[k][j-1]
                dynamic_arr[k].append(mine[k][j] + max(left_up,left_down,left))
    print(dynamic_arr)
    max_cnt = 0
    for j in range(n):
        max_cnt = max(max_cnt,dynamic_arr[j][-1])
    answer.append(max_cnt)
    
for ans in answer:
    print(ans)
    