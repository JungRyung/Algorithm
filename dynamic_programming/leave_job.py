import sys

n = int(sys.stdin.readline())
works = []
for i in range(n):
    t, p = map(int, sys.stdin.readline().split())
    works.append((t,p))
schedule = [False]*n

def sum_pay(schedule,idx,sum):
    # idx가 마지막이면 return
    if idx == n:
        return sum
    else:
        # 해당 상담을 할 수 있는 스케줄인지
        if schedule[idx]==False and idx+works[idx][0]-1 < n:
            # 해당 상담을 맡는경우와 안맞는 경우 비교 리턴
            no = sum_pay(schedule,idx+1,sum)
            for i in range(idx,idx+works[idx][0]):
                schedule[i] = True
            sum += works[idx][1]
            yes = sum_pay(schedule,idx+1,sum)
            max_pay = max(no,yes)
            return max_pay
        else:
            return sum_pay(schedule,idx+1,sum)

answer = sum_pay(schedule,0,0)
print(answer)