##### 쉬운 계단 수 #####
# URL : https://www.acmicpc.net/problem/10844
n = int(input())
num_cnt = 0

def find_stair_num(num,n,cnt):
    global num_cnt
    if cnt == n:
        num_cnt += 1
        return
    else:
        if 0 < num < 9:
            find_stair_num(num-1,n,cnt+1)
            find_stair_num(num+1,n,cnt+1)
        elif num == 0:
            find_stair_num(1,n,cnt+1)
        elif num == 9:
            find_stair_num(8,n,cnt+1)

for i in range(1,10):
    find_stair_num(i,n,1)

print(num_cnt)