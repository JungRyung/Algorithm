###### 금광 ######
import sys

def search_gold(pos,mine,gold_num,n,m):
    x, y = pos
    gold_num += mine[x][y]
    if y+1==m:
        return gold_num
    else:
        tmp = 0
        if x-1>=0:
            tmp = max(tmp,search_gold((x-1,y+1),mine,gold_num,n,m))
        tmp = max(tmp,search_gold((x,y+1),mine,gold_num,n,m))
        if x+1<n:
            tmp = max(tmp,search_gold((x+1,y+1),mine,gold_num,n,m))
        return tmp
        
answer = []
t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    array = list(map(int, sys.stdin.readline().split()))
    mine = [[] for _ in range(n)]

    for j in range(n*m):
        row = j // m
        mine[row].append(array[j])
    tmp = 0
    for j in range(n):
        tmp = max(tmp,search_gold((j,0),mine,0,n,m))
    answer.append(tmp)
print(answer)
    