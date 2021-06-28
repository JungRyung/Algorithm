##### 프린터 큐 #####
# URL : https://www.acmicpc.net/problem/1966
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))

    target = m
    cnt = 1
    while True:
        tmp = queue[0]
        is_max = True
        for j in queue:
            if j > tmp:
                is_max = False
        if is_max:
            queue.pop(0)
            if target == 0:
                break
            else:
                cnt += 1
                target -= 1
        else:
            queue.append(queue.pop(0))
            target -= 1
            if target < 0:
                target = len(queue)-1
            
    print(cnt)
