##### 셀프 넘버 #####
# URL : https://www.acmicpc.net/problem/4673

visited = [False] * 10001

def make_sequence(num):
    if num > 10000:
        return
    visited[num] = True
    next_num = num
    while num>0:
        next_num += num % 10
        num //= 10
    make_sequence(next_num)

for i in range(1,10001):
    # 아직 방문한 적 없는 수 = 셀프 넘버
    if visited[i] == False:
        print(i)
        make_sequence(i)
    else:
        make_sequence(i)

